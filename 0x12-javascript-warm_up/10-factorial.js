#!/usr/bin/node
// hi

function factoriall (a) {
  let z = 1;
  if ((a === 1) || (a === 0) || (isNaN(a))) {
    return (1);
  }
  else {
    for (let i = 1; i <= a; i++) {
      z = z * i;
    }
    return (z);
  }
}
const x = process.argv;
const xx = Number(x[2]);
console.log(factoriall(xx));
