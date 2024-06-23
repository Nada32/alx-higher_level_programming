#!/usr/bin/node
// hi

const x = process.argv;
for (let i = 2; i < 4; i++) {
  if ((x[i] === undefined) || (x.length === 3)) {
    console.log(x[i] + ' is undefined');
    break;
  } console.log(x[i]);
}
