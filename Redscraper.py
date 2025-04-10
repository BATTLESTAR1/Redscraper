import requests
from bs4 import BeautifulSoup

#website
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL) #getting the website from the internet

#using beautiful soup
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer") #storing the gotten page as results

#creating a banner
art = '''
🇼​​🇪​​🇱​​🇨​​🇴​​🇲​​🇪​​ 🇹​🇴​​ 🇷​​🇪​​🇩​​🇸​​🇨​​🇷​​🇦​​🇵​​🇪​​🇷​​​​​'''
print(art)
print("\n")

print("A​v​a​i​l​a​b​l​e J​o​b​🇸")
print("\n")

#filtering designer_jobs, and link
designer_jobs = results.find_all(
    "h2", string=lambda  text: "designer" in text.lower()
)
designer_job_cards = [
    h2_element.parent.parent.parent for h2_element in designer_jobs
]
#filtering engineer jobs, and link
engineer_jobs = results.find_all(
    "h2", string=lambda text: "engineer" in text.lower()
)
engineer_job_cards = [
    h2_element.parent.parent.parent for h2_element in engineer_jobs
]
#filtering Scientist jobs, and link
scientist_jobs = results.find_all(
    "h2", string=lambda text: "scientist" in text.lower()
)

scientist_job_cards = [
    h2_element.parent.parent.parent for h2_element in scientist_jobs
]
#filtering jobs with officer keywords, and link
officer_jobs = results.find_all(
    "h2", string=lambda  text: "officer" in text.lower()
)

officer_job_cards = [
    h2_element.parent.parent.parent for h2_element in officer_jobs
]
#filtering jobs with python keywords, and link
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_jobs_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

#this is where you write the code to display the filtered results
#just write the ""_job_cards to select the specific filter
for job_card in officer_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    link_url = job_card.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")