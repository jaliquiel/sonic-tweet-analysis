from twitter import *

CONSUMER_KEY = 'tVWZWJfKFv2s4qdJIOwjPBIwk'
CONSUMER_SECRET ='17B4xPaZJ5NNHwfXmnRAuVvmYkb8JnvfEXhXKGI3GuTWZ2tiTO'
OAUTH_TOKEN = '1190012319213867008-O8vhqrklw1Z1kTcchMa2t5X9Qhscch'
OAUTH_TOKEN_SECRET = 'nLyHDpan9zyCV5lTit4XKppm44QWUeW87jsHrQnl3om49'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
print(t)

search_results = t.search.tweets(q="#sonic", count= '10')
print(search_results)