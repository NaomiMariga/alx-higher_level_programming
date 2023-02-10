#!/usr/bin/node
const processes = require('process');
let argv = processes.argv;

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

argv = argv[2];
argv = Number(argv);
console.log(factorial(argv));
