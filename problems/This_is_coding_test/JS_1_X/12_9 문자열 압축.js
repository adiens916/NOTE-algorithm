/**
 * @param {string} s
 * @param {number} range
 * @returns string
 */
function compress(s, range) {
  let totalCount = 0;
  let count = 1;

  let start = 0;
  while (start < s.length) {
    // XXX: JavaScript에서도 substring을 쓰는데, Python처럼 관용적임...
    let prev = s.substring(start, start + range);
    let next = s.substring(start + range, start + range * 2);

    if (prev == next) {
      count += 1;
    } else {
      totalCount += prev.length + (count > 1 ? String(count).length : 0);
      count = 1;
      prev = next;
    }

    start += range;
  }

  return totalCount;
}

/**
 * @param {string[]} inputs
 */
function solution(inputs) {
  const s = inputs[0].toString();
  let minTotalCount = s.length;

  const mid = Math.floor(s.length / 2);
  for (let range = 1; range <= mid; range++) {
    const compressedCount = compress(s, range);
    minTotalCount =
      minTotalCount < compressedCount ? minTotalCount : compressedCount;
  }

  return minTotalCount;
}

const rl = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
  inputs.push(line);
}).on("close", () => {
  const answer = solution(inputs);
  console.log(answer);
  process.exit();
});

/**
 * abcabcabcabcdededededede
 * # 14
 */
