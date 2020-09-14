export default function appendToEachArrayValue(array, appendString) {
  out = []
  for (const el of array) {
    out.push(appendString + el)
  }

  return out;
}
