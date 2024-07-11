#!/usr/bin/node
// hi

function big (a) {
  let z = a[0];
  if ((a.length === 3) || (a[2] === undefined)) {
    return (0);
  } else {
      for (let i = 0; i < a.length; i++) {
        if (z <= a[i]) {
          z = a[i];
        }
      }
    }
    return (z);
}
let z = [0];
const x = process.argv;
for (let i = 0; i < x.length; i++) {
  z[i] = Number(x[i])
}
console.log(big(z));
