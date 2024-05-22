#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) { console.log(error); }
  if (response.statusCode !== 200) {
    console.log('Error code:' + response.statusCode);
  }
  const records = JSON.parse(body).results;
  let count = 0;
  records.forEach(record => {
    record.characters.forEach(charct => {
      if (charct.includes(18)) {
        count++;
      }
    });

  });
	console.log(count);
});
