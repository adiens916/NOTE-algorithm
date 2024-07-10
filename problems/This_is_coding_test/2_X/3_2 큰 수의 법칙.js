/**
 * @param {string[]} inputs
 */
function solution(inputs) {
  const [N, M, K] = inputs[0].split(" ").map((value) => parseInt(value));
  let numArr = inputs[1].split(" ").map((value) => parseInt(value));

  numArr.sort();
  const largest1 = numArr[N - 1];
  const largest2 = numArr[N - 2];

  const repCount = Math.floor(M / (K + 1));
  const remains = M % (K + 1);

  let sum = repCount * (largest1 * K + largest2);
  sum += remains * largest1;
  console.log(sum);
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

// 5 8 3
// 2 4 5 4 6
// # 46

// 5 7 2
// 3 4 3 4 3
// # 28
