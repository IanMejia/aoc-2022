from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> str:
    crates, instructions = s.split('\n\n')

    crates_len = len(crates.splitlines()[-1].rstrip())

    stacks = [[] for _ in range((crates_len + 2)//4)]

    for line in crates.splitlines():
        for pos, crate in enumerate(line[1::4]):
            if not crate.isspace():
                stacks[pos].append(crate)

    [stack.reverse() for stack in stacks]

    for instruction in instructions.splitlines():
        _, n_s, _, f_s, _, d_s = instruction.split()
        [stacks[int(d_s)-1].append(stacks[int(f_s)-1].pop()) for _ in range(int(n_s))]
    return ''.join(stack[-1] if stack else '' for stack in stacks)


INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = 'CMZ'


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
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
