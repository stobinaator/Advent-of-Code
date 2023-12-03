const fs = require('fs');
const input = fs.readFileSync('input.txt').toString('utf-8');

const BAG_CONTAINS = { red: 12, green: 13, blue: 14 };

const cleanUpLinesAndSplitThem = (input) => {
  const splitInput = input.split('\n');
  for (const i in splitInput) {
    splitInput[i] = splitInput[i]
      .replace(`Game ${Number(i) + 1}:`, '')
      .trim()
      .split('; ');
  }
  return splitInput;
};

const getNumberOfPossibleGames = (cleanedUpInput) => {
  let games = [];
  const possible = [];
  let arrayOfGames = [];

  for (const indexOfList in cleanedUpInput) {
    for (const inputs of cleanedUpInput[indexOfList]) {
      const listWithColorsAndValues = inputs.split(', ');
      for (const valueAndColor of listWithColorsAndValues) {
        let [value, color] = valueAndColor.split(' ');
        if (Number(value) > BAG_CONTAINS[color]) {
          games.push(Number(indexOfList) + 1);
        }
      }
    }
  }

  arrayOfGames = Array.from(new Set(games));
  const lenOfInput = input.split('\n').length;

  for (let i = 1; i <= lenOfInput; i++) {
    if (arrayOfGames.includes(i)) continue;
    possible.push(i);
  }

  return possible;
};

const totalSum = (total) => {
  return total.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    0
  );
};

const getNumberOfFewestCubes = (cleanedUpInput) => {
  let fewest = { red: 0, green: 0, blue: 0 };
  let numbers = [];

  for (const indexOfList in cleanedUpInput) {
    for (const inputs of cleanedUpInput[indexOfList]) {
      const listWithColorsAndValues = inputs.split(', ');
      for (const valueAndColor of listWithColorsAndValues) {
        let [value, color] = valueAndColor.split(' ');
        value = Number(value);
        fewest[color] = Math.max(fewest[color], value);
      }
    }
    numbers.push(fewest.red * fewest.blue * fewest.green);
    fewest = { red: 0, green: 0, blue: 0 };
  }
  return numbers;
};

const cleanedUpInput = cleanUpLinesAndSplitThem(input);

// Part 1
const possibleGames = getNumberOfPossibleGames(cleanedUpInput);
const part1 = totalSum(possibleGames);
console.log(part1);

// Part 2
const fewestCubes = getNumberOfFewestCubes(cleanedUpInput);
const part2 = totalSum(fewestCubes);
console.log(part2);
