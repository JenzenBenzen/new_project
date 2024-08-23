import requests

def main():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("Successfully reached Github API!")
    else:
        print("Failed to reach Github API.")

if __name__ == "__main__":
    main()
