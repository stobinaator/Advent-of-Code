const fs = require('fs');
const text = fs.readFileSync('./input.txt').toString('utf-8');

const regex = /\d+/g;
const digits = text.match(regex);

const separateTimesAndDistances = (digits) => {
  let times = [];
  let distances = [];

  for (let i = 0; i < digits.length / 2; i++) {
    times.push(digits[i]);
  }
  for (let i = digits.length / 2; i < digits.length; i++) {
    distances.push(digits[i]);
  }
  return [times, distances];
};

const part1 = (times, distances) => {
  let totalDistances = [];
  for (const [index, time] of times.entries()) {
    let winningDistances = [];

    for (let j = 1; j < time; j++) {
      const formula = (time - j) * j;

      if (formula > distances[index]) {
        winningDistances.push(formula);
      }
    }
    totalDistances.push(winningDistances);
  }

  return totalDistances
    .map((distance) => Object.keys(distance).length)
    .reduce((acc, curr) => (acc *= curr), 1);
};

const part2 = (times, distances) => {
  let totalWins = 0;
  for (let j = 1; j < times; j++) {
    if ((times - j) * j > distances) {
      totalWins++;
    }
  }
  return totalWins;
};
const [times, distances] = separateTimesAndDistances(digits);
const resultP1 = part1(times, distances);

const resultP2 = part2(times.join(''), distances.join(''));

console.log(resultP1);
console.log(resultP2);
