/**
 * @param {string[]} inputs
 */
function solution(inputs) {
  let [N, K] = inputs[0].split(" ").map((val) => parseInt(val));

  let count = 0;
  while (N > 1) {
    if (N % K == 0) {
      count += 1;
      N = Math.floor(N / K);
    } else {
      // XXX: N이 K보다 작은 경우, N - 1만큼 빼야 함 (아닌 경우, N % K 하면 0이 됨.)
      const remains = N > K ? N % K : N - 1;
      // XXX: count가 먼저 와야 함 (N이 줄어들기 전에)
      count += remains;
      N -= remains;
    }
    // console.log(N, K, count);
  }

  console.log(count);
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
 * 25 5
 * # 2
 * 25 6
 * # - / - - - 5
 */
