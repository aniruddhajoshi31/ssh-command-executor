import paramiko
import getpass


def execute_ssh_command(hostname, port, username, command):
    """Execute a command on a remote server via SSH."""
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        client.connect(
            hostname,
            port=port,
            username=username,
            password=getpass.getpass(f"Enter password for {username}@{hostname}: ")
        )

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()

        if output:
            print("Output:\n", output)
        if error:
            print("Error:\n", error)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    hostname = input("Enter hostname or IP address: ")
    port = int(input("Enter port (default 22): ") or 22)
    username = input("Enter username: ")
    command = input("Enter command to execute: ")

    execute_ssh_command(hostname, port, username, command)
