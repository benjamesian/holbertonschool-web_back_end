export default function appendToEachArrayValue(array, appendString) {
  const arr = array;
  for (const [idx, el] of Object.entries(array)) {
    arr[idx] = appendString + el;
  }

  return arr;
}
