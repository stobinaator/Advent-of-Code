import { readFileSync } from "fs";

function doStuff(input) {
  const characters = Array.from(input);
  console.log(characters);
  let str = "";
  for (let char of characters) {
    str += char;
    console.log(str);

    if (str.match(/mul\([0-9]{1,3}\,[0-9]{1,3}\)/)) {
      console.log("this is a match: ", str);
      //...
    }
  }
}

function main() {
  const input = readFileSync("./input.txt", "utf-8");
  doStuff(input);
}

main();
