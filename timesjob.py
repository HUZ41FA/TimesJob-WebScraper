from datetime import datetime
from bs4 import BeautifulSoup
import requests
from apscheduler.schedulers.blocking import BlockingScheduler

def times_job_scraping():
    get_request =  requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')

    soup = BeautifulSoup(get_request.text, 'lxml')

    number_of_jobs = soup.find('span', class_ ='totolResultCountsId')
    jobs = soup.find_all('li', class_= "clearfix job-bx wht-shd-bx")

    for job in jobs:
        posted = job.find_all('span')[len(job.find_all('span'))-1].text
        if posted == "Posted few days ago":
            title = job.header.h2.a.text.strip()
            company= job.header.h3.text.strip().split("(More Jobs)")
            for detail in job.find_all('ul', class_ = "top-jd-dtl clearfix"):
                _ ,experience = detail.find('li').text.split('card_travel')
                city = detail.find('span').text
            print(f"Title: {title}")
            print(f"Company: {company[0]}")
            print(f"Experience Required: {experience}")
            print(f"City: {city}")
            print("---------------------------------------------------------")
    print(datetime.now())


        
scheduler = BlockingScheduler()
scheduler.add_job(times_job_scraping, 'interval', minutes=1)
scheduler.start()