import os
import subprocess
from datetime import datetime 
import re

# Get the current working directory (adjust based on where you want to store files)
current_directory = os.path.dirname(os.path.realpath(__file__))

# Path to your list of explicit sites
explicit_sites_path = os.path.join(current_directory, "explicit-sites.txt")

# Path to the report file
report_file_path = os.path.join(current_directory, "accountability-report.txt")

# Function to read the explicit sites list
def load_explicit_sites():
    explicit_sites = set()
    with open(explicit_sites_path, 'r') as f:
        for line in f:
            explicit_sites.add(line.strip().lower())
    return explicit_sites

# Function to check verdicts output
def check_verdicts():
    explicit_sites = load_explicit_sites()

    # Run the Plucky verdicts command as a subprocess
    process = subprocess.Popen(
        ['pluck', 'verdicts', '-f'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=True  # Important for running shell commands on Windows
    )

    # Continuously read the output
    while True:
        # Read one line at a time from the output
        output = process.stdout.readline()
        if output == "" and process.poll() is not None:
            break
        
        # Check if any explicit site is in the output
        for site in explicit_sites:
            if site in output.lower():
                # If a match is found, log it
                log_explicit_site(output)
                break

# Function to log explicit sites with a timestamp, program, domain, and action
def log_explicit_site(verdict):
    # Get the current time and format it as a readable string
    timestamp = datetime.now().strftime('%Y-%m-%d')

    # Log the result with timestamp and the raw verdict output
    with open(report_file_path, 'a') as report_file:
        report_file.write(f"[{timestamp}] {verdict}")
    
    # Print to console for debugging
    print(f"Logged: [{timestamp}] {verdict}")

if __name__ == "__main__":
    check_verdicts()  # Make sure this function is called to start the process
