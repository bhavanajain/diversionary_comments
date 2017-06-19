import newspaper

def extractArticle(link):
    article = newspaper.Article(url=link)
    article.download()
    article.parse()
    ans = article.text
    return ans