#!/usr/bin/node
const processes = require('process');
const argv = processes.argv;
if (argv.length === 2) {
  console.log('No Argument');
} else if (argv.length === 3) {
  console.log('Argument found');
} else if (argv.length > 3) {
  console.log('Arguments found');
}
