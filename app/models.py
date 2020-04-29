class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,id,name,description, url,category,language):
        self.name = name
        self.id =  id
        self.description = description
        self.url = url
        self.category = category
        self.language = language
       

class Article:
    '''
    Article class to define Article Objects
    '''
    def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt):
        self.name = name
        self.id = id
        self.author =  author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
    

