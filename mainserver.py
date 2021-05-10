import connections
import server_handler
#instance of serveconnections
mysocket=connections.ServerConnection()
#create connections
mysocket.createConnections("",8080)
#listen the connections
mysocket.ListenConnections()

#accept all the connections
myconn,myadd=mysocket.acceptConnections()

server_handler.handleConnection(mysocket)

#---closing the connections
myconn.close()
mysocket.close()