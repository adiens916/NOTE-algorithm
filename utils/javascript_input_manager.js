/**
 * 알고리즘 문제 풀이 때 JavaScript 입력을 도와주는 클래스입니다.
 * 아래 메서드들을 이용해서 텍스트 입력을 받을 수 있습니다.
 *
 * 기본적으로 {파일 이름}_input.txt에 적힌 입력들을 읽어옵니다.
 * 제출 시에는 solution 함수를 포함해서 맨 끝까지 복사해서 붙여넣어야 합니다.
 *
 * 입력 예시
 * - 한 줄에 있는 정수 한 개:
 * `const n = input.readInt();`
 *
 * - 한 줄에 있는 문자열 하나:
 * `const word = input.readStr();`
 *
 * 주의: 답안 제출 시 출력 오류가 나는 경우,
 * 71번째의 빈 줄 추가하는 코드 제거하기.
 */

/** @param {Input} input */
function solution(input) {
  const n = input.readInt();

  const numbers = input
    .readStr()
    .split(" ")
    .map((str) => parseInt(str));

  let arr = [];
  for (let i = 0; i < 4; i++) {
    const numbers = input
      .readStr()
      .split(" ")
      .map((str) => parseInt(str));
    arr.push(numbers);
  }

  console.log("N: ", n);
  console.log("numbers: ", numbers);
  console.log("arr: ", arr);

  const string = input.readStr();
  const words = input.readStr().split(" ");

  let wordArr = [];
  for (let i = 0; i < 4; i++) {
    const words = input.readStr().split(" ");
    wordArr.push(words);
  }

  console.log(string, "/", words);
  console.log(wordArr);
}

class Input {
  // 기본값은 파일을 통해 입력받음. OJ 제출 시에는 false로 바꿔야 함!
  #inputByFile = true;
  // 입력 텍스트 파일 이름은 {현재 파일 이름}_input.txt 형식임
  #INPUT_FILE_SUFFIX = "_input.txt";
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
        this.#inputs.push(line);
      })
      .on("close", () => {
        // 입력과 출력 사이를 띄우기 위해 한 줄 추가
        console.log("");

        solution(this);
        process.exit();
      });
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
