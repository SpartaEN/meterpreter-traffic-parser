from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from ..exceptions import UnknowType
from ..enums import PacketMetaType, TLVType


ENDIAN = 'big'


def xor_decrypt(xor_key, data) -> bytes:
    result = b''

    for i in range(0, len(data)):
        result += (data[i] ^ xor_key[i % 4]).to_bytes(1, ENDIAN)

    return result


def get_tlv_value(meta, actual):
    return meta | actual


def extract_aes_key(private_key, payload):
    sentinel = get_random_bytes(16)
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_v1_5.new(rsa_key)
    return cipher.decrypt(payload, sentinel)


def parse_tlv_type(value):
    pkt_meta = False
    pkt_type = False
    for packet_meta in PacketMetaType:
        if packet_meta.value & value == packet_meta.value:
            pkt_meta = packet_meta.name
    for tlv_type in TLVType:
        if tlv_type.value & value == tlv_type.value:
            pkt_type = tlv_type.name
    if pkt_meta == False:
        raise UnknowType(f"Unknown packet meta , got {value}")
    if pkt_type == False:
        raise UnknowType(f"Unknown packet type , got {value}")
    return pkt_meta, pkt_type
