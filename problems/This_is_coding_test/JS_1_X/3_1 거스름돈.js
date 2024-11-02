function solution(inputs) {
  let money = parseInt(inputs[0]);
  let count = 0;
  const coins = [500, 100, 50, 10];

  for (const coin of coins) {
    count += parseInt(money / coin);
    money %= coin;
  }

  console.log(count);
}

// 1260
// # 6
//

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
