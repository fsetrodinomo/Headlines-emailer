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
content = ''

def extract_news(url):
    print ('Extracting financial times news stories ... ')
    cnt = ''
    cnt +=('<b>Financial Times Top Stories :</b>\n'+'<br>'+'-'*50+'<br>')
   #get content of the url 
    response = requests.get(url)