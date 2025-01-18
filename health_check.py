import yaml
import requests
import time
from urllib.parse import urlparse

def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def check_health(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET')
    headers = endpoint.get('headers', {})
    body = endpoint.get('body')

    try:
        if method == 'GET':
            response = requests.get(url, headers=headers, timeout=5)
        elif method == 'POST':
            response = requests.post(url, headers=headers, json=body, timeout=5)
        else:
            print(f"Unsupported HTTP method: {method}")
            return False, 0
        latency = response.elapsed.total_seconds() * 1000
        is_up = response.status_code in range(200, 300) and latency < 500
        return is_up, latency
    except requests.RequestException:
        return False, 0

def log_availability(domain_availability):
    for domain, (up_count, total_count) in domain_availability.items():
        availability = round((up_count / total_count) * 100) if total_count > 0 else 0
        print(f"{domain} has {availability}% availability percentage")

def monitor_endpoints(config_file):
    config = load_config(config_file)
    domain_availability = {}

    while True:
        for endpoint in config:
            domain = urlparse(endpoint['url']).netloc
            if domain not in domain_availability:
                domain_availability[domain] = [0, 0]  # [UP count, Total count]

            is_up, latency = check_health(endpoint)
            domain_availability[domain][1] += 1
            if is_up:
                domain_availability[domain][0] += 1

        log_availability(domain_availability)
        time.sleep(15)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python health_check.py <path_to_config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    monitor_endpoints(config_file)
