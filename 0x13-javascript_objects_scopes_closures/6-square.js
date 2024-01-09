#!/usr/bin/node
const Squarep = require('./5-square');

class Square extends Squarep{
    charPrint (c) {
        if (c === undefined) {
          c = 'X';
        }
        for (let i = 0; i < this.height; i++) {
          let s = '';
          for (let j = 0; j < this.width; j++) {
            s += c;
          }
          console.log(s);
        }
      }
}
module.exports = Square