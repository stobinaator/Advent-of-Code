const fs = require('fs');
const text = fs.readFileSync('./input.txt').toString('utf-8');
const splitCode = text.split('\n');

let numbersZeroToNine = [];
for (let i = 0; i < 10; i++) numbersZeroToNine.push(i.toString());

let finalPairs = [];
let pair = [0, 0];

for (let code of splitCode) {
  for (let i = 0; i < code.length; i++) {
    const leftItem = code[i];
    const rightItem = code[code.length - i - 1];

    if (numbersZeroToNine.includes(leftItem) && pair[0] === 0) {
      pair[0] = Number(leftItem);
    }
    if (numbersZeroToNine.includes(rightItem) && pair[1] === 0) {
      pair[1] = Number(rightItem);
    }
    if (pair[0] !== 0 && pair[1] !== 0) break;
  }

  finalPairs.push(...pair);
  pair = [0, 0];
}

let sum = 0;
for (let i = 0; i < finalPairs.length; i += 2) {
  sum += Number(`${finalPairs[i]}${finalPairs[i + 1]}`);
}
console.log(sum);
