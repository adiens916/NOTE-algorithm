const partition = function (arr, start, end) {
  const pivot = arr[start]
  let left = start
  let right = end
  let temp = null

  while (left <= right) {
    while (left <= end && arr[left] <= pivot)
      left += 1
    while (right >= 0 && arr[right] > pivot)
      right -= 1

    if (left <= right) {
      temp = arr[left]
      arr[left] = arr[right]
      arr[right] = temp
    } else {
      arr[start] = arr[right]
      arr[right] = pivot
      return [right - 1, left]
    }
  }
}


const quicksort = function (arr, start, end) {
  if (end <= start)
    return

  const bounds = partition(arr, start, end)
  quicksort(arr, start, bounds[0])
  quicksort(arr, bounds[1], end)
}


const arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quicksort(arr, 0, arr.length - 1)
console.log(arr)
