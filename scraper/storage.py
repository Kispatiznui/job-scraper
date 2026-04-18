import csv
import os

def save_jobs(jobs, filename="data/jobs.csv"):
    os.makedirs("data", exist_ok=True)

    existing_links = set()

    if os.path.exists(filename):
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_links = {row["link"] for row in reader}

    with open(filename, "a", newline="", encoding="utf-8") as f:
        fieldnames = ["title", "company", "link"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if os.path.getsize(filename) == 0:
            writer.writeheader()

        new_count = 0

        for job in jobs:
            if job["link"] not in existing_links:
                writer.writerow(job)
                new_count += 1

    return new_count

