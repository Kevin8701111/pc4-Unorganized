var http=require('http');
var fs = require('fs');

var server=http.createServer(function(req,res){
        if(req.url=='/'){
            fs.readFile('./websocket.html', function(err, data){
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(data, 'utf-8');
            });
        }else if(req.url=='/student'){
            res.writeHead(200,{'Content-Type':'text/html'});
            res.write('<html><body>This is student Page.</body></html>');
            res.end();
        }else if(req.url=='/admin'){
            res.writeHead(200,{'Content-Type':'text/html'});
            res.write('<html><body>This is admin Page.</body></html>');
            res.end();
        }else
            res.end('Invalid Request!');
 
});
 
server.listen(8002);