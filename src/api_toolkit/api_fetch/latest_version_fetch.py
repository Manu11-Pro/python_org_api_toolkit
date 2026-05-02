import requests
from bs4 import BeautifulSoup

def get_py_latest_version():
    url = "https://www.python.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    release_link = soup.find("a", href=lambda href: href and href.startswith("/downloads/release/python-"))

    if release_link:
        return release_link.text.replace("Python", "").strip()
    
    return "Version Not Found!"

if __name__ == "__main__":
    print(f"Latest release: {get_py_latest_version()}")
    print(f"\n {"-" * 30} \n")