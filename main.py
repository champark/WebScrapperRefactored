from extractors.wwr import extract_wwr_jobs
from extractors.getwork import extract_getwork
from file import save_to_fle

keyword = input("What do you want to search for?")

wwr_jobs = extract_wwr_jobs(keyword)
getwork_jobs = extract_getwork(keyword)
jobs = wwr_jobs + getwork_jobs

save_to_fle(keyword, jobs)
