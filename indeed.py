import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"
LAST_URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}&start=9999"

def extract_indeed_pages():
  result = requests.get(LAST_URL)

  soup = BeautifulSoup(result.text, "html.parser")

  pagination = soup.find("div", {"class":"pagination"})

  links = pagination.find_all("a")
  pages = []

  for link in links[1:]:
      pages.append(int(link.string))

  max_page = pages[-1]
  return max_page

def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    result = requests.get(f"{URL}&start={page*LIMIT}")
    print(result.status_code)
  return jobs