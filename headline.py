#handling http requests
import requests

#webscraping
from bs4 import BeautifulSoup
# #package to send the email
# import smtplib
# #creating email body
# from email.mime.multipart import  MIMEMultipart
# from email.mime.text import MIMEText
# #system date and time manipulation
# import datetime
# #create a seperate line with the date time to make sure that it is seperating automated email
# now = datetime.datetime.now()

#email content placeholder
#global object
content = ''

def extract_news(url):
    print ('New jobs... ')
    cnt = ''
    cnt +=('<b>Our newest jobs :</b>\n'+'<br>'+'-'*50+'<br>')
   #get content of the url and store in response object
   
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

    #local object only for extracting news
content = page.content
   #scraping website html 

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")

print(page.text)
print (results.prettify)

job_elements = results.find_all("div", class_="card-content")

python_jobs = results.find_all(
    "h2", string=lambda text:"python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]


for job_element in python_job_elements : 
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()



# ##Sending email

# print ('Composing email ...')

# #update email adress
# SERVER = 'smtp.office365.com'
# PORT = 587
# FROM = ""
# TO = ""
# PASS = ""

# #message body
# msg = MIMEMultipart ()

# msg['Subject']  = 'Financial times headlines ' + '' +str(now.day) + '-' + str(now.month) + '-' + str(
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
