function search(a, b) {
  while (b != 0) {
    t = a;
    a = b;
    b = t % b;
  }
  return a;
}

console.log(search(60, 96));
console.log(search(20, 8));

