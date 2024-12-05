import { readFileSync } from "fs";

// const input =
//   "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";

const input = readFileSync("./puzzle.txt", "utf-8");
console.log(input);

const multipliers = [...input.matchAll(/mul\([0-9]{1,3},[0-9]{1,3}\)/g)];
const result = multipliers.reduce((acc, multiplier) => {
  const [first, second] = multiplier[0]
    .replace("mul(", "")
    .replace(")", "")
    .split(",");
  acc += first * second;
  return acc;
}, 0);
console.log(result);
