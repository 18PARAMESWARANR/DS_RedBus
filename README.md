# REDBUS PROJECT-Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

PROJECT STATEMENT:
The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, 
analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, 
schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, 
this project can significantly improve operational efficiency and strategic planning in the transportation industry.


Technical Tags:
●	Web Scraping
●	Selenium
●	Streamlit
●	SQL
●	Data Analysis
●	Python (jupyter)
●	Interactive Application

Data Set Explanation:
   The scraped dataset for this project contained detailed information about bus services available on Redbus, the fields are:
   Bustype,Bus RouteName, Bus RouteLink, Price, Seat availability,Departing Time, ReachingTime,Duration 

Approach :
1) Data scrapping using selenium and cleaning:
    First, we installed all the important packages we need like panadas, selenium(keys,web DriverWait,By, expected conditions),time
    for streamlit application-streamlit, MySQLconnector/SQLAlchemy,streamlit-option-menu 
     1) first we start importing all these necessary packages using the pip install command.
     2) we define web driver(chrome diver) to get and open the Red bus URL and maximizing the browser window for better visibility.
     3) Then we write the code for scrapping the data for the corresponding state link we provide, followed by gathering all bus routes,bus routes name ,Route link,
        and all the bus information.
     4) The scrapped data we stored in a CSV file with a state name.
     5) like this we scrapped each 17 state bus details, each data stored corresponding to each state CSV files
     6) The all CSV file content, we put in one CSV file.
     7) The workflow continues by establishing a connection between Python and a MYSQL database.
     8) In MySQL we create one database and in that database, we create one table, and in that table, we insert the CSV file data.
     9) Here we clean the data and our data is ready for filtration, connection is closed between the database and Python.
           
2) streamlit webapplication :(redapp.py)
       1) The process starts with importing Streamlit and other required packages.
       2) Then we configure the web application page according to how we want to build.
       3) we set the connection between MySQL and Python using the specific database we created earlier. 
       4) we write filtration code based on Routename, Bus type, price ,star rating, and Seat availability.
       5) we write code for retrieved data displayed in a table format when the user provides input.
   
How to run streamlit code:
      In your IDE terminal type:**streamlit run redapp.py(your file name like here redapp.py)**
The solution can be applied to various business scenarios including:
●	Travel Aggregators: Providing real-time bus schedules and seat availability for customers.
●	Market Analysis: Analyzing travel patterns and preferences for market research.
●	Customer Service: Enhancing user experience by offering customized travel options based on data insights.
●	Competitor Analysis: Comparing pricing and service levels with competitors.
