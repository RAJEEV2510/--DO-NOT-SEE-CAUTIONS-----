from glob import glob
import os

def upload_files(mysocket):
    print("[+] upload files")
    files=glob("*.*")#list out all files in the directory
   
    for index,filename in enumerate(files):#enumarates functions gives index to every one item present in list
        print("[+]"+" "+str(index)+" "+os.path.basename(filename))
   

    while True:
        try:
            file_index=int(input("[+] Select file"))
            if file_index>=0 and file_index<len(files):
                filename=files[file_index]
                break
        except:
            print("invalid file selected")
    print("[+] selected file name "+filename)      
    print("\n")  
    mysocket.sendData(filename)    
    mysocket.send_file(filename)
          

