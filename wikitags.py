from urllib import request
from bs4 import BeautifulSoup
from mediawiki import MediaWiki, DisambiguationError

def getAnchorTags(list_of_names):
    wikipedia = MediaWiki()
    output = []
    for x in list_of_names:
        per = []
        try:
            curr = wikipedia.page(x)
            soup = BeautifulSoup(request.urlopen(curr.url).read(),"html.parser")
            soup = (soup.find('p'))
            temp = [tag['href'] for tag in soup.select('a[href]')]
            for g in temp:
                if 'wiki' in g and not 'ogg' in g:
                    k = g[6:]
                    per.append(k)
        except DisambiguationError as e:
            per = []
        output += per
    return output