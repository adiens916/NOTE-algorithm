/**
 * @param {string[]} inputs
 */
function solution(inputs) {
  const N = parseInt(inputs[0]);
  const dirs = inputs[1].split(" ");

  const d = {
    L: [0, -1],
    R: [0, 1],
    U: [-1, 0],
    D: [1, 0],
  };

  let row = 1;
  let col = 1;

  for (const c of dirs) {
    const y = row + d[c][0];
    const x = col + d[c][1];

    if (1 <= y && y <= N && 1 <= x && x <= N) {
      row = y;
      col = x;
    }
  }

  console.log(row, col);
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
 * R R R U D D
 * # 3 4
 */
