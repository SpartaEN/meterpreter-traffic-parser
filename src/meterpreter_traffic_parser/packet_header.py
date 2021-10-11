from .exceptions import BadPacketHeader
from .helpers import ENDIAN, xor_decrypt
from .enums import PacketTLVType


class PacketHeader:
    def __init__(self, data: bytes) -> None:
        if len(data) != 32:
            raise BadPacketHeader(f"Packet header length must be 32 bytes")
        zero_byte_pos = data[0:4].find(b"\x00")
        if zero_byte_pos != -1:
            raise BadPacketHeader(f"Bad XOR key at position {zero_byte_pos}")
        self.pkt_xor_key = data[0:4]
        data = xor_decrypt(self.pkt_xor_key, data[4:32])
        self.pkt_session_guid = data[0:16].hex()
        self.pkt_enc_flags = int.from_bytes(data[16:20], ENDIAN)
        self.pkt_tlv_length = int.from_bytes(data[20:24], ENDIAN)
        self.pkt_type = int.from_bytes(data[24:28], ENDIAN)

    def get_xor_key(self):
        return self.pkt_xor_key

    def get_session_guid(self):
        return self.pkt_session_guid

    def get_enc_flags(self):
        return self.pkt_enc_flags

    def get_length(self):
        return self.pkt_tlv_length

    def get_type(self):
        return self.pkt_type

    def get_type_text(self):
        return PacketTLVType.get_by_value(self.pkt_type)

    def describe(self):
        print(f"session_guid: {self.get_session_guid()}")
        print(f"enc_flags: {self.get_enc_flags()}")
        print(f"payload length (including tlv): {self.get_length()}")
        print(f"type: {self.get_type_text()}")
