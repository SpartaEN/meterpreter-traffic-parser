from enum import Enum
from ..exceptions import UnknowType


class TLVType(Enum):
    # Base
    # Represents an undefined/arbitrary value.
    TLV_TYPE_ANY = 0
    # Represents a command identifier.
    TLV_TYPE_COMMAND_ID = 1
    # Represents a request identifier value.
    TLV_TYPE_REQUEST_ID = 2
    # Represents an exception value.
    TLV_TYPE_EXCEPTION = 3
    # Represents a result value.
    TLV_TYPE_RESULT = 4

    # Argument basic types
    # Represents a string value.
    TLV_TYPE_STRING = 10
    # Represents an unsigned integer value.
    TLV_TYPE_UINT = 11
    # Represents a boolean value.
    TLV_TYPE_BOOL = 12

    # Extended types
    # Represents a length (unsigned integer).
    TLV_TYPE_LENGTH = 25
    # Represents arbitrary data (raw).
    TLV_TYPE_DATA = 26
    # Represents a set of flags (unsigned integer).
    TLV_TYPE_FLAGS = 27

    # Channel types
    # Represents a channel identifier (unsigned integer).
    TLV_TYPE_CHANNEL_ID = 50
    # Represents a channel type (string).
    TLV_TYPE_CHANNEL_TYPE = 51
    # Represents channel data (raw).
    TLV_TYPE_CHANNEL_DATA = 52
    # Represents a channel data group (group).
    TLV_TYPE_CHANNEL_DATA_GROUP = 53
    # Represents a channel class (unsigned integer).
    TLV_TYPE_CHANNEL_CLASS = 54
    # Represents a channel parent identifier (unsigned integer).
    TLV_TYPE_CHANNEL_PARENTID = 55

    # Channel extended types
    TLV_TYPE_SEEK_WHENCE = 70
    TLV_TYPE_SEEK_OFFSET = 71
    TLV_TYPE_SEEK_POS = 72

    # Grouped identifiers
    # Represents an exception code value (unsigned in).
    TLV_TYPE_EXCEPTION_CODE = 300
    # Represents an exception message value (string).
    TLV_TYPE_EXCEPTION_STRING = 301

    # Library loading
    # Represents a path to the library to be loaded (string).
    TLV_TYPE_LIBRARY_PATH = 400
    # Represents a target path (string).
    TLV_TYPE_TARGET_PATH = 401
    # Represents a process identifier of the migration target (unsigned integer).
    TLV_TYPE_MIGRATE_PID = 402
    # Represents a migration payload (raw).
    TLV_TYPE_MIGRATE_PAYLOAD = 404
    # Represents a migration target architecture.
    TLV_TYPE_MIGRATE_ARCH = 405
    # Represents a migration technique (unsigned int).
    TLV_TYPE_MIGRATE_TECHNIQUE = 406
    # Represents a migration payload base address (unsigned int).
    TLV_TYPE_MIGRATE_BASE_ADDR = 407
    # Represents a migration payload entry point (unsigned int).
    TLV_TYPE_MIGRATE_ENTRY_POINT = 408
    # Represents a unix domain socket path, used to migrate on linux (string)
    TLV_TYPE_MIGRATE_SOCKET_PATH = 409
    # Represents a migration stub (raw).
    TLV_TYPE_MIGRATE_STUB = 411
    # Represents the name of the ReflectiveLoader function (string).
    TLV_TYPE_LIB_LOADER_NAME = 412
    # Represents the ordinal of the ReflectiveLoader function (int).
    TLV_TYPE_LIB_LOADER_ORDINAL = 413

    # Transport switching
    # Represents the type of transport to switch to.
    TLV_TYPE_TRANS_TYPE = 430
    # Represents the new URL of the transport to use.
    TLV_TYPE_TRANS_URL = 431
    # Represents the user agent (for http).
    TLV_TYPE_TRANS_UA = 432
    # Represents the communications timeout.
    TLV_TYPE_TRANS_COMM_TIMEOUT = 433
    # Represents the session expiration.
    TLV_TYPE_TRANS_SESSION_EXP = 434
    # Represents the certificate hash (for https).
    TLV_TYPE_TRANS_CERT_HASH = 435
    # Represents the proxy host string (for http/s).
    TLV_TYPE_TRANS_PROXY_HOST = 436
    # Represents the proxy user name (for http/s).
    TLV_TYPE_TRANS_PROXY_USER = 437
    # Represents the proxy password (for http/s).
    TLV_TYPE_TRANS_PROXY_PASS = 438
    # Total time (seconds) to continue retrying comms.
    TLV_TYPE_TRANS_RETRY_TOTAL = 439
    # Time (seconds) to wait between reconnect attempts.
    TLV_TYPE_TRANS_RETRY_WAIT = 440
    # List of custom headers to send with the requests.
    TLV_TYPE_TRANS_HEADERS = 441
    # A single transport grouping.
    TLV_TYPE_TRANS_GROUP = 442

    # session/machine identification
    # Represents a machine identifier.
    TLV_TYPE_MACHINE_ID = 460
    # Represents a UUID.
    TLV_TYPE_UUID = 461
    # Represents a Session GUID.
    TLV_TYPE_SESSION_GUID = 462

    # Packet encryption
    # Represents DER-encoded RSA public key
    TLV_TYPE_RSA_PUB_KEY = 550
    # Represents the type of symmetric key
    TLV_TYPE_SYM_KEY_TYPE = 551
    # Represents the symmetric key
    TLV_TYPE_SYM_KEY = 552
    # Represents and RSA-encrypted symmetric key
    TLV_TYPE_ENC_SYM_KEY = 553

    # Pivots
    # Represents the id of the pivot listener
    TLV_TYPE_PIVOT_ID = 650
    # Represents the data to be staged on new connections.
    TLV_TYPE_PIVOT_STAGE_DATA = 651
    # Represents named pipe name.
    TLV_TYPE_PIVOT_NAMED_PIPE_NAME = 653

    # Represents an extension value.
    TLV_TYPE_EXTENSIONS = 20000
    # Represents a user value.
    TLV_TYPE_USER = 40000
    # Represents a temporary value.
    TLV_TYPE_TEMP = 60000

    @staticmethod
    def get_by_value(value):
        for packet_type in TLVType:
            if packet_type.value == value:
                return packet_type.name
        raise UnknowType(f"Unknow packet type, got {value}")


# Not working on some versions :(
# class TLVType(Enum):
#     # Base
#     # Represents an undefined/arbitrary value.
#     TLV_TYPE_ANY = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_NONE.value,        0)
#     # Represents a command identifier.
#     TLV_TYPE_COMMAND_ID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,        1)
#     # Represents a request identifier value.
#     TLV_TYPE_REQUEST_ID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,      2)
#     # Represents an exception value.
#     TLV_TYPE_EXCEPTION = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_GROUP.value,       3)
#     # Represents a result value.
#     TLV_TYPE_RESULT = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,        4)

#     # Argument basic types
#     # Represents a string value.
#     TLV_TYPE_STRING = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,     10)
#     # Represents an unsigned integer value.
#     TLV_TYPE_UINT = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       11)
#     # Represents a boolean value.
#     TLV_TYPE_BOOL = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_BOOL.value,       12)

#     # Extended types
#     # Represents a length (unsigned integer).
#     TLV_TYPE_LENGTH = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       25)
#     # Represents arbitrary data (raw).
#     TLV_TYPE_DATA = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,        26)
#     # Represents a set of flags (unsigned integer).
#     TLV_TYPE_FLAGS = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       27)

#     # Channel types
#     # Represents a channel identifier (unsigned integer).
#     TLV_TYPE_CHANNEL_ID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       50)
#     # Represents a channel type (string).
#     TLV_TYPE_CHANNEL_TYPE = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,     51)
#     # Represents channel data (raw).
#     TLV_TYPE_CHANNEL_DATA = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,        52)
#     # Represents a channel data group (group).
#     TLV_TYPE_CHANNEL_DATA_GROUP = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_GROUP.value,      53)
#     # Represents a channel class (unsigned integer).
#     TLV_TYPE_CHANNEL_CLASS = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       54)
#     # Represents a channel parent identifier (unsigned integer).
#     TLV_TYPE_CHANNEL_PARENTID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       55)

#     # Channel extended types
#     TLV_TYPE_SEEK_WHENCE = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       70)
#     TLV_TYPE_SEEK_OFFSET = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       71)
#     TLV_TYPE_SEEK_POS = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,       72)

#     # Grouped identifiers
#     # Represents an exception code value (unsigned in).
#     TLV_TYPE_EXCEPTION_CODE = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      300)
#     # Represents an exception message value (string).
#     TLV_TYPE_EXCEPTION_STRING = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    301)

#     # Library loading
#     # Represents a path to the library to be loaded (string).
#     TLV_TYPE_LIBRARY_PATH = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    400)
#     # Represents a target path (string).
#     TLV_TYPE_TARGET_PATH = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    401)
#     # Represents a process identifier of the migration target (unsigned integer).
#     TLV_TYPE_MIGRATE_PID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      402)
#     # Represents a migration payload (raw).
#     TLV_TYPE_MIGRATE_PAYLOAD = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,       404)
#     # Represents a migration target architecture.
#     TLV_TYPE_MIGRATE_ARCH = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      405)
#     # Represents a migration technique (unsigned int).
#     TLV_TYPE_MIGRATE_TECHNIQUE = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      406)
#     # Represents a migration payload base address (unsigned int).
#     TLV_TYPE_MIGRATE_BASE_ADDR = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      407)
#     # Represents a migration payload entry point (unsigned int).
#     TLV_TYPE_MIGRATE_ENTRY_POINT = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      408)
#     # Represents a unix domain socket path, used to migrate on linux (string)
#     TLV_TYPE_MIGRATE_SOCKET_PATH = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    409)
#     # Represents a migration stub (raw).
#     TLV_TYPE_MIGRATE_STUB = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,       411)
#     # Represents the name of the ReflectiveLoader function (string).
#     TLV_TYPE_LIB_LOADER_NAME = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    412)
#     # Represents the ordinal of the ReflectiveLoader function (int).
#     TLV_TYPE_LIB_LOADER_ORDINAL = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      413)

#     # Transport switching
#     # Represents the type of transport to switch to.
#     TLV_TYPE_TRANS_TYPE = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      430)
#     # Represents the new URL of the transport to use.
#     TLV_TYPE_TRANS_URL = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    431)
#     # Represents the user agent (for http).
#     TLV_TYPE_TRANS_UA = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    432)
#     # Represents the communications timeout.
#     TLV_TYPE_TRANS_COMM_TIMEOUT = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      433)
#     # Represents the session expiration.
#     TLV_TYPE_TRANS_SESSION_EXP = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      434)
#     # Represents the certificate hash (for https).
#     TLV_TYPE_TRANS_CERT_HASH = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,       435)
#     # Represents the proxy host string (for http/s).
#     TLV_TYPE_TRANS_PROXY_HOST = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    436)
#     # Represents the proxy user name (for http/s).
#     TLV_TYPE_TRANS_PROXY_USER = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    437)
#     # Represents the proxy password (for http/s).
#     TLV_TYPE_TRANS_PROXY_PASS = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    438)
#     # Total time (seconds) to continue retrying comms.
#     TLV_TYPE_TRANS_RETRY_TOTAL = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      439)
#     # Time (seconds) to wait between reconnect attempts.
#     TLV_TYPE_TRANS_RETRY_WAIT = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      440)
#     # List of custom headers to send with the requests.
#     TLV_TYPE_TRANS_HEADERS = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    441)
#     # A single transport grouping.
#     TLV_TYPE_TRANS_GROUP = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_GROUP.value,     442)

#     # session/machine identification
#     # Represents a machine identifier.
#     TLV_TYPE_MACHINE_ID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,    460)
#     # Represents a UUID.
#     TLV_TYPE_UUID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,       461)
#     # Represents a Session GUID.
#     TLV_TYPE_SESSION_GUID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,       462)

#     # Packet encryption
#     # Represents DER-encoded RSA public key
#     TLV_TYPE_RSA_PUB_KEY = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,       550)
#     # Represents the type of symmetric key
#     TLV_TYPE_SYM_KEY_TYPE = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_UINT.value,      551)
#     # Represents the symmetric key
#     TLV_TYPE_SYM_KEY = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,       552)
#     # Represents and RSA-encrypted symmetric key
#     TLV_TYPE_ENC_SYM_KEY = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,       553)

#     # Pivots
#     # Represents the id of the pivot listener
#     TLV_TYPE_PIVOT_ID = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,     650)
#     # Represents the data to be staged on new connections.
#     TLV_TYPE_PIVOT_STAGE_DATA = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_RAW.value,     651)
#     # Represents named pipe name.
#     TLV_TYPE_PIVOT_NAMED_PIPE_NAME = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_STRING.value,  653)

#     # Represents an extension value.
#     TLV_TYPE_EXTENSIONS = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_COMPLEX.value, 20000)
#     # Represents a user value.
#     TLV_TYPE_USER = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_COMPLEX.value, 40000)
#     # Represents a temporary value.
#     TLV_TYPE_TEMP = get_tlv_value(
#         PacketMetaType.TLV_META_TYPE_COMPLEX.value, 60000)

#     @staticmethod
#     def get_by_value(value):
#         for packet_type in TLVType:
#             if packet_type.value == value:
#                 return packet_type.name
#         raise UnknowType(f"Unknow packet type, got {value}")
