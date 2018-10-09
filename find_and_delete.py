import tweepy
import re
import time
from urllib.request import urlopen
import requests

###twitter
auth = tweepy.OAuthHandler([YOUR TWITTER API KEY], [YOUR TWITTER API KEY])
auth.set_access_token([YOUR TWITTER API KEY], [YOUR TWITTER API KEY] )
api = tweepy.API(auth)
###
m_=1
g_=2
y_=2014 #CHANGE HERE WITH THE YEAR YOU WANT TO START YOUR PURGE!!
def find(m,g,y):
	url = 'https://twitter.com/search?q=from%3Adigital_mine_%20since%3A'+str(y)+'-1-'+str(g-1)+'%20until%3A'+str(y)+'-'+str(m)+'-'+str(g)+'&src=typd'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	response = requests.get(url, headers=headers)
	#print(response.content)

	id_=re.findall('id="profile-tweet-action-reply-count-aria-(.+?)"',str(response.content))
	print (id_)
	return id_
x=0
idd=find(m_,g_,y_)
while y_<=2017: #CHANGE HERE WITH THE YEAR YOU WANT TO STOP YOUR PURGE!
	print ('YEAR:',y_)
	print('MONTH:',m_)
	print ('DAY',g_)
	if len(idd)>0:
		for i in idd:	
			try:
				api.destroy_status(i)
				x+=1
			except Exception as e:
				print (e)
		idd=find(m_,g_,y_)
		
	else:
		g_+=1
		idd=find(m_,g_,y_)
		if g_==32:
			m_+=1
			g_=2
			idd=find(m_,g_,y_)
		if m_==13:
			y_+=1
			m_=1
			idd=find(m_,g_,y_)
	print ('DELETED:',x)	

