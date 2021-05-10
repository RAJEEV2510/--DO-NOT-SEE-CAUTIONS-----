def download_file(my_socket):
    filename=my_socket.recv_data()
    my_socket.receive_file(filename)