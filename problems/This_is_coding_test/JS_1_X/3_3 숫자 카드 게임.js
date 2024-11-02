/**
 * @param {string[]} inputs
 */
function solution(inputs) {
  const [N, M] = inputs[0].split(" ").map((val) => parseInt(val));

  let max = 0;
  for (let i = 1; i < N + 1; i++) {
    const numArr = inputs[i].split(" ").map((val) => parseInt(val));
    const minInLine = numArr.reduce((prev, cur) => (prev < cur ? prev : cur));
    max = minInLine > max ? minInLine : max;
  }

  console.log(max);
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
 * 3 3
 * 3 1 2
 * 4 1 4
 * 2 2 2
 * # 2
 */
