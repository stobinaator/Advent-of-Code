const fs = require('fs');
const text = fs.readFileSync('./input.txt').toString('utf-8');

const splitLines = text.split('\n');
const NUMBERS = [
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
];

let part1 = 0;
let part2 = 0;

for (const line of splitLines) {
  const p1_digits = [];
  const p2_digits = [];

  const chars = [...line];
  chars.forEach((char, i) => {
    if (!isNaN(char)) {
      p1_digits.push(char);
      p2_digits.push(char);
    }

    for (const value of NUMBERS.entries()) {
      if (line.slice(i).startsWith(value[1])) {
        p2_digits.push(String(value[0] + 1));
      }
    }
  });

  part1 += Number(p1_digits[0] + p1_digits[p1_digits.length - 1]);
  part2 += Number(p2_digits[0] + p2_digits[p2_digits.length - 1]);
}

console.log(part1);
console.log(part2);
