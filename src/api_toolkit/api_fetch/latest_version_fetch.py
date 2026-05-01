import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.python.org/")
print(f"Status: {response.status_code}")

def get_py_latest_version():
    url = "https://www.python.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    release_link = soup.find("a", href=lambda href: href and href.startswith("/downloads/release/python-"))

    if release_link:
        return release_link.text.replace("Python", "").strip()
    
    return "Version Not Found!"

print(f"Latest release: {get_py_latest_version()}")