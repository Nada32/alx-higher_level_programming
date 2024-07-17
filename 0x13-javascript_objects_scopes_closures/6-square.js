#!/usr/bin/node
// hi

module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
  charPrint(c) {
    let n = '';
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
    else {
      this.print();
    }
    
  }
};
