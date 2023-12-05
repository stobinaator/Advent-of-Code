const fs = require('fs');
const input = fs.readFileSync('input.txt').toString('utf-8');

const buildDecks = (input) => {
  let winningCardsPart1 = [];
  let winningCardsPart2 = [];
  input.split('\n').forEach((line) => {
    let winningNumbersCount = 0;
    const [card, numbers] = line.split(':');

    let [leftNums, rightNums] = numbers.split(' | ');
    leftNums = leftNums
      .trim()
      .split(' ')
      .filter((num) => num !== '');

    rightNums = rightNums
      .trim()
      .split(' ')
      .filter((num) => num !== '');

    for (const num of rightNums) {
      if (leftNums.includes(num)) {
        winningNumbersCount += 1;
      }
    }
    winningCardsPart1.push(winningNumbersCount);
    winningCardsPart2.push([winningNumbersCount]);
  });

  return [winningCardsPart1, winningCardsPart2];
};

const transformDeck = (winningCards) => {
  for (const [index, cardMatches] of winningCards.entries()) {
    for (const match of cardMatches) {
      for (let j = 1; j < match + 1; j++) {
        winningCards[index + j].push(winningCards[index + j][0]);
      }
    }
  }
  return winningCards;
};

let [deckPart1, deckPart2] = buildDecks(input);

const part1 = deckPart1
  .filter((value) => value !== 0)
  .reduce(
    (accumulator, currentValue) =>
      (accumulator += Math.pow(2, currentValue - 1)),
    0
  );

let part2 = 0;
deckPart2 = transformDeck(deckPart2);
deckPart2.forEach((deck) => (part2 += deck.length));

console.log(part1);
console.log(part2);
