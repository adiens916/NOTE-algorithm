/** @param {Input} input */
function solution(input) {
  const N = input.readInt();
  const dequeue = new Deque(N);

  for (let i = 0; i < N; i++) {
    const inputs = input.readStrArr();
    const { command, X } = splitInput(inputs);
    if (X) {
      dequeue[command](X);
    } else {
      dequeue[command]();
    }
  }

  dequeue.print();
}

/** @param {string} inputs */
function splitInput(inputs) {
  const command = inputs[0];

  let X = null;
  if (inputs.length == 2) {
    X = parseInt(inputs[1]);
  }

  return { command, X };
}

class Deque {
  dequeue = Array();
  frontIdx = -1;
  backIdx = -1;
  count = 0;

  constructor(N) {
    this.dequeue = Array(N);
    this.frontIdx = N;
  }

  push_front(X) {
    this.frontIdx -= 1;
    this.dequeue[this.frontIdx] = X;
    this.count += 1;
  }

  push_back(X) {
    console.log("push_back!");
  }

  pop_front() {
    console.log("pop_front!");
  }

  pop_back() {
    console.log("pop_back!");
  }

  size() {
    console.log("size!");
  }

  empty() {
    console.log("empty");
  }

  front() {
    console.log("front!");
  }

  back() {
    console.log("back!");
  }

  print() {
    console.log(this.dequeue);
  }
}

class Input {
  // 기본값은 파일을 통해 입력받음. OJ 제출 시에는 false로 바꿔야 함!
  #inputByFile = true;
  // 입력 텍스트 파일 이름은 {현재 파일 이름}_input.txt 형식임
  #INPUT_FILE_SUFFIX = ".txt";
  #inputFileName = "";
  // process.stdin은 터미널 통해 입력하는 걸 의미
  #inputStream = process.stdin;
  #inputs = [];

  constructor() {
    if (this.#inputByFile) {
      this.#makeInputFileName();
      this.#setInputStreamAsFile();
    }
    this.#run();
  }

  #makeInputFileName() {
    const path = require("path");
    // __filename은 special attribute 중 하나이며 전체 경로 포함.
    // basename 결과는 파일명만 (+확장자 포함).
    const fileName = path.basename(__filename);
    const fileNameRoot = fileName.split(".")[0];
    this.#inputFileName = `${fileNameRoot}${this.#INPUT_FILE_SUFFIX}`;
  }

  #setInputStreamAsFile() {
    const fs = require("fs");
    const fileStream = fs.createReadStream(this.#inputFileName);
    this.#inputStream = fileStream;
  }

  #run() {
    const readline = require("readline");
    const reader = readline.createInterface({
      input: this.#inputStream,
      output: process.stdout,
    });

    reader
      .on("line", (line) => {
        this.#push(line);
      })
      .on("close", () => {
        // 입력과 출력 사이를 띄우기 위해 한 줄 추가
        console.log("");

        solution(this);
        process.exit();
      });
  }

  #push(element) {
    this.#inputs.push(element);
  }

  readInt() {
    return parseInt(this.#inputs.shift());
  }

  /** @returns {Array<number>} */
  readIntArr() {
    return this.#inputs
      .shift()
      .split(" ")
      .map((number) => parseInt(number));
  }

  /** @param {number} lineNumber */
  readIntArrForLines(lineNumber) {
    const lines = [...Array(lineNumber).keys()];
    return lines.map(() => this.readIntArr());
  }

  /** @returns {string} */
  readStr() {
    return this.#inputs.shift().trim();
  }

  /** @returns {Array<string>} */
  readStrArr() {
    return this.#inputs
      .shift()
      .split(" ")
      .map((word) => word);
  }

  /** @param {number} lineNumber */
  readStrArrForLines(lineNumber) {
    const lines = [...Array(lineNumber).keys()];
    return lines.map(() => this.readStrArr());
  }
}

new Input();
