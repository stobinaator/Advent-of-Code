from collections import Counter
from typing import Dict
import os

SEGMENTS_TO_DIGITS = {
                        'abcefg': 0,
                        'cf': 1,
                        'acdeg': 2,
                        'acdfg': 3,
                        'bcdf': 4,
                        'abdfg': 5,
                        'abdefg': 6,
                        'acf': 7,
                        'abcdefg': 8,
                        'abcdfg': 9
                    }

class Screen:
    def __init__(self, input_line: str) -> None:
        self.screen_digits = ["".join(sorted(x))
                             for x in input_line.split(' | ')[1].split()]
        self.decoder = Decoder.parse_input(input_line)
        self.decoder.decode()
    
    def decode_screen(self, segments_mapping: Dict[str, str] = SEGMENTS_TO_DIGITS) -> int: 
        screen_digit_num = []
        for screen_digit in self.screen_digits:
            screen_digit_decoded = "".join(sorted(self.decoder.decoding_dict[x] for x in screen_digit))
            screen_digit_as_dig = str(segments_mapping[screen_digit_decoded])
            screen_digit_num.append(screen_digit_as_dig)
        return int("".join(screen_digit_num))

class Decoder:
    def __init__(self, digits:str) -> None:
        # split strings and sort them alphabetically
        self.digits = ["".join(sorted(x)) for x in digits.split()]
        self.decoding_dict = {i: "" for i in 'abcdefg'}

    def decode(self) -> None:
        """
        Maps the letters describing the scrambled digits to 
        the letters from the problem description
        """
        letter_counts = Counter("".join(self.digits))

        # get 1,4,7,8
        code_one = [x for x in self.digits if len(set(x)) == 2][0]
        code_four = [x for x in self.digits if len(set(x)) == 4][0]
        code_seven = [x for x in self.digits if len(set(x)) == 3][0]
        code_eight = [x for x in self.digits if len(set(x)) == 7][0]

        # get a
        (self.decoding_dict['a'], ) = set(code_seven).difference(code_one)

        # get f
        self.decoding_dict['f'] = [k for k,v in letter_counts.items()
                                    if v == 9][0]

        # get e
        self.decoding_dict['e'] = [k for k,v in letter_counts.items()
                                    if v == 4][0]

        # get c
        self.decoding_dict['c'] = [x for x in code_one
                                    if x != self.decoding_dict['f']][0]
        
        # get b
        self.decoding_dict['b'] = [k for k, v in letter_counts.items()
                                    if v == 6][0]

        # get d
        self.decoding_dict['d'] = [x for x in code_four
                                   if (x != self.decoding_dict['b'] and
                                       x != self.decoding_dict['c'] and
                                       x != self.decoding_dict['f'])][0]

        # get g
        self.decoding_dict['g'] = [k for k in self.decoding_dict.keys()
                                    if k not in self.decoding_dict.values()][0]

        # reverse keys and vals for easier decoding
        self.decoding_dict = {v: k for k,v in self.decoding_dict.items()}

    @staticmethod
    def parse_input(input_line: str) -> 'Decoder':
        return Decoder(input_line.split(' | ')[0])

cd = os.path.abspath(os.getcwd())
with open(f'{cd}/input.txt') as f:
    total = sum(Screen(line).decode_screen() for line in f)
print(total)