#!/usr/bin/node

const esrever = (list) => {
  const newArr = [];
  for (const elem of list) {
    newArr.unshift(elem);
  }

  return newArr;
};

module.exports = { esrever };
