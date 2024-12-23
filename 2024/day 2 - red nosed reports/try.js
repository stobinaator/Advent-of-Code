import { readFileSync } from "fs";

function returnSplitInput(filename) {
  return readFileSync(filename, "utf-8")
    .split("\n")
    .map((report) => report.split(" ").map(Number));
}

function ascending(report) {
  // 1 3 6 7 9
  const correct = [];
  for (let i = 0; i < report.length - 1; i++) {
    const firstNum = report[i];
    const secondNum = report[i + 1];
    if (firstNum < secondNum) {
      const difference = Math.abs(firstNum - secondNum);
      if (1 <= difference && difference <= 3) {
        correct.push(true);
      }
    }
  }
  console.log(correct, report.length, correct.length);
  return correct.length === report.length - 1 ? true : false;
}

function descending(report) {
  // 7 6 4 2 1
  const correct = [];
  for (let i = 0; i < report.length - 1; i++) {
    const firstNum = report[i];
    const secondNum = report[i + 1];
    if (firstNum > secondNum) {
      const difference = Math.abs(firstNum - secondNum);
      if (1 <= difference && difference <= 3) {
        correct.push(true);
      }
    }
  }
  return correct.length === report.length - 1 ? true : false;
}

function isRepSafe(report) {
  const first = report[0];
  const second = report[1];
  if (first === second) {
    return false;
  }
  return first > second ? descending(report) : ascending(report);
}

function countSafeReports(reports) {
  const count = reports.filter((report) => isRepSafe(report)).length;
  return count;
}

function main() {
  const reports = returnSplitInput("./puzzle.txt");
  const part1 = countSafeReports(reports);
  console.log(part1);
}

main();
