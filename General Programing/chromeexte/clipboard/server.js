// npm install -g browserify

const http = require("http");
const hostname = '127.0.0.1';
const port = 3001;
const server = http.createServer( (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
   runScript();
})
server.listen(port, hostname, ()=>{
  console.log("running")
});

function runScript(){
  'use strict';
   const spawn = require("child_process").spawn;
   return spawn('python', ['./reading.py', ]);
}
// const process = spawn('python', ['./reading.py', ]);
