#!/usr/bin/node
const processes = require('process');
const argv = processes.argv;
function add (a, b) {
  a = Number(a);
  b = Number(b);
  console.log(a + b);
}

add(argv[2], argv[3]);
