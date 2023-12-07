const fs = require('fs');
const text = fs.readFileSync('./input.txt').toString('utf-8');
const regex = /\d+/gi;

let [times, distances] = text.split('\n');
times = times.split(':')[1].match(regex).map(Number);
distances = distances.split(':')[1].match(regex).map(Number);

const f = (time, distance) => {
  let winningDistances = [];

  for (let j = 1; j < time; j++) {
    const formula = (time - j) * j;

    if (formula > distance) {
      winningDistances.push(formula);
    }
  }

  return winningDistances.length;
};

let resultP1 = 1;
for (let x of [...Array(times.length).keys()]) {
  resultP1 *= f(times[x], distances[x]);
}

const resultP2 = f(times.join(''), distances.join(''));

console.log(resultP1);
console.log(resultP2);
