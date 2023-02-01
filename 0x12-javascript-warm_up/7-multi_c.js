#!/usr/bin/node
const processes = require('process');
const argv = processes.argv;
let num = argv[2];
num = Number(num);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (num > 0) {
    console.log('C is fun');
    num--;
  }
}
