import requests
from bs4 import BeautifulSoup

def get_py_jobs():
    pyorg_url = "https://www.python.org/"

    jobs_pages = ["https://www.python.org/jobs/?page=1", "https://www.python.org/jobs/?page=2"]

    all_jobs = []

    for url in jobs_pages:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        jobs_section = soup.find("ol", class_="list-recent-jobs list-row-container menu")

        if not jobs_section:
            print("Could not find jobs section")

        jobs_items = jobs_section.find_all("li")

        for item in jobs_items:
            job_company_span = item.find("span", class_= "listing-company-name")
            job_company_span_all_text = list(job_company_span.stripped_strings)

            job_location_span = item.find("span", class_= "listing-location")

            job_type_span = item.find("span", class_= "listing-job-type")

            job_listing_publish_date_span = item.find("span", class_= "listing-posted")

            job_category_span = item.find("span", class_= "listing-company-category")

            job_title = item.find("a").text
            job_company = job_company_span_all_text[-1]
            job_partial_link = item.find("a")["href"]
            job_full_link = f"{pyorg_url + job_partial_link}"
            job_location = job_location_span.text.strip()
            job_type_span_all_text = job_type_span.text.strip()
            job_listing_publish_date_span_all_text = job_listing_publish_date_span.text.strip()
            job_category_span_all_text = job_category_span.text.strip()

            all_jobs.append({
                "Job Title": job_title,
                "Job Company": job_company,
                "Job Link": job_full_link,
                "Job Location": job_location,
                "Job Type": job_type_span_all_text,
                "Job Listing Publish Date": job_listing_publish_date_span_all_text,
                "Job Category": job_category_span_all_text
            })

    return all_jobs

if __name__ == "__main__":
    all_jobs_data = get_py_jobs()

    print(f"Python Jobs: ")
    print("\n # Python Jobs # \n")

    for jobs in all_jobs_data:
        print(f"JOB TITLE : {jobs["Job Title"]}")
        print(f"COMPANY : {jobs["Job Company"]}")
        print(f"JOB LINK : {jobs["Job Link"]}")
        print(f"JOB LOCATION : {jobs["Job Location"]}")
        print(f"JOB TYPE : {jobs["Job Type"]}")
        print(f"JOB LISTING PUBLISH DATE : {jobs["Job Listing Publish Date"]}")
        print(f"JOB CATEGORY : {jobs["Job Category"]}")
        print("\n")

    print("\n --- End of Python Jobs Feed --- \n")