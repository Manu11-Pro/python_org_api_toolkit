import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.python.org/")
print(f"Status: {response.status_code}")

def get_py_news():
    url = "https://www.python.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    latest_news_section = soup.find("div", class_="medium-widget blog-widget")

    if not latest_news_section:
        print("Could not find latest news section")

    latest_news_items = latest_news_section.find_all("li")

    blogs = []

    for item in latest_news_items:
        text_link_tag = item.find("a").text
        date_tag = item.find("time").text
        

        if text_link_tag and date_tag:
            news = item.find("a").text
            date = item.find("time").text
            link = item.find("a")["href"]

            blogs.append({
                "News": news,
                "Date": date,
                "Link": link,
            })

    return blogs[:5]

news_and_blog_data = get_py_news()

for blogs in news_and_blog_data:
    print(f"Latest Blogs and News: ")
    print("\n")
    print("\n # Python News and Blogs # \n")
    print(f"TITLE : {blogs["News"]}")
    print(f"DATE : {blogs["Date"]}")
    print(f"LINK : {blogs["Link"]}")
    print("\n")

print("\n --- End of News and Blogs Feed --- \n")
