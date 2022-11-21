/**
 * JavaScript 입력을 도와주는 클래스.
 * 상황에 맞는 메서드를 골라 입력값 추출.
 * 어떻게 쓰는지는 아래 solution 예시를 참고해 실행시켜보면 됨.
 *
 * 주의: 답안 제출 시 출력 오류가 나는 경우, 71번째의 빈 줄 추가하는 코드 제거하기.
 */

/** @param {Input} input */
function solution(input) {
  const n = input.readInt();
  const numbers = input.readIntArr();
  const arr = input.readIntArrForLines(4);
  console.log("N: ", n);
  console.log("numbers: ", numbers);
  console.log("arr: ", arr);

  const string = input.readStr();
  const words = input.readStrArr();
  const wordArr = input.readStrArrForLines(2);
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
    this.#initReadline();
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

  #initReadline() {
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
