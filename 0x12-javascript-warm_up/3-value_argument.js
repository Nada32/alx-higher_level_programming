#!/usr/bin/node
// hi

const x = process.argv;
if (x[2] === undefined) {
  console.log('No argument');
} else {
  console.log(x[3]);
}
