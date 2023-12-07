const fs = require('fs');
const data = fs.readFileSync('input.txt').toString('utf-8');

const lines = data.split('\n');
const regex = /\d+/g;
let p1 = 0;

for (let [index, line] of lines.entries()) {
  const [first, rest] = line.split('|');
  const [id_, card] = first.split(':');
  const rests = Array.from(new Set(rest.match(regex).map(Number)));
  const cards = Array.from(new Set(card.match(regex).map(Number)));

  // this is "intersection" in js
  let val = cards.filter((x) => rests.includes(x)).length;
  if (val > 0) {
    p1 += Math.pow(2, val - 1);
  }
}
console.log(p1);
