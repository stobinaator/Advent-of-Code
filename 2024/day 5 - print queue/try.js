import { readFileSync } from "fs";

// pages
function cleanUpPages(pages) {
  const splitPages = pages.split("\n");
  const cleaned = splitPages.map((page) => page.split("|"));
  const converted = cleaned.map(([first, second]) => [
    Number(first),
    Number(second),
  ]);
  return converted;
}

function createPageLookup(pages) {
  let lookup = {};
  for (const page of pages) {
    if (!lookup[page[0]]) {
      lookup[page[0]] = [page[1]];
    } else {
      lookup[page[0]].push(page[1]);
    }
  }
  return lookup;
}

function handlePages(pages) {
  const clean = cleanUpPages(pages);
  const lookup = createPageLookup(clean);
  return lookup;
}

// rules
function cleanUpUpdateRules(rules) {
  const cleanedRules = rules
    .split("\n")
    .map((row) => row.split(",").map(Number));
  return cleanedRules;
}

function findCorrectlyOrderedPageUpdates(lookup, updates) {
  console.log(lookup);

  const result = updates.filter((update) => {
    console.log(update);
    const passes = [];

    for (let i = 0; i < update.length; i++) {
      const number = update[i];
      const splitUpdate = update.slice(i + 1, update.length);

      if (lookup[number]) {
        const pass = splitUpdate.every((val) => lookup[number].includes(val));
        passes.push(pass);
      } else {
        if (i === update.length - 1) {
          continue;
        } else {
          passes.push(false);
        }
      }
    }
    return passes.every((v) => v === true);
  });
  return result;
}

function calculateMiddleValuesPassSum(passes) {
  let result = 0;
  for (let pass of passes) {
    const middle = Math.floor(pass.length / 2);
    result += pass[middle];
  }
  return result;
}

function readFile(filename) {
  const data = readFileSync(filename, "utf-8");
  const [pages, pageRules] = data.split("\n\n");
  const pageLookup = handlePages(pages);
  const updates = cleanUpUpdateRules(pageRules);
  const passes = findCorrectlyOrderedPageUpdates(pageLookup, updates);
  const result = calculateMiddleValuesPassSum(passes);
  console.log(result);
}

function main() {
  readFile("./puzzle.txt");
}

main();
