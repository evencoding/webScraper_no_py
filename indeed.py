import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://kr.indeed.com/jobs?q=python&limit={LIMIT}'

def extract_indeed_pages():  
  result = requests.get(URL)
  soup = BeautifulSoup(result.text , "html.parser")
  pagenation = soup.find("div" , {"class" : "pagination"})
  pages = pagenation.find_all('a')
  spans = []
  for page in pages[:-1]:    
    spans.append( int(page.string) )
  max_page_is =  spans[-1]
  return max_page_is


def extract_indeed_job(last_page):
  jobs = []
  for n in range(last_page):
    result = requests.get( f"{URL}start={n * LIMIT}" )

    soup = BeautifulSoup(result.text , "html.parser")
    results = soup.find_all("a" , {"class" : "tapItem"})

    for result in results:
      title = result.find( "h2" , {"class" : "jobTitle"})
      print(title.find("span" ,title=True ).string)
