/**
 * @param {string[]} inputs
 */
function solution(inputs) {
  let totalCount = 0;
  const countBy3 = count3InHour();

  const N = parseInt(inputs[0]);
  for (let h = 0; h <= N; h++) {
    // XXX: String(h) 혹은 h.toString()
    if (String(h).includes("3")) {
      totalCount += 3600;
    } else {
      totalCount += countBy3;
    }
  }

  console.log(totalCount);
}

function count3InHour() {
  let count = 0;

  for (let m = 0; m < 60; m++) {
    if (String(m).includes("3")) {
      count += 60;
      continue;
    }
    for (let s = 0; s < 60; s++) {
      if (String(s).includes("3")) {
        count += 1;
      }
    }
  }

  return count;
}

const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
}).on("close", () => {
  solution(inputs);
  process.exit();
});

/**
 * 5
 * # 11475
 */
