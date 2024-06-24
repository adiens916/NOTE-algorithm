var inputFile = "";
if (process.platform === "linux") {
  inputFile = "/dev/stdin";
} else {
  const filePath = require("path").parse(__filename);
  inputFile = `${filePath.dir}\\${filePath.name}.txt`;
}

const input = require("fs").readFileSync(inputFile).toString().split(" ");
const A = parseInt(input[0]);
const B = parseInt(input[1]);
console.log(A + B);
