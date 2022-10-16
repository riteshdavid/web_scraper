#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import time

print("[]INFO: Getting to python.org/jobs ...")
html_text=requests.get('https://www.python.org/jobs/')
time.sleep(2)



soup=BeautifulSoup(html_text.text,'html.parser')
tags=soup.find('ol',class_='list-recent-jobs list-row-container menu')
company_name=tags.find_all('li')
print("[]INFO: Analyzing Page For Jobs ..." )
time.sleep(2)
for company in company_name:
    companyname=company.find('span',class_="listing-company-name")
    company_loc=company.find('span',class_="listing-location")
    company_jobtype=company.find('span',class_="listing-job-type")
    company_posted=company.find('span',class_="listing-posted")
    company_jobcategory=company.find('span',class_="listing-company-category")
    print(companyname.text.strip())
    print(company_loc.text.strip())
    print(company_jobtype.text.strip())
    print(company_posted.text.strip())
    print(company_jobcategory.text.strip())
    print("\n")
