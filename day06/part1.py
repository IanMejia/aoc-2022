from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    packet_pos = 4
    for pos, _ in enumerate(s):
        packet_set = set(s[pos:pos + 4])
        if len(packet_set) == 4:
            packet_pos += pos
            break

    return packet_pos


INPUT_S = '''\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
'''
EXPECTED = 7

INPUT_S2 = '''\
bvwbjplbgvbhsrlpgdmjqwftvncz
'''
EXPECTED2 = 5


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
        (INPUT_S2, EXPECTED2),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
