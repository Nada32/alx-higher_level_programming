#!/usr/bin/node
// hi

function add (a, b) {
  return (a + b);
}
const x = process.argv;
console.log(add(Number(x[2]), Number(x[3])));
