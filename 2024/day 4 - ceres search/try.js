import { readFileSync } from "fs";

function cleanInput(filename) {
  const data = readFileSync(filename, "utf-8");
  const cleaned = data.split("\n").map((row) => Array.from(row));
  return cleaned;
}

function countLeftRight(input) {
  const rows = input.length;
  const cols = input[0].length;
  let count = 0;

  for (let i = 0; i < rows; i++) {
    let tempCount = 0;
    for (let j = 0; j < cols - 3; j++) {
      const first = input[i][j];
      const second = input[i][j + 1];
      const third = input[i][j + 2];
      const fourth = input[i][j + 3];
      const word = `${first}${second}${third}${fourth}`;
      if (word === "XMAS") {
        tempCount += 1;
      }
    }
    count += tempCount;
  }
  //   console.log(count);
  return count;
}

function countRightLeft(input) {
  const rows = input.length;
  const cols = input[0].length;
  let count = 0;

  for (let i = 0; i < rows; i++) {
    let tempCount = 0;
    // console.log("row", i + 1);
    for (let j = cols - 1; j > 2; j--) {
      //   console.log(i, j);
      const first = input[i][j];
      const second = input[i][j - 1];
      const third = input[i][j - 2];
      const fourth = input[i][j - 3];
      const word = `${first}${second}${third}${fourth}`;
      //   console.log(input[i], word);
      if (word === "XMAS") {
        tempCount += 1;
      }
    }
    count += tempCount;
    // console.log("row ", i + 1, " has ", tempCount);
  }
  //   console.log(count);
  return count;
}

function countTopDown(input) {
  const rows = input.length;
  const cols = input[0].length;
  let count = 0;

  for (let i = 0; i < cols; i++) {
    let tempCount = 0;
    for (let j = 0; j < rows - 3; j++) {
      const first = input[j][i];
      const second = input[j + 1][i];
      const third = input[j + 2][i];
      const fourth = input[j + 3][i];
      const word = `${first}${second}${third}${fourth}`;
      if (word === "XMAS") {
        tempCount += 1;
      }
    }
    count += tempCount;
  }
  //   console.log(count);
  return count;
}

function countBottomUp(input) {
  const rows = input.length;
  const cols = input[0].length;
  let count = 0;

  for (let i = 0; i < cols; i++) {
    let tempCount = 0;
    for (let j = rows - 1; j > 2; j--) {
      const first = input[j][i];
      const second = input[j - 1][i];
      const third = input[j - 2][i];
      const fourth = input[j - 3][i];
      const word = `${first}${second}${third}${fourth}`;
      //   console.log(word);
      if (word === "XMAS") {
        tempCount += 1;
      }
    }
    count += tempCount;
  }
  //   console.log(count);
  return count;
}

function countTopDownRightDiagonal(input) {
  const rows = input.length;
  const cols = input[0].length;
  let count = 0;

  for (let i = 0; i < rows - 3; i++) {
    let tempCount = 0;
    for (let j = 0; j < cols - 3; j++) {
      const first = input[i][j];
      const second = input[i + 1][j + 1];
      const third = input[i + 2][j + 2];
      const fourth = input[i + 3][j + 3];
      const word = `${first}${second}${third}${fourth}`;
      if (word === "XMAS") {
        tempCount += 1;
      }
    }
    count += tempCount;
  }
  //   console.log(count);
  return count;
}

function countTopDownLeftDiagonal(input) {
  const rows = input.length;
  const cols = input[0].length;
  let count = 0;

  for (let i = 0; i < rows - 3; i++) {
    let tempCount = 0;
    for (let j = cols - 1; j >= 3; j--) {
      const first = input[i][j];
      const second = input[i + 1][j - 1];
      const third = input[i + 2][j - 2];
      const fourth = input[i + 3][j - 3];
      const word = `${first}${second}${third}${fourth}`;
      if (word === "XMAS") {
        tempCount += 1;
      }
    }
    count += tempCount;
  }
  //   console.log(count);
  return count;
}

function countBottomUpRigthDiagonal(input) {
  const rows = input.length;
  const cols = input[0].length;
  let count = 0;

  for (let i = rows - 1; i >= 3; i--) {
    let tempCount = 0;
    for (let j = 0; j < cols - 3; j++) {
      //   console.log(i, j);
      const first = input[i][j];
      const second = input[i - 1][j + 1];
      const third = input[i - 2][j + 2];
      const fourth = input[i - 3][j + 3];
      const word = `${first}${second}${third}${fourth}`;
      if (word === "XMAS") {
        tempCount += 1;
      }
    }
    count += tempCount;
  }
  //   console.log(count);
  return count;
}

function countBottomUpLeftDiagonal(input) {
  const rows = input.length;
  const cols = input[0].length;
  let count = 0;

  for (let i = rows - 1; i >= 3; i--) {
    let tempCount = 0;
    for (let j = cols - 1; j >= 3; j--) {
      //   console.log(i, j);
      const first = input[i][j];
      const second = input[i - 1][j - 1];
      const third = input[i - 2][j - 2];
      const fourth = input[i - 3][j - 3];
      const word = `${first}${second}${third}${fourth}`;
      if (word === "XMAS") {
        tempCount += 1;
      }
    }
    count += tempCount;
  }
  //   console.log(count);
  return count;
}

function main() {
  const input = cleanInput("./puzzle.txt");
  const left = countLeftRight(input);
  const right = countRightLeft(input);
  const td = countTopDown(input);
  const bu = countBottomUp(input);
  const tdr = countTopDownRightDiagonal(input);
  const tdl = countTopDownLeftDiagonal(input);
  const bur = countBottomUpRigthDiagonal(input);
  const bul = countBottomUpLeftDiagonal(input);
  const result = left + right + td + bu + tdr + tdl + bur + bul;
  console.log(result);
}
main();
