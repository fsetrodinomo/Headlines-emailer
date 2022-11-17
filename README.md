# Scraping jobs
Scraping jobs is a script which use the fake job website from Python.
T

<b>!NOTE </b> <br>
This projects requires to have Python installed on your computer.
If you don't have Python installed check the documentation :
https://docs.python.org/3/using/index.html


# Installation
```bash
git clone https://github.com/fsetrodinomo/ScrapingJobs
```

# Usage
### How to change the searching term?
On line 18 there is a text element.
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












