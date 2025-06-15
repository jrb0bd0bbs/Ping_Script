import time
import subprocess
from datetime import datetime

# Target hosts
hosts = ['google.com', 'msn.com']

# Output file path
log_file = '/home/d/Documents/ping_project.txt'

def ping(host):
    try:
        # Ping once and wait max 2 seconds
        output = subprocess.run(['ping', '-c', '1', '-W', '2', host],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        if output.returncode == 0:
            return f"SUCCESS: {host} responded"
        else:
            return f"FAILURE: {host} did not respond"
    except Exception as e:
        return f"ERROR: Exception occurred while pinging {host} - {e}"

def log_result(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    full_message = f"[{timestamp}] {message}\n"
    with open(log_file, 'a') as file:
        file.write(full_message)

if __name__ == "__main__":
    while True:
        for host in hosts:
            result = ping(host)
            log_result(result)
        time.sleep(60)  # Wait 1 minute before next round
