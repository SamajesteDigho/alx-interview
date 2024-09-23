#!/usr/bin/node
/**
 * Here wedo something of our code
 */
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function fetchUrlsInOrder (urls) {
  const promises = urls.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error && response.statusCode === 200) {
          reject(error);
        } else {
          const data = JSON.parse(body).name;
          resolve(data);
        }
      });
    });
  });
  try {
    return await Promise.all(promises);
  } catch (error) {
    return [];
  }
}

request(url, (error, response, body) => {
  if (error && response.statusCode === 200) {
    console.log(`Error: ${error}`);
  } else {
    const characters = JSON.parse(body).characters;
    fetchUrlsInOrder(characters)
      .then(results => {
        results.forEach(name => {
          console.log(name);
        });
      })
      .catch(error => {
        console.log(error);
      });
  }
});
