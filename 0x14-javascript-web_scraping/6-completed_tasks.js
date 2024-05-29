#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response, body) {
  if (error) { console.log(error); }
  const tasksCompleted = {};
  const sbody = JSON.parse(body);
  sbody.forEach((todo) => {
    if (todo.completed) {
      if (!tasksCompleted[todo.userId]) {
        tasksCompleted[todo.userId] = 1;
      } else {
        tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(tasksCompleted);
});
