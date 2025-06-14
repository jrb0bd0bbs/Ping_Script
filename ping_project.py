import os
import time
import subprocess

# File path where the results will be stored
file_path = "/home/d/Documents/ping_project.txt"

def ping(host):
    """Ping a host and return the latency in ms"""
    try:
        # Use the 'ping' command on the system (works on Unix-based systems)
        result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # If the ping is successful
        if result.returncode == 0:
            # Extract the time=XXX ms from the output
            output = result.stdout.decode('utf-8')
            latency = output.split('time=')[1].split(' ms')[0]
            return latency
        else:
            return None
    except Exception as e:
        print(f"Error pinging {host}: {e}")
        return None

def log_ping_results():
    """Logs the ping results for google.com and msn.com to a file"""
    with open(file_path, 'a') as file:
        while True:
            google_latency = ping("google.com")
            msn_latency = ping("msn.com")
            
            # Get the current time for the log entry
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            
            # Write the results to the file
            file.write(f"{current_time} - google.com latency: {google_latency if google_latency else 'Timeout'} ms, msn.com latency: {msn_latency if msn_latency else 'Timeout'} ms\n")
            
            # Wait for 1 minute before checking again
            time.sleep(60)

if __name__ == "__main__":
    log_ping_results()
