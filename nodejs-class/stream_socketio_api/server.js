var http = require('http');
var fs = require('fs');
var count = 0;

const async = require("async");
const sleep = () => new Promise((res, rej) => setTimeout(res, 1000));

const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://kevin87011111:example@cluster0-b9pzv.gcp.mongodb.net/test"

MongoClient.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true },function(err, client) {
  if(err) {
       console.log('Error occurred while connecting to MongoDB Atlas...\n',err);
  }
  console.log('Connected...');


var dbo = client.db("stream_IoT");

var myquery = { stream_name: "A" };

var server = http.createServer(function(res, res) {
  fs.readFile('./index.html', function(err, data){
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(data, 'utf-8');
  })
}).listen(8001, '0.0.0.0');

console.log('server running at http://0.0.0.0:8001');

var io = require('socket.io').listen(server);

io.sockets.on('connection', function(socket) {
    count++;
    (async () => {
      while(1){
        dbo.collection("object_status").find(myquery).toArray(function(err, data) {
          if (err) throw err;
          // console.log(data);
          var data= data[0].stream_A_status;
        // data = "warning";
          console.log('status : ' + data);
          socket.broadcast.emit('stream_1_status', {status: data});
        });
        await sleep();

      }
    })();
    console.log("user connected" + count + 'users');
    socket.broadcast.emit('users', {number: count});
    
    socket.on('disconnect', function() {
        
      count--;
      console.log('user disconnected' + count + 'users');
      socket.broadcast.emit('users', {number: count});
    });

  });
});