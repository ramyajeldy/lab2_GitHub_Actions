import requests

def get_github_status():
    response = requests.get("https://api.github.com")
    response1 = requests.get("https://api.github.com/invalid-endpoint")
    return response.status_code, response1.status_code

if __name__ == "__main__":
    status, invalid_status = get_github_status()
    print("GitHub API status code:", status)
    print("Invalid endpoint status code:", invalid_status)
