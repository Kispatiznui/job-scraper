import logging
import json
from scraper.fetcher import fetch_jobs
from scraper.parser import parse_jobs
from scraper.storage import save_jobs
from scraper.filters import filter_jobs

URL = "https://realpython.github.io/fake-jobs”

def setup_logging():
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def load_config():
    with open("config.json") as f:
        return json.load(f)

def main():
    setup_logging()
    config = load_config()

    logging.info("Starting job scraping process")

    html = fetch_jobs(URL)
    jobs = parse_jobs(html)

    logging.info(f"Jobs found: {len(jobs)}")

    filtered_jobs = filter_jobs(jobs, config)

    logging.info(f"Jobs after filtering: {len(filtered_jobs)}")

    save_jobs(filtered_jobs)

    print("✅ Jobs saved successfully")

if __name__ == "__main__":
    main()

