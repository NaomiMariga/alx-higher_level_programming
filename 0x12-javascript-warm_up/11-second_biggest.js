#!/usr/bin/node
const processes = require('process');
const argv = processes.argv;

if (argv.length === 2) {
  console.log(0);
} else if (argv.length === 3) {
  console.log(0);
} else {
  argv.splice(0, 2);
  argv.sort(function (a, b) { return b - a; });
  console.log(argv[1]);
}
