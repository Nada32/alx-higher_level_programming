#!/usr/bin/node
// hi

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w !== undefined && h !== undefined) && (w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let l = '';
      for (let j = 0; j < this.width; j++) {
        l += 'X';
      }
      console.log(l);
    }
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }

  rotate () {
    let z = 0;
    z = this.width;
    this.width = this.height;
    this.height = z;
  }
};
