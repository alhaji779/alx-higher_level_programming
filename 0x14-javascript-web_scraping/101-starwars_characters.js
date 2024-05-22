#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const mId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${mId}`;

request.get(url, (error, response, body) => {
    if (error){
        console.log(error);
    };
    if (response.statusCode !== 200){
        console.log('Failed to fetch:'+ response.statusCode);
    }

    const datas = JSON.parse(body);
    const data = datas.characters;
    data.forEach(character => {
        request.get(character, (error, response, body) => {
            if (error) {
                console.log(error);
            };
            names = JSON.parse(body);
            console.log(names.name);
            fs.writeFile('castname.txt', names.name, 'utf-8',
        function(error){
            if (error){
                console.log(error);
            }
        });
        });
    });
});
