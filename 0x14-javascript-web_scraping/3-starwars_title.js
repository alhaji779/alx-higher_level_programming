#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const fUrl = url + process.argv[2];

request.get(fUrl, function (error, response, body) {
  if (error) { console.log(error); } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
