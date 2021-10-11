from enum import Enum
from ..exceptions import UnknowType


class PacketTLVType(Enum):
    PACKET_TLV_TYPE_REQUEST = 0
    PACKET_TLV_TYPE_RESPONSE = 1
    PACKET_TLV_TYPE_PLAIN_REQUEST = 10
    PACKET_TLV_TYPE_PLAIN_RESPONSE = 11

    @staticmethod
    def get_by_value(value):
        for packet_type in PacketTLVType:
            if packet_type.value == value:
                return packet_type.name
        raise UnknowType(f"Unknow packet type, got {value}")
