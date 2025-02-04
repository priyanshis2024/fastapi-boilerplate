""" This file contains the constants"""

from enum import Enum


class Gender(int, Enum):
    MALE = 1
    FEMALE = 2
    NON_BINARY = 3
    PREFER_NOT_TO_ANSWER = 4


class Status(int, Enum):
    DISABLED = 0
    ENABLED = 1
    BLOCKED = 2
