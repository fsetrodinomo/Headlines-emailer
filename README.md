# Scraping jobs
Scraping jobs is a script used for helping the user to find the right job.

# Installation
<b> Requirement: </b> <br>
This projects requires to have Python installed on your computer.
If you don't have Python installed check the documentation :
https://docs.python.org/3/using/index.html
```bash
git clone https://github.com/fsetrodinomo/ScrapingJobs
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

If you want to search a different term just change the text of Python to your own preffered text for example PHP.
```python
L17 python_jobs = results.find_all(
L18    "h2", string=lambda text:"python" in text.lower()
L19 )
```





## Future feature
- automated email for newest jos

## Learning resources
<li>LearningSource : https://www.youtube.com/watch?v=s8XjEuplx_U </li>
<li>LearningSource : https://realpython.com/beautiful-soup-web-scraper-python/ </li>

## License

[MIT](https://choosealicense.com/licenses/mit/)












