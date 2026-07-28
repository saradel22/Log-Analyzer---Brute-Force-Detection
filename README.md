# Log-Analyzer---Brute-Force-Detection
A simple Python script that parses authentication log files and flags IP addresses with repeated failed login attempts — a common indicator of brute-force attacks.

How it works
Reads a log file line by line
Looks for lines containing failed login attempts
Extracts the source IP address from each line
Counts how many failed attempts came from each IP
Flags any IP that crosses a configurable threshold (default: 5 attempts)
Usage
bash
python3 log_analyzer.py

By default it analyzes sample_auth.log. To analyze your own log file, change the LOG_FILE variable at the top of log_analyzer.py.

Example Output
===== LOG ANALYSIS REPORT =====

[OK]     192.168.1.5  ->  3 failed attempts
[ALERT]  10.0.0.9     ->  6 failed attempts  (possible brute-force attack)
[OK]     172.16.0.3   ->  1 failed attempts
Why I built this

I use Splunk for SIEM-based log analysis, and wanted to understand how basic log parsing and threat detection logic works at the code level. This script mirrors the core idea behind brute-force detection rules used in real SIEM platforms, built from scratch in Python.

Possible improvements
Support for multiple log formats (Windows Event Logs, Apache/Nginx logs)
Export results to CSV or JSON
Add a time window (e.g., 5 failed attempts within 60 seconds)
Send an alert email or Slack message when a threshold is crossed
Tech used

Python 3 (standard library only — no external dependencies)
