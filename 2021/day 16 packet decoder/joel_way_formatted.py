from typing import List, Tuple
from dataclasses import dataclass
from functools import reduce
import os

cd = os.path.abspath(os.getcwd())


def hex_char_to_bin(hex_char: str) -> str:
    """Convert a hex character to a binary string of lenght 4."""
    return bin(int(hex_char, 16))[2:].zfill(4)


def hex_to_bin(hex_str: str) -> str:
    """Convert a hex string to a binary string."""
    return "".join(hex_char_to_bin(hex_char) for hex_char in hex_str)


assert hex_to_bin("D2FE28") == "110100101111111000101000"

# 110_      100_  (1)0111_ (1)1110_ (0)0101_  000
# version type_id    G1       G2       G3    discard


@dataclass
class Packet:
    version: int
    type_id: int
    subpackets: List["Packet"] = ()
    value: int = None
    op: str = None

    def sum_of_versions(self) -> int:
        return self.version + sum(
            packet.sum_of_versions() for packet in self.subpackets
        )

    def evaluate(self) -> int:
        if self.type_id == 0:
            # sum packet
            return sum(packet.evaluate() for packet in self.subpackets)
        elif self.type_id == 1:
            # product packet
            return reduce(
                lambda x, y: x * y, (packet.evaluate() for packet in self.subpackets)
            )
        elif self.type_id == 2:
            # minimum packet
            return min(packet.evaluate() for packet in self.subpackets)
        elif self.type_id == 3:
            # maximum packet
            return max(packet.evaluate() for packet in self.subpackets)
        elif self.type_id == 4:
            # literal value
            return self.value
        elif self.type_id == 5:
            # greater than packet
            assert len(self.subpackets) == 2
            return (
                1
                if self.subpackets[0].evaluate() > self.subpackets[1].evaluate()
                else 0
            )
        elif self.type_id == 6:
            # less than packet
            assert len(self.subpackets) == 2
            return (
                1
                if self.subpackets[0].evaluate() < self.subpackets[1].evaluate()
                else 0
            )
        elif self.type_id == 7:
            # equal packets
            assert len(self.subpackets) == 2
            return (
                1
                if self.subpackets[0].evaluate() == self.subpackets[1].evaluate()
                else 0
            )
        else:
            raise ValueError(f"Unknown packet type: {self.type_id}")


def parse(byt3s: str, start: int = 0) -> Tuple["Packet", int]:
    """Parse a packet from a byt3s string."""
    # check for all zeros
    if all(byt3s[i] == "0" for i in range(start, len(byt3s))):
        return None

    version = int(byt3s[start : start + 3], 2)
    type_id = int(byt3s[start + 3 : start + 6], 2)
    start += 6

    if type_id == 4:
        # literal
        return _extraction_for_typeid_4(byt3s, start, version, type_id)
    # operator
    length_type_id = byt3s[start]
    start += 1
    nsp = tlib = None
    if length_type_id == "0":
        return _extraction_for_lentype_0(byt3s, start, version, type_id)
    elif length_type_id == "1":
        return _extraction_for_lentype_1(byt3s, start, version, type_id)
    else:
        raise ValueError(f"Unknown length type id: {length_type_id}")


def _extraction_for_lentype_1(byt3s, start, version, type_id):
    nsp = int(byt3s[start : start + 11], 2)
    start += 11
    subpackets = []

    while len(subpackets) < nsp:
        subpacket, start = parse(byt3s, start)
        subpackets.append(subpacket)
    packet = Packet(version, type_id, subpackets=subpackets)
    return packet, start


def _extraction_for_lentype_0(byt3s, start, version, type_id):
    tlib = int(byt3s[start : start + 15], 2)
    start += 15
    end = start + tlib

    subpackets = []
    while True:
        subpacket, start = parse(byt3s, start)
        if subpacket is None:
            break
        subpackets.append(subpacket)
        if start >= end:
            break
    packet = Packet(version, type_id, subpackets=subpackets)
    return packet, start


def _extraction_for_typeid_4(byt3s, start, version, type_id):
    digits = []
    while byt3s[start] == "1":
        digits.append(byt3s[start + 1 : start + 5])
        start += 5
    # and now we have the last byte
    digits.append(byt3s[start + 1 : start + 5])
    start += 5

    value = int("".join(digits), 2)

    packet = Packet(version, type_id, value=value)
    return packet, start


def add_up_all_version_numbers(hex_string: str) -> int:
    """Add up all version numbers in a hex string."""
    byt3s = hex_to_bin(hex_string)
    packet, _ = parse(byt3s)
    return packet.sum_of_versions()


assert add_up_all_version_numbers("8A004A801A8002F478") == 16
assert add_up_all_version_numbers("620080001611562C8802118E34") == 12
assert add_up_all_version_numbers("C0015000016115A2E0802F182340") == 23
assert add_up_all_version_numbers("A0016C880162017C3686B18A3D4780") == 31


def evaluate(hex_string: str) -> int:
    """Evaluate a hex string"""
    byt3s = hex_to_bin(hex_string)
    packet, _ = parse(byt3s)
    return packet.evaluate()


assert evaluate("C200B40A82") == 3
assert evaluate("04005AC33890") == 54
assert evaluate("880086C3E88112") == 7
assert evaluate("CE00C43D881120") == 9
assert evaluate("D8005AC2A8F0") == 1
assert evaluate("F600BC2D8F") == 0
assert evaluate("9C005AC2F8F0") == 0
assert evaluate("9C0141080250320F1802104A08") == 1


if __name__ == "__main__":
    raw = open(f"{cd}/input.txt").read()
    packet, _ = parse(hex_to_bin(raw))
    print(packet.sum_of_versions())
    print(packet.evaluate())
