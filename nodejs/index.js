'use strict';

const express = require('express');
const app = express();

app.get('/api/time', (req, res) => {
  res.send({ time: new Date() });
});

app.get('*', (req, res) => {
  res.send(`'${req.url}' endpoint not found.\nAvailable:\n/api/time`);
});

app.listen(8080, '0.0.0.0', () => {
  console.log('Server has been succesfully started');
});
