#!/usr/bin/node
const processes = require('process');
const argv = processes.argv;
let num = argv[2];
num = Number(num);
if (!(isNaN(num))) {
  console.log('My Number: ' + num);
} else {
  console.log('Not a number');
}
