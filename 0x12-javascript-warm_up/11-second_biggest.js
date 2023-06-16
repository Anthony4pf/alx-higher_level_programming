#!/usr/bin/node

if (process.argv.length <= 2) {
  console.log(0);
} else {
  let biggest = parseInt(process.argv[2]);
  let index = 2;

  for (let i = 2; i < process.argv.length; i++) {
    if (biggest < parseInt(process.argv[i])) {
      index = i;
      biggest = parseInt(process.argv[index]);
    }
  }

  let secondBiggest = parseInt(process.argv[2]);

  for (let i = 2; i < process.argv.length; i++) {
    if (secondBiggest < parseInt(process.argv[i]) && i !== index) {
      secondBiggest = parseInt(process.argv[i]);
    }
  }
  console.log(secondBiggest);
}
