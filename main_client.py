import clientconnection
import clienthandle

if __name__=="__main__":
    my_socket=clientconnection.ClientConnection()
    my_socket.Connect("192.168.0.12", 8080)
    clienthandle.handleConnection(my_socket)
    my_socket.close()
    
