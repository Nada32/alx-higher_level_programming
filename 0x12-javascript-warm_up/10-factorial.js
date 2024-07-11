#!/usr/bin/node
// hi

const x = process.argv;
const xx = Number(x[2]);
let z = 1;
if ((xx === 1) || (xx === 0) || (isNaN(x[2]))) {
    console.log(1);
  }
else {
  for (let i = 1; i <= xx; i++) {
    z = z * i;
  }
  console.log(z);
}
