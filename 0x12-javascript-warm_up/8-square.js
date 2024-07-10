#!/usr/bin/node
// hi

const x = process.argv;
let i = 0;
if (x[2] === undefined) {
  console.log('Missing size');
}
for (; i < Number(x[2]); i++) {
  let l = "";
  for (let j = 0; j < Number(x[2]); j++) {
    l += 'X';
  }
  console.log(l);
}
