const fs = require('fs');
const text = fs.readFileSync('./input.txt').toString('utf-8').split('\n');

// I need this constant in order to convert each hand's character to corresponding value
// this string becomes a hex-number which will get compared
const CARDS = {
  2: 0,
  3: 1,
  4: 2,
  5: 3,
  6: 4,
  7: 5,
  8: 6,
  9: 7,
  T: 8,
  J: 9,
  Q: 'a',
  K: 'b',
  A: 'c',
};

let typeOfHands = {
  high: [],
  one: [],
  two: [],
  three: [],
  full: [],
  four: [],
  five: [],
};

const separateCardsAndBids = (text) => {
  let cards = [];
  let bids = [];
  for (const pair of text) {
    cards.push(pair.split(' ')[0]);
    bids.push(pair.split(' ')[1]);
  }
  return [cards, bids];
};

const getHandOccurrences = (cards) => {
  let handOccurrences = [];

  for (let card of cards) {
    const occurrences = {};
    for (const char of [...card]) {
      if (char in occurrences) {
        occurrences[char] += 1;
      } else {
        occurrences[char] = 1;
      }
    }
    handOccurrences.push(occurrences);
  }

  return handOccurrences;
};

const getTypesOfHands = (hands) => {
  // [{ '5': 2, '8': 2, Q: 1 },...]
  occurrences = getHandOccurrences(hands);

  for (let [index, cardOccur] of occurrences.entries()) {
    const len = Object.values(cardOccur).length;
    let highestOccurrence = Math.max(...Object.values(cardOccur));
    switch (len) {
      case 1:
        typeOfHands['five'].push(index);
        break;
      case 2:
        if (highestOccurrence === 3) {
          typeOfHands['full'].push(index);
        }
        if (highestOccurrence === 4) {
          typeOfHands['four'].push(index);
        }
        break;
      case 3:
        if (highestOccurrence === 2) {
          typeOfHands['two'].push(index);
        }
        if (highestOccurrence === 3) {
          typeOfHands['three'].push(index);
        }
        break;
      case 4:
        if (highestOccurrence === 2) {
          typeOfHands['one'].push(index);
        }
        break;
      case 5:
        typeOfHands['high'].push(index);
        break;
    }
  }
};

const compareAndSort = (handIndices) => {
  let listOfHexNumbers = [];

  for (const hand of handIndices) {
    const cardsToIndices = [...cards[hand]]
      .map((card) => {
        return CARDS[card];
      })
      .join('');

    listOfHexNumbers.push({ index: hand, handIndices: cardsToIndices });
  }

  // [{ index: 899, handIndices: '444c4' }, ..];
  return listOfHexNumbers
    .sort((a, b) => {
      return parseInt(a.handIndices, 16) - parseInt(b.handIndices, 16);
    })
    .map((ind) => ind.index);
};

const arrangeCardsBasedOnRank = () => {
  const finalOrder = [];
  for (const x of Object.values(typeOfHands)) {
    if (x.length === 1) {
      finalOrder.push(...x);
    } else {
      finalOrder.push(...compareAndSort(x));
    }
  }
  return finalOrder;
};

const [cards, bids] = separateCardsAndBids(text);
getTypesOfHands(cards);
const finalOrder = arrangeCardsBasedOnRank();

let result = 0;
for (let [index, order] of finalOrder.entries()) {
  result += (index + 1) * bids[order];
}
console.log(result);
