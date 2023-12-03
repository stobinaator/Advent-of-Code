const fs = require('fs');
const input = fs.readFileSync('input.txt').toString('utf-8');

const digits = {
  one: '1',
  two: '2',
  three: '3',
  four: '4',
  five: '5',
  six: '6',
  seven: '7',
  eight: '8',
  nine: '9',
};

const left = {
  oneight: '1',
  eightwo: '8',
  twone: '2',
};

const right = {
  eightwo: '2',
  oneight: '8',
  twone: '1',
};

// const part1 = /\d/gi;
const part2 =
  /\d|oneight|one|twone|two|three|four|five|six|seven|eightwo|eight|nine/gi;
const numbers = [];

input.split('\n').forEach((line) => {
  const found = line.match(part2);

  let leftNum = -1;
  let rightNum = -1;

  if (!isNaN(found[0])) {
    leftNum = found[0];
  } else {
    leftNum = left.hasOwnProperty(found[0]) ? left[found[0]] : digits[found[0]];
  }
  if (!isNaN(found[found.length - 1])) {
    rightNum = found[found.length - 1];
  } else {
    rightNum = right.hasOwnProperty(found[found.length - 1])
      ? right[found[found.length - 1]]
      : digits[found[found.length - 1]];
  }

  const num = Number(leftNum + rightNum);

  numbers.push(num);
});

const result = numbers.reduce(
  (accumulator, currentValue) => accumulator + currentValue,
  0
);
console.log(result);
