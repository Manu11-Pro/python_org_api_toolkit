import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.python.org/jobs/")
status_code = response.status_code

if status_code == 200:
    print("\n Status Good for Fetching! \n")
    print(f"\n {"-" * 30} \n")

def get_py_jobs():
    pyorg_url = "https://www.python.org/"

    jobs_pages = ["https://www.python.org/jobs/?page=1", "https://www.python.org/jobs/?page=2"]

    for url in jobs_pages:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        jobs_section = soup.find("ol", class_="list-recent-jobs list-row-container menu")

        if not jobs_section:
            print("Could not find jobs section")

        jobs_items = jobs_section.find_all("li")

        jobs = []

        for item in jobs_items:
            job_company_span = item.find("span", class_= "listing-company-name")
            job_company_span_all_text = list(job_company_span.stripped_strings)

            job_location_span = item.find("span", class_= "listing-location")

            job_type_span = item.find("span", class_= "listing-job-type")

            job_listing_date_span = item.find("span", class_= "listing-posted")

            job_title = item.find("a").text
            job_company = job_company_span_all_text[-1]
            job_partial_link = item.find("a")["href"]
            job_full_link = f"{pyorg_url + job_partial_link}"
            job_location = job_location_span.text.strip()
            job_type_span_all_text = job_type_span.text.strip()
            job_listing_date_span_all_text = job_listing_date_span.text.strip()


            print("\n")
            print(job_title)
            print(job_company)
            print(job_full_link)
            print(job_location)
            print(job_type_span_all_text)
            print(job_listing_date_span_all_text)
            print("\n")
        
print(get_py_jobs())

#         if _ and _:
#             job_title = item.find("a").text
#             job_company = item.find("text").text
#             link = item.find("a")["href"]

#             blogs.append({
#                 "Job Title": job_title,
#                 "Comapany": job_company,
#                 "Link": link,
#             })

#     return blogs[:5]

# news_and_blog_data = get_py_jobs()

# for blogs in news_and_blog_data:
#     print(f"Latest Blogs and News: ")
#     print("\n")
#     print("\n # Python News and Blogs # \n")
#     print(f"TITLE : {blogs["News"]}")
#     print(f"DATE : {blogs["Date"]}")
#     print(f"LINK : {blogs["Link"]}")
#     print("\n")

# print("\n --- End of News and Blogs Feed --- \n")