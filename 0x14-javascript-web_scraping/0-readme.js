#!/usr/bin/node
const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8',
  function (err, data) {
    if (err) {
      console.log(err);
      return;
    }
    process.stdout.write(data);
  });
