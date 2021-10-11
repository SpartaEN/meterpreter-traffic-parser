from enum import Enum
from ..exceptions import UnknowType


class PacketMetaType(Enum):
    # Meta TLV argument type representing a null value.
    TLV_META_TYPE_NONE = 0 << 0
    # Meta TLV argument type representing a string value.
    TLV_META_TYPE_STRING = 1 << 16
    # Meta TLV argument type representing a unsigned integer value.
    TLV_META_TYPE_UINT = 1 << 17
    # Meta TLV argument type representing a raw data value.
    TLV_META_TYPE_RAW = 1 << 18
    # Meta TLV argument type representing a boolean value.
    TLV_META_TYPE_BOOL = 1 << 19
    # Meta TLV argument type representing a quad-word value.
    TLV_META_TYPE_QWORD = 1 << 20
    # Meta TLV argument type representing a compressed data value.
    TLV_META_TYPE_COMPRESSED = 1 << 29
    # Meta TLV argument type representing a group value.
    TLV_META_TYPE_GROUP = 1 << 30
    # Meta TLV argument type representing a nested/complex value.
    TLV_META_TYPE_COMPLEX = 1 << 31
    # Meta TLV argument type representing a flag set/mask value.

    @staticmethod
    def TLV_META_TYPE_MASK(x):
        return x & 0xffff0000

    @staticmethod
    def get_by_value(value):
        for packet_type in PacketMetaType:
            if packet_type.value == value:
                return packet_type.name
        raise UnknowType(f"Unknow packet type, got {value}")
