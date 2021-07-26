# Group-Project-1: Is Twitter an Influencer

The scope of our project will demonstrate the relationships between financial indices and how the disclosure of new information impacts the relationships between those indices and the NASDAQ Biotechnology Index.  Our analysis will utilize databases from Alpaca and visualize the information in Plotly graphs to show the relationship over a certain timeframe (5 years). We define “new information” as the public announcement of some significant global or national information. We will collect our news data from Twitter API. 

---

##About
In this project, we are testing for correlations between the public disclosure of information
about an industry and the prices of assets for companies in that industry. 

We use Tweets to indicate the release of information. To narrow the data collection task, we 
will gather historical tweets from high-influence accounts in the knowledge domain of a
target industry. For this experiment, we selected the Biotech industry.
 
## NLP
see [nlp_on_tweets.py](./nlp_on_tweets.py), [parse_tweet_response.py](./parse_tweet_response.py)
### Tweets
Twenty high-profile twitter accounts in the biotech space were identified as listed [here](./biotech_influcencers.txt).
The Twitter API was used to extract account IDs and all historical tweets from these influencer 
accounts.

### Target Industry Language
To measure how many Tweets over time refer to topics in the biotech industry, we obtained a
document embedding of the summary statement for each of five companies as found on Yahoo!
Finance. Using Spacy to break each summary into sentences, each sentence was classified into
a word vector using the 700-parameter pre-trained biotech-specific Sent2Vec model obtained
[here](https://github.com/ncbi-nlp/BioSentVec). To obtain a document-embedding, we used
the mean of the sentence vectors for each document.
 
This same model and method was used to classify each tweet in the industry domain.
 
### Similarity Detection
Given a set of document embeddings for each company and a set of tweet embeddings on the
same domain-specific Sent2Vec model, we calculated the cosine similarity between each tweet
and each of five document embeddings to obtain a matrix of similarity metrics roughly
indicating the degree to which each tweet refers to concepts related to each company.
These data were dumped to a [csv file](./tweet_cosine_similarities.csv)

### Data Cleaning
To obtain a time series for comparison with each company from the list of historical
tweets, we bucketed our index by day and then found the sum of the cosine similarities
of tweets from that day with respect to each company. See 
    


          


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
  pip install -r requirements.txt
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
