from extractors.wwr import extract_wwr_jobs
from extractors.getwork import extract_getwork


keyword = input("What do you want to search for?")

wwr_jobs = extract_wwr_jobs(keyword)
getwork_jobs = extract_getwork(keyword)

#print(f"wwr_jobs : {wwr_jobs}")
#print(f"getwork_jobs : {getwork_jobs}")

jobs = wwr_jobs + getwork_jobs

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")
for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")
file.close()
