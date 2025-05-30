from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import scrape_eventbrite
from datetime import datetime

def job():
    print(f"[{datetime.now()}] Running scheduled scrape...")
    scrape_eventbrite()
    print(f"[{datetime.now()}] Scraping complete.")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'interval', hours=6)
    print("Starting scheduler. Scraping will run every 6 hours.")
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Scheduler stopped.")
