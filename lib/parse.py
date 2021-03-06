import math

from datetime import datetime
from datetime import timedelta


class CardInfo(object):
    def __init__(self, data):
        self.data = data

        self.mask = self.get_mask()

    def get_mask(self) -> list:
        return [
            self.data[6] & 255, self.data[2] & 255, self.data[1] & 255,
            self.data[5] & 255
        ]

    def get_timestamp(self) -> datetime:
        minutes = ((((self.data[40] ^ self.mask[0]) & 1) << 10) |
                   (((self.data[41] ^ self.mask[1]) & 255) << 2)) | ((
                       (self.data[42] ^ self.mask[2]) & 192) >> 6)

        days = (((self.data[39] ^ self.mask[3]) & 63) << 7) | ((
            (self.data[40] ^ self.mask[0]) & 254) >> 1)

        return datetime(2005, 12, 31, 0, 0, 0) + timedelta(
            days=days, minutes=minutes)
