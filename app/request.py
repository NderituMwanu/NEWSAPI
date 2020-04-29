import urllib, json
from models import Source, Article
import requests


# Aquring the news source from the base url

base_url = app.config['SOURCES_BASE_URL']
base_url_article = app.config['ARTICLES_BASE_URL']
apiKEY = app.config['API_KEY']

def get_sources():
    
    get_source_url = base_url.format(api_key)
    res = requests.get(get_source_url)
    data = res.json().get('sources')
    return process_sources(data)

def process_sources(sources_list):
    '''
    View function for source objects
    '''
    sources_results = []
    for source_item in sources_list:
        name = source_item.get('name')
        id = source_item.get('id')
        description = source_item.get('description')
        category = source_item.get('category')
        language = source_item.get('language')
        url = source_item.get('url')
        
        
        if url:
            sources_object = Source(name,id,description, url, category, language)
            sources_results.append(sources_object)

            # appends the new object in the source_list
        
    return sources_results

def get_articles(source_id):
    '''
    view function that gets the articles
    '''

    get_articles_url = base_url_article.format(source_id, api_key)
    res = requests.get(get_articles_url)
    articles_data = res.json().get('articles')

    return process_articles(articles_data)

def process_articles(articles_list):
    articles = []
    if articles_list:
        for article in articles_list:
            articles.append(article)
        return articles

        
        
        



