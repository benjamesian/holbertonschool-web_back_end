const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http
  .createServer((req, res) => {
    console.log(process.argv);
    switch (req.url) {
      case '/':
        res.end('Hello Holberton School!');
        break;
      case '/students':
        countStudents(process.argv[2])
          .then((data) => res.end(data));
        break;
      default:
        break;
    }
  })
  .listen(1245);

module.exports = app;
