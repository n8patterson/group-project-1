# Group-Project-1: Is Twitter an Influencer

The scope of our project will demonstrate the relationships between financial indices and how the disclosure of new information impacts the relationships between those indices and the NASDAQ Biotechnology Index.  Our analysis will utilize databases from Alpaca and visualize the information in Plotly graphs to show the relationship over a certain timeframe (5 years). We define “new information” as the public announcement of some significant global or national information. We will collect our news data from Twitter API. 

---


## Technologies
This project leverages python 3.8.8 with the following packages:

* [os module](https://docs.python.org/3/library/os.html) - This module provides a portable way of using operating system dependent functionality.

* [request](https://anaconda.org/anaconda/requests) - Makes request in python.

* [JSON](https://docs.python.org/3/library/json.html) - Used to transfer data as text. Used by APIs and Databases.

* [pandas](https://pandas.pydata.org/docs) - For manipulating the DataFrame.

* [dotenv](https://pypi.org/project/python-dotenv/) - Reads key-value pairs from .env file that can be set as environment variables.

* [Jupyter Lab](https://jupyterlab.readthedocs.io.en/stable) - For code and visualizations.

* [matplotlib](https://matplotlib.org/) - Used to create static, animate, and interactive visualizations in Python.

* [numpy](https://numpy.org/install/) - For scientific computing with python

* [Alpaca Trade API](https://alpaca.markets/docs/) - Used to get API data to run within the application

* [hvplot](https://hvplot.holoviz.org/user_guide/Introduction.html) - For creating the visualization of our data from the DataFrame.

* [collections](https://docs.python.org/3/library/collections.html) - For storing collections of data and counting them.

## Installation Guide


In gitbash after you have activated your dev environment, install the following:

```python
  pip install jupyter lab
```

*Anaconda requests

    `conda install -c anaconda request`
  
 
![install request](https://github.com/mckayav3/Module5_Challenge/blob/main/Images/install_requests.JPG)


*Json

    `conda install -c jmcmurray json`
    
    
![install json](https://github.com/mckayav3/Module5_Challenge/blob/main/Images/install_json.JPG)



*Dotenv

    `pip install python-dotenv`
    
    
![install dotenv](https://github.com/mckayav3/Module5_Challenge/blob/main/Images/install_dotenv.JPG)



*Alpaca Trade API

    `pip install alpaca-trade-api`
    
    
![install alpaca](https://github.com/mckayav3/Module5_Challenge/blob/main/Images/install_alpaca.JPG)


In gitbash after you have activated your dev environment, install the following:

```python
  pip install jupyter lab
```
   
*Plotly

    `conda install -c plotly plotly=4.13`
    
![install plotyly](https://github.com/mckayav3/Module6_Challenge/blob/main/Images/install_plotly.JPG)


*Pyviz Hvplot

    `conda install -c pyviz hvplot`
    
![install pyviz hvplot](https://github.com/mckayav3/Module6_Challenge/blob/main/Images/install_pyviz_hvplot.JPG)

In gitbash after you have activated your dev environment, install the following:

```python
  pip install jupyter lab
```
   
*Plotly

    `conda install -c plotly plotly=4.13`
    
![install plotyly](https://github.com/mckayav3/Module7_Challenge/blob/main/images/install_plotly.JPG)


*Pyviz Hvplot

    `conda install -c pyviz hvplot`
    
![install pyviz hvplot](https://github.com/mckayav3/Module7_Challenge/blob/main/images/install_pyviz_hvplot.JPG)

*Sqlalchemy

    `conda list sqlalchemy`
    
    `pip install SQLAlchemy`
    
![list sqlalchemy](https://github.com/mckayav3/Module7_Challenge/blob/main/images/list_sqlalchemy.JPG)

![install sqlalchemy](https://github.com/mckayav3/Module7_Challenge/blob/main/images/install_sqlalchemy.JPG)


## Examples

The images below show the different types of charts and graphs that should result from running the code in the Twitter Influencer. By reviewing the charts and graphs we can analyze the Twitter Influencer application to compare NASDAQ Biotechnology Index prices to keywords pulled from Twitter API.






## Usage

Given we want to check the effect of news events on NBI prices. When a keyword from the word bank is tracked over time from Twitter API. Then we see if this had a negative, positive, or no influence on the NBI prices during that event.

## Contributors

Alissa Bolla
Michael Gough
Andrew McKay
Arturo Garcidueñas
