import praw
import re
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

def getRed(link):
    r = praw.Reddit(client_id= '7sdG8ZEP0wOzzQ',
                client_secret='IiU7QAq-HPfmYhTlgqdVkMnsje4',
                user_agent = 'Utsav FlareApp 0.1 by utsavsingla',
                redirect_uri='http://localhost:5000')
    submission = r.submission(url=link)
    print(submission)
    title = str(submission.title)
    body = str(submission.selftext)
    coms = ''
    auths = ''
    x=0
    for comments in submission.comments:
        if x>30:
            break
        coms+= " "+ str(comments.body)
        auths += " "+str(comments.author)
        x+=1
    
    finalStr = title + coms + " "+ body + " "+ auths
    cleaned = cleanText(finalStr)
    return cleaned

def cleanText(text):
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = set(stopwords.words('english'))
    text = BeautifulSoup(text, "lxml").text # HTML decoding
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text
    text = BAD_SYMBOLS_RE.sub('', text) # delete symbols which are in BAD_SYMBOLS_RE from text
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)
    return text