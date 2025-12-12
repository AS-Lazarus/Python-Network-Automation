# Network Security Tool: Simple Log Analyzer
# Author: AS-Lazarus
# Purpose: Scans server logs for suspicious 'Failed Login' attempts.

# 1. Simulate a list of server logs (normally this would read a file)

server_logs = [
    "2025-01-10 08:00:01 - User: admin - Status: SUCCESS",
    "2025-01-10 08:01:23 - User: guest - Status: SUCCESS",
    "2025-01-10 08:02:11 - User: admin - Status: FAILED LOGIN",  # Suspicious!
    "2025-01-10 08:04:05 - User: root - Status: FAILED LOGIN",   # Suspicious!
    "2025-01-10 08:05:00 - User: staff - Status: SUCCESS"
]

print("*** STARTING LOG SCAN ***")

# 2. Loop through each line in the logs

for log_line in server_logs:
    
    # 3. Check if the specific keyword exists in the line
    if "FAILED LOGIN" in log_line:
        print(f"⚠️ ALERT: Suspicious Activity Detected! -> {log_line}")
    else:
        # If it's normal, just ignore (or print 'OK')
        print(f"OK: {log_line}")

print("*** SCAN COMPLETE ***")
