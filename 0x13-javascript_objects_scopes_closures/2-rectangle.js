#!/usr/bin/node
// hi

module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      this.width = w;
      this.height = h;
    }
  }
};
