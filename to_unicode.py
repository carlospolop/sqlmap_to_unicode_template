import sys
import unicodedata
import urllib.parse
from lib.core.enums import PRIORITY
__priority__ = PRIORITY.NORMAL

transformations = {
    "a": "%c2%aa",
    "b": "%e1%b5%87",
    "c": "%e1%b6%9c",
    "d": "%e1%b5%88",
    "e": "%e1%b5%89",
    "f": "%e1%b6%a0",
    "g": "%e1%b5%8d",
    "h": "%ca%b0",
    "i": "%e1%b5%a2",
    "j": "%ca%b2",
    "k": "%e1%b5%8f",
    "l": "%cb%a1",
    "m": "%e1%b5%90",
    "n": "%e2%81%bf",
    "o": "%c2%ba",
    "p": "%e1%b5%96",
    "q": "%e2%93%a0",
    "r": "%ca%b3",
    "s": "%cb%a2",
    "t": "%e1%b5%97",
    "v": "%e1%b5%9b",
    "w": "%e1%b5%82",
    "x": "%cb%a3",
    "y": "%ca%b8",
    "z": "%e1%b6%bb",

    "A": "%e1%b4%ac",
    "B": "%e1%b4%ae",
    "C": "%e2%84%82",
    "D": "%e1%b4%b0",
    "E": "%e1%b4%b1",
    "F": "%e2%84%b1",
    "G": "%e1%b4%b3",
    "H": "%e1%b4%b4",
    "I": "%e1%b4%b5",
    "J": "%e1%b4%b6",
    "K": "%e1%b4%b7",
    "L": "%e1%b4%b8",
    "M": "%e1%b4%b9",
    "N": "%e1%b4%ba",
    "O": "%e1%b4%bc",
    "P": "%e1%b4%be",
    "Q": "%e2%84%9a",
    "R": "%e1%b4%bf",
    "S": "%e2%93%88",
    "T": "%e1%b5%80",
    "U": "%e1%b5%81",
    "V": "%e2%85%a4",
    "W": "%e1%b5%82",
    "X": "%e2%85%a9",
    "Y": "%e2%93%8e",
    "Z": "%e2%84%a4",

    "'": "%ef%bc%87",
    '"': "%ef%bc%82",
    "-": "%ef%b9%a3",
    ";": "%cd%be",
    "/": "%ef%bc%8f",
    "#": "%ef%b9%9f",
    "=": "%e2%81%bc",
    "$": "%ef%b9%a9",
    "{": "%ef%b9%9b",
    "}": "%ef%b9%9c",
    "<": "%ef%b9%a4",
    "%": "%ef%b9%aa",
    "[": "%ef%bc%bb",
    "\\": "%ef%b9%a8"
}


def dependencies():
    pass

def to_unicode(payload):
    final = ""
    for c in str(payload):
        if c in transformations:
            final += transformations[c]
        else:
            final += c
    return final

def tamper(payload, **kwargs):
    payload = to_unicode(payload)
    return payload
