import os
from newsapi import NewsApiClient
import questionary
from pprint import pprint
import json

NEWS_API_KEY_PATH = '/Users/michael/news_api_key'

VIEW_TOP = "View top headlines by keyword(s)"
VIEW_ALL = "View all articles by keyword(s)"
DOWNLOAD_TOP = "Download top headlines by keyword(s)"
DOWNLOAD_ALL = "Download all articles by keyword(s)"
DONE = "Done"


def get_news_api_key():
    try:
        with open(NEWS_API_KEY_PATH, 'r') as _file:
            return _file.read().strip()
    except:
        return questionary.text("Enter News API Key: ").ask()


def fetch_all_headlines(sort='relevancy', **kwargs):
    results = news_client.get_everything(q=kwargs['query'],
                           #sources=','.join(sources),
                           #domains='bbc.co.uk,techcrunch.com',
                           from_param=kwargs['start_date'],
                           to=kwargs['end_date'],
                           language='en',
                           sort_by=sort)
    total_results = results['totalResults']
    print(f'total results: {total_results}')
    yield results['articles']
    pages = int(total_results/100.0)
    for i in range(2, pages):
        res = news_client.get_everything(q=kwargs['query'],
                           from_param=kwargs['start_date'],
                           to=kwargs['end_date'],
                           language='en',
                           sort_by=sort,
                           page_size=100,
                           page=i)
        yield res['articles']


def fetch_top_headlines(**kwargs):
    category = questionary.select("Select a category for top headlines: ",
                                  choices=[
                                      'business',
                                      'entertainment',
                                      'general',
                                      'health',
                                      'science',
                                      'sports',
                                      'technology'
                                  ]).ask()
    res = news_client.get_top_headlines(q=kwargs['query'],
                                        category=category,
                                        language='en',
                                        country='us',
                                        page_size=100,
                                        page=1
                                        )
    total_results = res['totalResults']
    pages = int(total_results/100.0)
    print(f'total results: {total_results}')
    yield res['articles']
    for i in range(2, pages):
        res = news_client.get_top_headlines(q=kwargs['query'],
                                        category=category,
                                        language='en',
                                        country='us',
                                        page_size=100,
                                        page=i
                                        )
        yield res['articles']


def get_date_range():
    start_date = questionary.text("Start Date? (yyyy-mm-dd), <enter> for None").ask()
    if start_date == '':
        start_date = None
    end_date = questionary.text("End Date? (yyyy-mm-dd), <enter> to default to today's date").ask()
    if end_date == '':
        end_date=None

    return start_date, end_date


def view_articles(fetcher):
    for page in fetcher:
        for article in page:
            pprint(article)
        input("\n<enter> to view next page or <ctrl-c> to go back")
    print("-- end --")


def get_fetcher(choice, query, date_range):
    fetcher = {
        VIEW_TOP: fetch_top_headlines,
        DOWNLOAD_TOP: fetch_top_headlines,
        VIEW_ALL: fetch_all_headlines,
        DOWNLOAD_ALL: fetch_all_headlines
    }[choice](start_date=date_range[0],
              end_date=date_range[1],
              query=query)
    if choice == VIEW_TOP or choice == DOWNLOAD_TOP:
        fetcher = fetch_top_headlines
    elif choice == VIEW_ALL or choice == DOWNLOAD_ALL:
        fetcher = fetch_all_headlines
    return fetcher(query=query, start_date=date_range[0], end_date=date_range[1])


def download_articles(fetcher, description):
    output = []
    for page in fetcher:
        output.extend(page)

    file_path = f'{description}.json'
    with open(file_path, 'a') as _file:
        _file.write(json.dumps({'articles': output}))
    print(f"saved {len(output)} results to {file_path}")


def search_articles(choice=None):
    if choice == DONE:
        return False
    else:
        query = questionary.text("Search Keyword(s)? ").ask()
        if query == '':
            query = None

        date_range = get_date_range()
        fetcher = get_fetcher(choice, query, date_range)

        download = {DOWNLOAD_TOP: True, DOWNLOAD_ALL: True}.get(choice, False)
        if download:
            download_articles(fetcher, description=f'{query}-{date_range[0]}-{date_range[1]}')
        else:
            try:
                view_articles(fetcher)
            except KeyboardInterrupt:
                pass

        more = questionary.select("\nanother search?", choices=["Yes", "No"]).ask()
        return {"Yes": True, "No": False}[more]


if __name__ == "__main__":
    run = True
    news_api_key = os.environ.get('NEWS_API_KEY', get_news_api_key())
    news_client = NewsApiClient(api_key=news_api_key)

    while run:
        filter = questionary.select(
            "What do you want to do?",
            choices=[
                VIEW_TOP,
                VIEW_ALL,
                DOWNLOAD_TOP,
                DOWNLOAD_ALL,
                DONE]).ask()
        run = search_articles(filter)
