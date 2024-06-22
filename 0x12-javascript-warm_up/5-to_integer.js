#!/usr/bin/node
// hi

const x = process.argv;
if (typeof (Number(x[2])) !== 'number') {
  console.log('Not a number');
} else {
  console.log('My number: ' + (x[2]));
}
