# Site Health Monitor

## Overview
This program monitors the health of HTTP endpoints and logs availability percentages.

## Requirements
- Python 3.8+
- `requests` and `PyYAML` libraries

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fetch_health_check.git
   cd fetch_health_check
##  Set Up a Virtual Environment
2. Create and activate a Python virtual environment to avoid conflicts with system packages:
    python3 -m venv venv
    source venv/bin/activate--- FOR WINDOWS
## Install Dependencies
3. Install the required Python libraries:
   pip install -r requirements.txt
## Configuration File Setup
4. Create a file named config.yaml in the project directory:
   nano config.yaml
## Create the Python Script
5.  touch health_check.py
   nano health_check.py
## Usage Instructions
6. Run the script with the path to the configuration file as an argument:
   python health_check.py config.yaml
## Monitor the Output
7.The program logs cumulative availability percentages for each domain every 15 seconds. Example:
  fetch.com has 33% availability percentage
  www.fetchrewards.com has 100% availability percentage
  fetch.com has 67% availability percentage
  www.fetchrewards.com has 50% availability percentage
## Stop the program
   CTRL+C
