from requests import get
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?search_uuid=&term="
  results = []

  response = get(f"{base_url}{keyword}")
  
  if response.status_code != 200:
    print("Can't request website")
  else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']
        company, kind, region = anchor.find_all('span', class_="company")
        
        job_data = {
            'position': kind.string.replace(",", " "),
            'company': company.string.replace(",", " "),
            'location': region.string.replace(",", " "),
            'link': f"https://weworkremotely.com{link}",
        }
        results.append(job_data)
  return results
