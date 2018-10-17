# Krishna Agarwal 👨‍🎓

Given a medical symptom, list down the possible medical conditions/diagnosis and for
any given diagnosis suggest various treatments. 💊

A Demo Video of the whole project running can be found here. 🎥 \
[Demo Video - Health Checker.mp4](https://github.com/KriAga/Health-Checker/blob/master/Demo%20Video%20-%20Health%20Checker.mp4?raw=true)

### Prerequisites

Python3.6 🐍 \
PyCharm \
Mysql 8.0.11.0 \
Selenium driver 


### Dependencies

beautifulsoup4 4.6.3 \
chardest 3.0.4\
click 7.0\
flask 1.0.2 \
get 1.0.3\
pip 18.1\
post 1.0.2\
public 1.0.3\
query-string 1.0.2\
request 1.0.2\
requests 2.19.1\
scraper 0.1.0\
selenium 3.14.1\
urllib3 1.23 


## Getting Started 👍

You need to start MySQL server.
Open the project in Pycharm and run the [web-app\app.py](https://github.com/KriAga/Health-Checker/blob/master/HealthChecker/web-app/app.py) file. It will run the flask server. Open the link provided => ```http://127.0.0.1:5000/```


## Deployment
💥*Edit:* 💥 ➕ \
Added a deployable Docker Image 🐋 for the project. Having issues with API 3 and it is still not working, all other APIs are fully functional (1, 2, 4 and 5).

For API 3, I think I'll have to run a seperate docker that will run the browser and then get the data. I am not familiar about integrating browser as of now so not able to implement this portion. We can run the API 3 locally for now. 😶


```
sudo docker run --name mysql -e MYSQL_ROOT_PASSWORD=password -d mysql:5.5

sudo docker run -itd -p 5000:5000 --name app --link mysql:mysql -d kriaga/healthapi:latest
```

## Running the tests
API 1 - http://127.0.0.1:5000/api/one/ \
API 2 - http://127.0.0.1:5000/api/two/ \
API 3 - http://127.0.0.1:5000/api/three/ \
API 4 - http://127.0.0.1:5000/api/four/ \
API 5 - http://127.0.0.1:5000/api/five/ 

## Description

**API 1 - To fetch the symptoms**

Using the Apimedic API fetching all the symptoms.\
The [fetchSymptoms.py](https://github.com/KriAga/Health-Checker/blob/master/HealthChecker/fetchSymptoms.py) file is the base on which the other files are also made so this particular API was of much importance. 🌟 \
The code makes a file Symptoms.txt 📄 that stores all the symptoms in descending order of their lengths. This sorted data is also stored in a list. 


**API 2 - To fetch the medical conditions**

Again using the Apimedic API fetching all the medical conditions using the symptom ID and providing the year of birth and the gender for better results.
We can also fetch the medical condition with multiple symptoms by providing more than one symptom IDs. 😇

**API 3 - To fetch the treatment of a medical condition**

This API was to be made by scraping the web. I explored some online available websites (https://www.nhsinform.scot/) for this purpose but wasn't able to find any particular website with all the required data. If any website had the data it was neither easily scrapable nor asured that data would be available. 😩

I mailed my query to [Ravi Maink](mailto:ravi.manik@innovaccer.com) 👨‍💻 and he explained me the problem statement. He asked me to simple Google search 🔍 for the medical condition and get the treatment data. I understood where the resultant data was (Right hand side data of Google Search) but on further research found that Google had made that dynamic data unscrappable directly by libraries like BeautifulSoup and Scrapy. 😠 😿

Here:
https://stackoverflow.com/a/14431651

I tried the alternate solutions provided by the stackoverflow answer only to find out that either they are too dificult to implement or are shut-down. 😟 🛌 💤 So, I thought of an another way round by headless Chrome Selenium Automation. 😵 In layman's terms I am running a selenium chrome driver by the python script in the backend, searching for the medical condition on https://www.google.com/ and then scraping the right hand side dynamically generated data and storing it in a dictionary. 😁 😉 😎

The problem statement also asked to store the once searched disease into the database 📁 , for this purpose I am using mysql server to store the data on my system locally. In my code the database would be created automatically and next time when the desease is searched it is first fetched from the database and in case it is unavaliable it then runs the selenium browser.

The fact that we are making a google search gives us an advantage of bypassing the typing error. I store the disease and the treatment in the database only after getting the right searched data from the browser. 🙌

**API 4 - Finding nearest doctors based on given location**

👨‍⚕ There were many methods to get this thing done. We can simply make a google search for ```doctors near me``` and get the map and show it on the browser but I dont think that it would be the right solution to the problem. I wanted to display the exact address of the doctor near me with his/her profile.

I searched for the available APIs online and found three APIs. 
*   [BetterDoctor API](https://developer.betterdoctor.com/)
*   [Practo](https://developers.practo.com/)
*   [National Hospital Directory with Geo Code and additional parameters](https://data.gov.in/catalog/hospital-directory-national-health-portal)

The Practo API was active for Indian locations 🇮🇳 (I tested the API on its portal) but is not available now as it is under revamp.

The National Hospital Directory was available as an API but was for Indian locations only. 🇮🇳

As Innovaccer is a company that has most of its bussiness in United States of Ameria 🇺🇸 , it would have been of not much use to implement and India only API.

And hence the 🎁BetterDoctor API🎁 , it's only con that it is not available outside USA otherwise it is the best website for our problem as there are a number of APIs that can be used with a lot of parameters. I have used the basic ```Doctor search``` API which takes in the latitude, longitude, the order in which the result should be displayed (for example ascending order of the distance or name or rating), the maximum number of results and the size of the area in which the API needs to search; as input and returns a perfect JSON with a huge number of parameters.

I fetched data in the order of the closest doctors.

For future work on this project one can easily make a whole profile page of the doctors with their Education, Bio, Phone Number, Claims, License Number etc. It is also possible to search for doctors who have a speciality in a particular field. It would be a great feature. 🛩

**API 5 - Extract Symptom from sentence and show the Medical Condition**

Taking a sentence as input that has one symptom. Extracting this symptom from the sentence and using it to fetch for the appropriate medical condition.

I tried using nltk for this. I removed stopwords from the sentence but still words like ```I``` were left in the resultant text. I could have changed the stopwords.txt file of the nltk library but I wanted to find a much simpler approach. So, I tried to extract the Keywords from the sentence and it was successfull for words like ```headache``` but failed miserable for ```back pain```, ```brain cancer``` etc as they had two words and each being a keyword in itself. This could have been rectified by tweaking the library 😒 instead I did a better approach of looking for each symptom in the sentence and as soon as a symptom matched I fetched for its symptom ID from the dictionary that I made for API 1 and used it further to find the medical condition.

Reason why I had sorted the symptoms data in API 1 in the order of the largest symptom first was to help get the best result in API 5 here. 🤔

```
Example: 
    sentence => "I am having abdominal and back pain"
    symptomsName => ["fever", "headache", "back pain", "abdominal and back pain"]

    Now, if we take each symptom and search for it in sentence we will get the result as "back pain" whereas the actual result should have been "abdominal and back pain".

    Therefore I sorted the symptomsName in descending order so as to have symptomsName as:
    ["abdominal and back pain", "back pain", "headache", "fever"]

    Now, the result would be "abdominal and back pain".
    Which is the right result.
```

😎

## Future Work ✈️

We can ~~deploy the whole project on Docker~~ and implement more APIs from BetterDoctor API. We can also make a direct page to get the treatments based on the sentences of the user stating his/her symptoms of a medical disease.

## Author ✍️

* [**Krishna Agarwal**](https://github.com/Kriaga)

## License 📄

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details