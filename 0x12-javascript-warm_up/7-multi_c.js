#!/usr/bin/node
// hi

const x = process.argv;
const myVar = 'C is fun';
let i = 0;
if (x[2] === undefined) {
  console.log('Missing number of occurrences');
}
for (; i < Number(x[2]); i++) {
  console.log(myVar);
}
