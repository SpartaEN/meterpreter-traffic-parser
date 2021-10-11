from .packet_header import PacketHeader
from .tlv_unit import TLVUnit
from .helpers import xor_decrypt
from .exceptions import IncompletePayload, AESKeyError
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


class Packet:
    def __init__(self, data, aes_key=b"") -> None:
        self.packet_header = PacketHeader(data[0:32])
        self.tlv_type = self.packet_header.get_type()
        self.tlv_length = self.packet_header.get_length()
        self.payload_length = self.tlv_length - 8
        if (len(data[32:]) != self.payload_length):
            raise IncompletePayload(
                f"Expecting payload length {self.tlv_length}, got {len(data[32:])}")
        self.data_raw = xor_decrypt(
            self.packet_header.get_xor_key(), data[32:])
        # Decrypt packet if enc_flags are set
        if self.packet_header.get_enc_flags() != 0:
            if len(aes_key) != 32:
                raise AESKeyError("Invalid AES Key or AES Key was not set")
            iv = self.data_raw[0:16]
            cipher = AES.new(aes_key, AES.MODE_CBC, iv)
            self.data_raw = unpad(cipher.decrypt(
                self.data_raw[16:]), AES.block_size)
        # Parse all TLVs
        raw = self.data_raw
        self.data_parsed = []
        while len(raw) != 0:
            tlv = TLVUnit(raw)
            raw = raw[tlv.get_length():]
            self.data_parsed.append(tlv)

    def get_packet_header(self):
        return self.packet_header

    def get_parsed_units(self):
        return self.data_parsed

    def describe(self):
        self.get_packet_header().describe()
        print("\nTLV units:")
        for i in self.data_parsed:
            i.describe()
            print("")
