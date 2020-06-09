# coding: utf-8
import json
import pymongo
from mitmproxy import ctx

#client = pymongo.MongoClient('localhost')
#db = client['igetget']
#collection = db['books']

def response(flow):
    #global collection
    url = 'https://dedao.igetget.com/v3/discover/bookList'
    #url = 'https://entree.igetget.com/michelangelo/v1/book-list/recommend/info'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        books = data.get('c').get('list')
        for book in books:
            data = {
                'title': book.get('name'),
                'cover': book.get('cover'),
                'summary': book.get('other_share_summary'),
                'price': book.get('price')
            }
            ctx.log.info(data)
            #collection.insert(data)

