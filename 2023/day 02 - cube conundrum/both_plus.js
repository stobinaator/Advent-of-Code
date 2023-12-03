const fs = require('fs');
const input = fs.readFileSync('input.txt').toString('utf-8');

let p1 = 0;
let p2 = 0;
const BAG_CONTAINS = { red: 12, green: 13, blue: 14 };

for (const line of input.split('\n')) {
  let ok = true;
  let fewest = { red: 0, green: 0, blue: 0 };

  const [id_, linee] = line.split(':');
  for (const event of linee.split(';')) {
    for (const balls of event.split(',')) {
      let [n, color] = balls.trim().split(' ');
      n = Number(n);
      fewest[color] = Math.max(fewest[color], n);
      if (n > BAG_CONTAINS[color]) {
        ok = false;
      }
    }
  }
  let score = 1;
  for (const v of Object.values(fewest)) {
    score *= v;
  }
  p2 += score;

  if (ok) {
    p1 += Number(id_.split(' ')[1]);
  }
}
console.log(p1);
console.log(p2);
