import requests

def main():
    response = requests.get("https://api.github.com")
    print("GitHub API status code:", response.status_code)

if __name__ == "__main__":
    main()
