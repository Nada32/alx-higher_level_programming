#!/usr/bin/node
// hi

function big (a) {
  let z = 0;
  if ((a.length === 3)) {
    return (0);
  } else {
      for (let i = 0; i < a.length; a++) {
        if (z <= i) {
          z = i;
        }
      }
  }
  return (z);
}
const x = process.argv;
const xx = Number(x[2]);
console.log(big(xx));
