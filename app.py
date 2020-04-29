from flask import Flask,render_template,request
from newsapi import NewsApiClient


app = Flask(__name__)
 
yourAPIKEY = 'e35e468d3c6b4178a34ed70d92f68356'   # write your API key here
 
newsapi = NewsApiClient(api_key=yourAPIKEY)
 
 
#print(top_headlines['articles'])
 
#head_lines=[]
 
#for news in top_headlines['articles']:
 #   head_lines.append(news['title'])
 
 
@app.route('/')
def home():
    #news =head_lines
    return render_template('index.html',news='')
 
 
     
@app.route('/results/',methods=['POST']) 
def get_results():
    keyword = request.form['keyword']  #getting input from user
 
    news = newsapi.get_top_headlines(q=keyword,
                                     #sources='bbc-news,the-verge',#optional and you can change
                                     #category='business', #optional and you can change also
                                     language='en', #optional and you can change also
                                     country='in')
    #print(news['articles'])
    return render_template('index.html',news=news['articles'])
 
 
 
if __name__ == "__main__":
    app.run()