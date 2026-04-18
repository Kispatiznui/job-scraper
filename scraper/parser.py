from bs4 import BeautifulSoup

def parse_jobs(html):
    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    job_elements = soup.find_all("div", class_="card-content")

    for job in job_elements:
        try:
            title = job.find("h2", class_="title").text.strip()
            company = job.find("h3", class_="company").text.strip()
            link = job.find("a")["href"]

            jobs.append({
                "title": title,
                "company": company,
                "link": link
            })
        except:
            continue

    return jobs

