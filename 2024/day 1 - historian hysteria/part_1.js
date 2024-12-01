import { readFileSync } from "fs";

function prepareInput(filename) {
  const data = readFileSync(filename, "utf-8");

  const rowsCols = data.split("\n").map((r) => r.split(" "));

  return rowsCols;
}

function splitIntoColumns(input) {
  const firstCol = input.map((r) => r[0]).map(Number);

  const secondCol = input.map((r) => r[r.length - 1]).map(Number);

  return [firstCol, secondCol];
}

function calculateTotalDistance(firstCol, secondCol) {
  firstCol.sort((a, b) => a - b);
  secondCol.sort((a, b) => a - b);

  const diffs = [];
  for (let i = 0; i < firstCol.length; i++) {
    diffs.push(Math.abs(firstCol[i] - secondCol[i]));
  }

  const result = diffs.reduce((acc, val) => {
    return (acc += val);
  }, 0);

  return result;
}

function calculateSimilarityScore(firstCol, secondCol) {
  const occurences = {};
  firstCol.forEach((number) => {
    secondCol.forEach((number2) => {
      if (number === number2) {
        occurences[number] = (occurences[number] || 0) + 1;
      }
    });
  });

  const similarity = Object.entries(occurences).reduce(
    (acc, [k, v]) => acc + k * v,
    0
  );
  return similarity;
}

function main() {
  const input = prepareInput("./puzzle.txt");
  const [first, second] = splitIntoColumns(input);
  const part1 = calculateTotalDistance(first, second);

  const part2 = calculateSimilarityScore(first, second);
  console.log(part1);
  console.log(part2);
}

main();
