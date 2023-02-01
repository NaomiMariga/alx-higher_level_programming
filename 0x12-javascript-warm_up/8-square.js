#!/usr/bin/node
const processes = require('process');
const argv = processes.argv;
let num = argv[2];
num = Number(num);
const num2 = num;
if (isNaN(num)) {
  console.log('Missing size');
} else {
  while (num > 0) {
    console.log('X'.repeat(num2));
    num--;
  }
}
