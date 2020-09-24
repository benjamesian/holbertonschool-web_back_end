export default function createInt8TypedArray(length, position, value) {
  const a = new ArrayBuffer(8 * length);
  const b = new Int8Array(a);
  b[position] = value;
  return b;
}
