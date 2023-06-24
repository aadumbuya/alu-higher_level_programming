#!/usr/bin/node

const argument = process.argv[2];
const numOccurrences = parseInt(argument);

if (!isNaN(numOccurrences)) {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
