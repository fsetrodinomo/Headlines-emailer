#handling http requests
import requests

#webscraping
from bs4 import BeautifulSoup
#package to send the email
import smtplib
#creating email body
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
#system date and time manipulation
import datetime
#create a seperate line with the date time to make sure that it is seperating automated email
now = datetime.datetime.now()

#email content placeholder
#global object
content = ''

def extract_jobs(url) :
    #scraping website html 
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    print(page.text)
    print (results.prettify)
    job_elements = results.find_all("div", class_="card-content")
    python_jobs = results.find_all(
        "h2", string=lambda text:"python" in text.lower())
    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
        ]
    for job_element in python_job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        return (job_element,title_element,company_element,location_element)

#     cnt = extract_jobs('https://realpython.github.io/fake-jobs/')
#     content += cnt
#     content += ('<br>-------<br>')
#     content += ('<br><br>End of message')


# ##Sending email

# print ('Composing email ...')

# #update email adress
# SERVER = 'smtp.office365.com'
# PORT = 587
# FROM = "jolieaurelius@outlook.com"
# TO = "setrodinomof@outlook.com"
# PASS = "Duckduck123"

# #message body
# msg = MIMEMultipart ()

# msg['Subject']  = 'Jobs in python ' + '' +str(now.day) + '-' + str(now.month) + '-' + str(
#     now.year) 
# msg ['From'] = FROM
# msg ['To'] = TO

# msg.attach(MIMEText(content,'html'))

# print ('Ínitiating server ......')

# server = smtplib.SMTP(SERVER, PORT)
# server.set_debuglevel(1)
# server.ehlo()
# server.starttls()
# server.login(FROM, PASS)
# server.sendmail(FROM,TO, msg.as_string())

# print('Email sent ....')

# server.quit()
    



