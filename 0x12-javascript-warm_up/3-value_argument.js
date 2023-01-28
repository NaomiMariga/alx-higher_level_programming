#!/usr/bin/node
const processes = require('process');
const argv = processes.argv;
if (!(argv[2])) {
  console.log('No arguement');
} else {
  console.log(argv[2]);
}
