
from flask import render_template
from ..request import get_sources, get_articles
from . import main
from flask_http_response import success, result, error
    

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    gets the articles
    '''
    
    articles = get_articles(source_id)
    return render_template('article.html', articles=articles)


@main.route('/')
def home():
    #news =head_lines
    return render_template('index.html')
 
 
     
@main.route('/results/',methods=['POST']) 
def get_results():
    keyword = request.form['keyword']  #getting input from user
 
    news = newsapi.get_top_headlines(q=keyword,
                                     #sources='bbc-news,the-verge',#optional and you can change
                                     #category='business', #optional and you can change also
                                     language='en', #optional and you can change also
                                     country='in')
    #print(news['articles'])
    return render_template('index.html',news=news['articles'])