import psutil
import time

def monitor_cpu_process(pid, threshold=80):  # Lowered threshold for testing
    """
    Continuously monitors the CPU usage of a specific process.
    If the CPU usage of the process exceeds the predefined threshold, an alert message is displayed.

    Args:
        pid (int): Process ID of the target process.
        threshold (int): The CPU usage percentage that triggers an alert. Default is 80.
    """
    print(f"Monitoring CPU usage of process with PID: {pid}")

    try:
        process = psutil.Process(pid)
        
        while True:
            # Get the CPU usage of the specific process as a percentage
            cpu_usage = process.cpu_percent(interval=1) / psutil.cpu_count()
            print(f"CPU usage of process {pid}: {cpu_usage}%")  # Debugging line

            # Check if the CPU usage exceeds the predefined threshold
            if cpu_usage > threshold:
                print(f"Alert! CPU usage of process {pid} exceeds threshold: {cpu_usage}%")
            
            # Delay to prevent high CPU utilization due to continuous loop
            time.sleep(1)
    
    except psutil.NoSuchProcess:
        print(f"No process found with PID: {pid}")
    
    except KeyboardInterrupt:
        # Handle user interruption (Ctrl+C)
        print("\nMonitoring interrupted by user.")
    
    except Exception as e:
        # Handle other exceptions
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        # Read the PID from the file
        with open("cpu_load_pid.txt", "r") as pid_file:
            target_pid = int(pid_file.read().strip())
        
        monitor_cpu_process(target_pid)
    except FileNotFoundError:
        print("PID file not found. Ensure that cpu_load.py is running and has created the PID file.")
    except ValueError:
        print("Invalid PID value. Ensure the PID file contains a valid integer.")
