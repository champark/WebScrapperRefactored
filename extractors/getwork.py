from requests import get
from bs4 import BeautifulSoup

def get_page_count(keyword):
  base_url = "https://getwork.com/search/results?keyword="
  #results = []

  response = get(f"{base_url}{keyword}")

  if response.status_code != 200:
    print("Can't request getwork!")
    return 0
  else:
    soup = BeautifulSoup(response.text, "html.parser")
    pagination = soup.find("ul", class_="job-listing-pagination no-margin")
    pages = pagination.find_all("li")
    if pages == None:
      return 1
    elif len(pages) >= 7:
      return 5
    else:
      return len(pages) - 2

def extract_getwork(keyword):
  base_url = "https://getwork.com/search/results?keyword="
  results = []

  pages = get_page_count(keyword)

  for page in range(pages):
    response = get(f"{base_url}{keyword}&pageNum={page+1}")
    if response.status_code != 200:
      print("Can't request getwork!")
    else:
      soup = BeautifulSoup(response.text, "html.parser")
      jobs = soup.find_all('div', class_="job-listing-clickable")
      for job in jobs:
        position = job.find('h4', class_="search-result-link").string
        company = job.find_all('span', class_='semi-bold')[0].string
        anchor = job['data-job-url']
        location = job.find_all('span', class_='semi-bold')[1].string
        
        job_data = {
            'position': position.replace(",", " "),
            'company': company.replace(",", " "),
            'location': location.replace(",", " "),
            'link': f"https://getwork.com{anchor}"
        }
        results.append(job_data)
  return results
