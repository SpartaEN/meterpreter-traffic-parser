from .helpers import ENDIAN, parse_tlv_type
import zlib
from .enums import PacketMetaType
from .exceptions import UnknowType


class TLVUnit:
    def __init__(self, data) -> None:
        self.data_header = data[0:8]
        self.data_length = int.from_bytes(self.data_header[0:4], ENDIAN)
        self.data_type = int.from_bytes(self.data_header[4:8], ENDIAN)
        self.data_payload = data[8:self.data_length]
        if self.data_type & PacketMetaType.TLV_META_TYPE_COMPRESSED.value == PacketMetaType.TLV_META_TYPE_COMPRESSED.value:
            self.data_payload = zlib.decompress(self.data_payload)
            self.data_type = self.data_type ^ PacketMetaType.TLV_META_TYPE_COMPRESSED.value

    def get_data(self):
        return self.data_payload

    def get_type(self):
        return self.data_type

    def get_length(self):
        return self.data_length

    def get_payload(self):
        return self.data_payload

    def get_type_text(self):
        # return TLVType.get_by_value(self.data_type)
        return parse_tlv_type(self.data_type)

    def describe(self):
        # print(self.data_header.hex() + self.data_payload.hex())
        try:
            packet_meta, packet_type = self.get_type_text()
            print(f"type: {packet_meta}, {packet_type}")
        except UnknowType as e:
            print(e)
        print(f"length: {self.get_length()}")
        print(f"payload: {self.get_payload()}")
