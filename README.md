# Scraping jobs
Scraping jobs is a script used for helping the user to find the right job.

# Run script
<b> Requirement: </b> <br>
This projects requires to have Python installed on your computer.
If you don't have Python installed check the documentation :
https://docs.python.org/3/using/index.html

### Clone project 
```python
git clone https://github.com/fsetrodinomo/ScrapingJobs
```

### Go to directory
```python
cd ScrapingJobs
```

### Run script
```python
python pyscrape.py
```



# Breakdown code
### How do you get the text from the website ?
There are 2 packages used. Requests and BeautifulSoup. If you want to get the data from a website you need a HTTP requests, simplified:A request which help you to create a request and a response. In this case the content of the website https://realpython.github.io/fake-jobs/.
BeautifulSoup helps to get the content of the website and turn it into HTML. At L6 you can decide from which div tag you want to select your information.

<i>If you would open the page , click on your right mouse button and select 'Inspect' you can see the structure of a website. The divs consist out of smaller divs and the more you click through the divs the more specific the information of the divs get. </i>

```python
L1  import requests
L2  from bs4 import BeautifulSoup

#scraping website html 
L3  URL = "https://realpython.github.io/fake-jobs/"
L4  page = requests.get(URL)

L5  soup = BeautifulSoup(page.content, "html.parser")

L6  results = soup.find(id="ResultsContainer")

L7  print(page.text)
```



### How to change the searching term?
On line 18 there is a text element. This element use the data type String. The String uses a method called "Lambda".
In this case Lambda helps to be more precise. If you remove Lambda the script will only search if the term is available at the title.
Although if you are searching for a job , sometimes it isn't always straight forward at the title but there is a clear demand when you look at the description.
L21 makes sure that to get the right element. 

If you want to search a different term just change the text of Python to your own preffered text for example PHP.
```python
L17 python_jobs = results.find_all(
L18    "h2", string=lambda text:"python" in text.lower()
L19 )
L20 python_job_elements = [
L21        h2_element.parent.parent.parent for h2_element in python_jobs
L22  ]
```


### How do I get the location,company and the job title?
With a for loop you can search through the job_element. By selecting the tag , for example H3, and the class you can print out the different 
divs. If you only print L26 until L29 than the command line will return HTML . Quite readable for someone who can read HTML although without the HTML it's readable for everyone! 
If you don't run L33 the information will be messy.

```python
L26 for job_element in python_job_elements:
L27       title_element = job_element.find("h2", class_="title")
L28       company_element = job_element.find("h3", class_="company")
L29       location_element = job_element.find("p", class_="location")
L30       print(title_element.text.strip())
L31       print(company_element.text.strip())
L32       print(location_element.text.strip())
L33    print()

```





## Future feature
- automated email for newest jos

## Learning resources
<li>LearningSource : https://www.youtube.com/watch?v=s8XjEuplx_U </li>
<li>LearningSource : https://realpython.com/beautiful-soup-web-scraper-python/ </li>

## License

[MIT](https://choosealicense.com/licenses/mit/)












