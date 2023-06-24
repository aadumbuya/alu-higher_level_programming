#!/usr/bin/node

const argument = process.argv[2];
const parsedInt = parseInt(argument);

if (!isNaN(parsedInt)) {
  console.log('My number: ' + parsedInt);
} else {
  console.log('Not a number');
}
