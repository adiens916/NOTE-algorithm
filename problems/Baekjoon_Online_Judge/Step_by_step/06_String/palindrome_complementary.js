/**
 * 평문이 주어졌을 때, 뒤에 문자를 최소한으로 붙여서 회문으로 만들어야 함.
 * 이때의 최소한의 길이를 반환.
 *
 * @param {string} plain
 * @example
 *  "abcb" => "abcb+a" => 5
 *  "abcde" => "abcdedcba" => 9
 *  "abb" => "abb+a" => 4
 */
function solution(plain) {
  let minLength = plain.length;
  let axis = Math.floor(plain.length / 2);

  for (axis; axis < plain.length; axis++) {
    // 홀수
    let pairResult = checkPair(plain, axis, (isAxisIncluded = false));
    if (pairResult == true) {
      minLength = axis * 2 + 1;
      break;
    }

    // 짝수
    pairResult = checkPair(plain, axis, (isAxisIncluded = true));
    if (pairResult == true) {
      minLength = (axis + 1) * 2;
      break;
    }
  }

  return minLength;
}

/**
 * 현재 문자열이 axis를 기준으로 대칭인지 확인
 * 문자열 길이가 홀짝인지에 따라 대칭 여부가 바뀜.
 *
 * @param {string} plain
 * @param {number} axis
 * @param {boolean} isAxisIncluded
 */
function checkPair(plain, axis, isAxisIncluded) {
  let isPaired = true;
  const shift = isAxisIncluded ? 1 : 0;

  for (let distance = 0; distance < plain.length - axis; distance++) {
    const left = axis - distance + shift;
    const right = axis + distance;

    if (isOutOfRange(left, right, plain)) {
      break;
    } else if (plain[left] != plain[right]) {
      isPaired = false;
      break;
    }
  }

  return isPaired;
}

function isOutOfRange(left, right, plain) {
  return left < 0 || right >= plain.length;
}

console.log(solution("abcb"));
console.log(solution("abb"));
