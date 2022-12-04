from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    counter = 0
    for line in lines:
        e1, e2 = line.split(',')
        e1_a, e1_b = e1.split('-')
        e2_a, e2_b = e2.split('-')

        e1_r = set(range(int(e1_a), int(e1_b) + 1))
        e2_r = set(range(int(e2_a), int(e2_b) + 1))
        match = e1_r.issubset(e2_r) or e2_r.issubset(e1_r)
        if match:
            counter += 1

    return counter


INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 2

INPUT_S2 = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
2-6,4-8
'''
EXPECTED2 = 1


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
