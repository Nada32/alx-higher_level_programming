#!/usr/bin/node
// hi

const x = process.argv;
let i = 0;
if (typeof (Number(x[2])) !==  'number') {
  console.log('Missing size');
}
for (; i < Number(x[2]); i++) {
  let l = '';
  for (let j = 0; j < Number(x[2]); j++) {
    l += 'X';
  }
  console.log(l);
}
