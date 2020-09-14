function appendToEachArrayValue(array, appendString) {
  for (const [idx, el] of Object.entries(array)) {
    array[idx] = appendString + el;
  }

  return array;
}
