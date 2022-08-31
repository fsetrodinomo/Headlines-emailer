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

def extract_news(url):
    print ('Extracting financial times news stories ... ')
    cnt = ''
    cnt +=('<b>Financial Times Top Stories :</b>\n'+'<br>'+'-'*50+'<br>')
   #get content of the url and store in response object
    response = requests.get(url)
    #local object only for extracting news
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i ,tag in enumerate(soup.find_all('div',attrs={'class':'o-teaser__heading','o-teaser__meta':''})):
        cnt += ((str(i+1)+' :: '+tag.text+ "\n" + '<br>') if tag.text!='More' else'')
    return (cnt)

    cnt = extract_news('https://www.ft.com/todaysnewspaper/')
    content += cnt
    content += ('<br>-------<br>')
    content += ('<br><br>End of message')


##Sending email

print ('Composing email ...')

#update email adress
SERVER = 'smtp.gmail.com'
PORT = 587
FROM = "jolieaurelius@gmail.com"
TO = "jolieaurelius@gmail.com"
PASS = "test"

#message body
msg = MIMEMultipart ()

msg['Subject']  = 'Financial times headlines ' + '' +str(now.day) + '-' + str(now.month) + '-' + str(
    now.year) 
msg ['From'] = FROM
msg ['To'] = TO

msg.attach(MIMEText(content,'html'))

print ('Ínitiating server ......')
