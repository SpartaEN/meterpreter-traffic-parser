class BadPacketHeader(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class IncompletePayload(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class UnknowType(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AESKeyError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
