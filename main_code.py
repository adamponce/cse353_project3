"""
This document is the file that contains all of the functions in python necessary
to complete project 3.
"""

import socket

"""
Here are all the definitions needed for the Socket
"""
SIZE = 1024
FORMAT = "utf-8"
PORT = 12344


"""
This will create nodes in which every node will open and read an input file
which contains data that should send across the network to other nodes. Every
node creates an output file which has all the data it was sent by other nodes.
The nodes will send data via a local switch.
"""
def nodes():
    """
    Creating the socket and connecting
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), PORT))

    """
    Opening and reading file
    """
    file = open('confA.txt', 'r')
    count = 0

    """
    this while loop will read through the entire file and send the data line by line
    to node B, it will then have an if statement and when the file is completely
    read it will then a 'stop' to node B and then it will wait for confirmation
    that the data was received. It will then close socket and exit.
    """
    while True:
        count += 1

        print(count)

        line = file.readline()

        if not line:
            print("hit the not line")
            s.send("stop".encode(FORMAT))
            break

        s.send(line.encode())

    msg = s.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """
    Closes file and socket then exits server
    """
    file.close()

    s.close()

    """
    This creates the socket object and binds the socket
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")

    s.bind((socket.gethostname(), port))
    print("socket binded to %s" %(port))

    """
    put the socket into listening mode
    """
    s.listen(5)

    """
    This while loop recieves the data from node A and prints the data line by line
    to the terminal. it will then break when it recieves 'stop' from node A and Then
    it will close the socket.
    """
    while True:
        #Node B has accepted connection from node A
        clientsocket, address = s.accept()

        #receiving data from node A.
        while True:
            data = clientsocket.recv(SIZE).decode(FORMAT)
            print("Node B received: " + data)
            #stops the intake from node A
            if data == "stop":
                break

        clientsocket.send("File data recieved".encode(FORMAT))

        clientsocket.close()



    """
    This section sends data to node C
    """
    #s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s2.connect((socket.gethostname(), port2))

    """
    Opening and reading file
    """
    file = open('confB.txt', 'r')
    count2 = 0


    """
    this while loop will read through the entire file and send the data line by line
    to node B, it will then have an if statement and when the file is completely
    read it will then a 'stop' to node B and then it will wait for confirmation
    that the data was received. It will then close socket and exit.
    """
    while True:
        count2 += 1

        print(count2)

        line = file.readline()

        if not line:
            print("hit the not line")
            s.send("stop".encode(FORMAT))
            break

        s.send(line.encode())

    msg = s.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")


    file.close()

    s2.close()



"""
Same as the css_switch_class however, it will start traffic forwarding at the
moment the main CCS switch fails.
"""
def css_shadow_switch():
    """
    I am struggling with what to put in these.
    """
    ClientSocket = socket.socket()
    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    Response = ClientSocket.recv(2048)
    while True:
        Input = input('Your message: ')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(2048)
        print(Response.decode('utf-8'))
    ClientSocket.close()

    return 0


"""
This function is a switch class that is more powerful and faster than the other
switches in order to handle aggregated traffic. The CSS will first flood frames
to the underlying CAS instead of the end user and will then forward the traffic
based on the network number. Also takes care of forwarding firewalling rules.
It will read the firewall rules from a file.
"""
def css_switch_class():
    global firewall
    """
    I am struggling with what to put in these.
    """
    ClientSocket = socket.socket()
    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    Response = ClientSocket.recv(2048)
    while True:
        Input = input('Your message: ')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(2048)
        print(Response.decode('utf-8'))
    ClientSocket.close()

    return 0


"""
The switch in this function will allow multiple connections and will use frame
flooding and source address matching to determine where to send frames. The
switches in this function connect to the core switch in order to forward global
traffic. Function is capable of firewalling and bridging functionalities.
"""
def cas_switch_class():
    """
    I am struggling with what to put in these.
    """
    ClientSocket = socket.socket()
    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    Response = ClientSocket.recv(2048)
    while True:
        Input = input('Your message: ')
        ClientSocket.send(str.encode(Input))
        Response = ClientSocket.recv(2048)
        print(Response.decode('utf-8'))
    ClientSocket.close()

    return 0


"""
This class will instantiate the nodes and switches as well as a single core
switch. This class will wait until all nodes are done sending data before it
shuts down all individual nodes. Following this it will shut down the switch and
hub and then will exit cleanly
"""
def main():
    cas_switch_class()
    css_switch_class()
    css_shadow_switch()
    nodes()

firewall
main()
