/**
 * 알고리즘 문제 풀이 때 JavaScript 입력을 도와주는 클래스입니다.
 * 아래 메서드들을 이용해서 텍스트 입력을 받을 수 있습니다.
 *
 * 제출 시에는 맨 처음 HAS_INPUT_FILE 변수를 포함해서,
 * 맨 끝 new Input()까지 복사해서 붙여넣어야 합니다.
 *
 * 입력 예시
 * - 한 줄에 있는 문자열 하나:
 * `const word = input.readStr();`
 *
 * - 한 줄에 있는 문자열 여러 개:
 * `const words = input.readStr().split(" ");`
 *
 * - 한 줄에 있는 정수 한 개:
 * `const n = input.readInt();`
 *
 * - 한 줄에 있는 정수 여러 개:
 * `const numbers = input.readStr().split(" ").map(x => parseInt(x));`
 */

// 파일 입력이 필요한 경우 true로 바꾸기
const HAS_INPUT_FILE = false;
// 입력 텍스트 파일 이름은 {현재 파일 이름}.txt 형식임
const INPUT_FILE_SUFFIX = ".txt";

/** @param {Input} input */
function solution(input) {
  // 아래 있는 코드들은 전부 사용 예시입니다.
  // 문제를 풀 때는 전부 지우시면 됩니다.

  // 한 줄에 있는 정수 한 개
  const n = input.readInt();
  console.log("N: ", n);

  // 한 줄에 있는 정수 여러 개
  const numbers = input
    .readStr()
    .split(" ")
    .map((str) => parseInt(str));
  console.log("numbers: ", numbers);

  // 여러 줄에 있는 정수 여러 개
  let arr = [];
  for (let i = 0; i < 4; i++) {
    const numbers = input
      .readStr()
      .split(" ")
      .map((str) => parseInt(str));
    arr.push(numbers);
  }
  console.log("arr: ", arr);

  // 한 줄에 있는 문자열 한 개
  const string = input.readStr();
  // 한 줄에 있는 문자열 여러 개
  const words = input.readStr().split(" ");
  console.log(string, "/", words);

  // 여러 줄에 있는 문자열 여러 개
  let wordArr = [];
  for (let i = 0; i < 4; i++) {
    const words = input.readStr().split(" ");
    wordArr.push(words);
  }
  console.log(wordArr);
}

//////////////////////////////////////////////////

class Input {
  #inputs = [];

  constructor() {
    this.#run();
  }

  #run() {
    const readline = require("readline");
    const reader = readline.createInterface({
      input: this.#getInputStream(),
      output: process.stdout,
    });

    reader
      .on("line", (line) => {
        this.#inputs.push(line);
      })
      .on("close", () => {
        if (HAS_INPUT_FILE) {
          // 파일 입력 시, 입력과 출력 사이를 띄우기 위해 한 줄 추가
          console.log("");
        }

        solution(this);
        process.exit();
      });
  }

  #getInputStream() {
    if (HAS_INPUT_FILE) {
      return this.#getInputStreamAsFile();
    } else {
      // process.stdin은 터미널 통해 입력하는 걸 의미
      return process.stdin;
    }
  }

  #getInputStreamAsFile() {
    const fs = require("fs");
    const inputFileName = this.#getInputFileName();
    const fileStream = fs.createReadStream(inputFileName);
    return fileStream;
  }

  #getInputFileName() {
    const path = require("path");
    // __filename은 special attribute 중 하나이며 전체 경로 포함.
    // basename 결과는 파일명만 (+확장자 포함).
    const fileName = path.basename(__filename);
    const fileNameRoot = fileName.split(".")[0];
    return `${fileNameRoot}${INPUT_FILE_SUFFIX}`;
  }

  /** @returns {number} */
  readInt() {
    this.#checkHasInput();
    const number = this.#checkTypeAndGet("number");
    return Number(number);
  }

  /** @returns {string} */
  readStr() {
    this.#checkHasInput();
    const str = this.#checkTypeAndGet("string");
    return str.trim();
  }

  #checkHasInput() {
    if (this.#inputs.length === 0) {
      console.log("InputError: Not enough inputs");
    }
  }

  /**
   * @param {('string'|'number')} type
   * @returns {string|number}
   */
  #checkTypeAndGet(type) {
    const input = this.#inputs.shift();
    if (typeof input === "string") {
      return input;
    } else if (typeof Number(input) === "number") {
      return input;
    } else {
      console.log("InputError:", input, "is not", type);
    }
  }
}

new Input();
