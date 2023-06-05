// server.js

var WebSocketServer = require("websocket").server;
var http = require("http");

var server = http.createServer(function(request, response) {
    response.writeHead(404);
    response.end();
});

server.listen(8080, function() {
    console.log("Server listening on port 8080.");
});

var wsServer = new WebSocketServer({
    httpServer: server
});

var clients = [];

wsServer.on("request", function(request) {
    var connection = request.accept(null, request.origin);
    clients.push(connection);

    connection.on("message", function(message) {
        var content = message.utf8Data;
        for (var i = 0; i < clients.length; i++) {
            clients[i].sendUTF(content);
        }
    });

    connection.on("close", function(connection) {
        var index = clients.indexOf(connection);
        clients.splice(index, 1);
    });
});
