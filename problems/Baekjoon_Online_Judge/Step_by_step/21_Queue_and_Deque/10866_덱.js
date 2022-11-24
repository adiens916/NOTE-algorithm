/** @param {Input} input */
function solution(input) {
  const N = input.readInt();
  const dequeue = new Deque(N);

  for (let i = 0; i < N; i++) {
    const inputs = input.readStr().split(" ");
    const { command, X } = splitInput(inputs);
    dequeue[command](X);
  }
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
  max = 0;
  head = -1;
  tail = -1;
  count = 0;

  constructor(N) {
    this.dequeue = Array(N);
    this.max = N;
  }

  push_front(X) {
    // 앞으로 이동
    this.head -= 1;
    // 넣기 전 인덱스 유효해야 함
    this.head = this.#adjust_index(this.head);

    // 넣기
    this.dequeue[this.head] = X;
    this.count += 1;

    // 다른 쪽 끝도 위치 보장
    this.#sync_index(this.head);
  }

  push_back(X) {
    this.tail += 1;
    this.tail = this.#adjust_index(this.tail);

    this.dequeue[this.tail] = X;
    this.count += 1;

    this.#sync_index(this.tail);
  }

  pop_front() {
    if (this.count > 0) {
      // 제거
      // push 단계에서 유효한 위치를 보장하므로,
      // pop 때는 바로 제거 가능
      const X = this.dequeue[this.head];

      // 뒤로 이동
      this.head += 1;
      this.count -= 1;

      // 이동 후 위치 조정
      this.head = this.#adjust_index(this.head);

      // 다른 쪽도 위치 조정
      this.#sync_index(this.head);

      console.log(X);
    } else {
      console.log(-1);
    }
  }

  pop_back() {
    if (this.count > 0) {
      const X = this.dequeue[this.tail];

      this.tail -= 1;
      this.count -= 1;

      this.tail = this.#adjust_index(this.tail);
      this.#sync_index(this.tail);

      console.log(X);
    } else {
      console.log(-1);
    }
  }

  #adjust_index(index) {
    if (index < 0) {
      index = this.max - 1;
    } else if (index > this.max - 1) {
      index = 0;
    }
    return index;
  }

  #sync_index(index) {
    if (this.count == 1) {
      this.head = index;
      this.tail = index;
    }
  }

  size() {
    console.log(this.count);
  }

  empty() {
    if (this.count == 0) {
      console.log(1);
    } else {
      console.log(0);
    }
  }

  front() {
    if (this.count > 0) {
      console.log(this.dequeue[this.head]);
    } else {
      console.log(-1);
    }
  }

  back() {
    if (this.count > 0) {
      console.log(this.dequeue[this.tail]);
    } else {
      console.log(-1);
    }
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
        console.log("\n");

        solution(this);
        // process.exit();
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

  /** @returns {string} */
  readStr() {
    return this.#inputs.shift().trim();
  }
}

new Input();
