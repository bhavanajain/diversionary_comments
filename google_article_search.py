from googleapiclient.discovery import build

def google_search(search_term, api_key, cse_id, **kwargs):
     service = build("customsearch", "v1", developerKey=api_key)
     res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
     links = [curr['link'] for curr in res['items']]
     return links