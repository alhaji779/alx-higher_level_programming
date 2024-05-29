#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fPath = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) { console.log(error); }
  if (response.statusCode !== 200) {
    console.log('Code: ' + response.statusCode);
  }

  // const data = JSON.parse(body);
  fs.writeFile(fPath, body, 'utf-8',
    function (err) {
      if (err) { console.log(err); }
    });
});
