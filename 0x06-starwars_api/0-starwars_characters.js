#!/usr/bin/node
/**
 * Here wedo something of our code
 */
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

function fetchNamePromises (url) {
  return new Promise((_, __) => {
    request(url, (err, response, body) => {
      if (!err && response.statusCode === 200) {
        const data = JSON.parse(body);
        console.log(data.name);
      }
    });
  });
}

request(url, async (err, response, body) => {
  if (!err && response.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    const promises = [];
    characters.forEach(elt => {
      promises.push(fetchNamePromises(elt));
    });
    Promise.all(promises);
  }
});
