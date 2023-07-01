#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const fs = require('fs');
const path = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  fs.writeFile(path, body, err => {
    if (err) {
      console.log(err);
    }
  });
});
