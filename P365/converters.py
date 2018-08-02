class UintWithoutZero:
    regex = '[0-9]+'

    @staticmethod
    def to_python(value):
        return int(value)

    @staticmethod
    def to_url(value):
        return value
