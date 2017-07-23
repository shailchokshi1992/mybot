from random  import randint
from time    import sleep
from tweepy  import OAuthHandler, API

infile = open('qutoes.txt', 'r')
Facts = []
for line in infile:
    Facts.append(line.strip('\n'))
infile.close()

Hashtags = ['#inspirational', '#motivaion','#thought','#motivationmylife','#mylifemyrules']

# Credentials to access Twitter API
ACCESS_TOKEN    = '845540536417103875-Z5jyS1thWiaoNtHaqIrFntAw7b3vEhL'
ACCESS_SECRET   = 'JETplJEpYDZ16ypfrGgQmCXrUIMILJhn0xaSGDYpyuwsc'
CONSUMER_KEY    = '5nTfkoZhy7OdOGBCOUoOm0W5M'
CONSUMER_SECRET = '6xjOSN5A9gCqXb5iBdUq8rtiVe0QVdV7tieDVuX2w3sLCzKTKH'

# Initiate the connection to Twitter API
Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)

outfile = open('Log.txt', 'a')
i = 0
while i < len(Facts):
    TwitterBot.update_status(Facts[i]+' '+Hashtags[randint(0,len(Hashtags)-1)]) # Tweet a fact as well as a random hashtag
    outfile.write(str(i)+': '+Facts[i]+'\n') # Keep a log of tweeted facts in case server shuts off
    outfile.flush()
    sleep(randint(30, 36)*5) # Tweet every 4-5 hours to prevent bot recognition
    i += 1
