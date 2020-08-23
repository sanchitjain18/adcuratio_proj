**INTRODUCTION** <br><br>
The motive of this assignment is to scrap the data from the https://news.ycombinator.com/ website and store the scrapped data into MongoDB maintaining two collections:
  1. URL and Heading of the Blog
  2. URL and Metadata
  
**PLATFORM**
  1. PyCharm: for writing the python code
  2. MongoDB Compass: to check the Database contents
  
**WORKFLOW**
  1. DB Setup: <br>
     -> Created an account in MongoDB.<br>
     -> Created DB cluster using AWS cloud provider in North Virginia region, which will hold the collections.<br>
     -> Selected the Driver(Python 3.8v) and chose the appropriate DB connection string to be used in the application.
  
  2. Virtual Environment Setup: <br>
     -> Created a virtual environment in python for implementing the scrapping code.
        
  3. Install Dependencies:<br>
     -> pip install beautifulsoup4 <br>
     -> pip install requests <br>
     -> pip install urllib3 <br>
     -> pip install pymongo <br>
     All the dependencies can be found in the requirement.txt file
     
  4. Code Implementation:<br>
     -> When the code is executed(test.py), the following data is scrapped from the website and stored into two different collections:<br>
        + **ycombinator_sc_data.url_header** collection contains URL and Heading of the Blog, and <br>
        + **ycombinator_sc_data.url_metadata** collection contains URL and Metadata.
    
