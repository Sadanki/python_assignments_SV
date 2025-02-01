import os

def generate_cpu_load():
    """
    Generates CPU load by performing intensive computations in a loop.
    """
    pid = os.getpid()
    print(f"CPU Load Process ID: {pid}")
    
    # Write the PID to a file
    with open("cpu_load_pid.txt", "w") as pid_file:
        pid_file.write(str(pid))
    
    while True:
        x = [i**2 for i in range(10000)]

if __name__ == "__main__":
    generate_cpu_load()
