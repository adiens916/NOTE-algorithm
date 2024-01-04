// https://nyang-in.tistory.com/212
// 이해가 안 되면 해당 블로그의 예시 꼭 참고하기

// 조합
function getCombination(array, selectNumber) {
  const results = [];

  if (selectNumber == 1) {
    return array.map((element) => [element]);
  }

  array.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombination(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    results.push(...attached);
  });

  return results;
}

console.log(getCombination([1, 2, 3, 4], 3));

// 순열
function getPermutation(array, selectNumber) {
  const results = [];

  if (selectNumber == 1) {
    return array.map((element) => [element]);
  }

  array.forEach((fixed, index, origin) => {
    // rest 부분만 조합과 다름.
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = getPermutation(rest, selectNumber - 1);
    const attached = permutations.map((permutation) => [fixed, ...permutation]);
    results.push(...attached);
  });

  return results;
}

console.log(getPermutation([1, 2, 3, 4], 3));
