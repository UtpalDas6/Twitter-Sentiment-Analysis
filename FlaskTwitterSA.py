'''from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()'''
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import tweepy
from textblob import TextBlob
ck='yO3xKe4YCkGv2Tu3W8rmjJWOX'
cs='JWuDVy8A1f7TITyK5gZoguYNvAS7xJgJ4xQUFclAAp2E6Q28O1'

at='979590528483258368-heb1Vj5r7sjOW1rMGPXrEVEtK7I8Frk'
ats='2XCyn0gOFMxxINO9IDrr6PDgznqUEN8AGCIlxHSZKhOtt'

auth=tweepy.OAuthHandler(ck,cs)
auth.set_access_token(at,ats)

api=tweepy.API(auth)

public_tweets=api.search('IPL')
p=[]
s=[]
t=[]
for tweet in public_tweets:
    t.append(pd.to_datetime(tweet._json['created_at']))
    analysis=TextBlob(tweet.text)
    #print(type(analysis.sentiment))
    p.append(analysis.sentiment[0])
    s.append(analysis.sentiment[1])
d={'polarity':p,'subjectivity':s,'time':t}
df=pd.DataFrame(data=d)
df = df.sort_values('time', ascending=True)
ax = df[['subjectivity','polarity']].plot(kind='bar',title='IPL:Twitter Sentimental Analysis')
ax.set_xlabel('Tweets', fontsize=12)
ax.set_ylabel('polarity/subjectivity', fontsize=12)
plt.show()
plt.plot(df['time'], df['polarity'])
plt.xlabel('date')
plt.ylabel('polarity')
plt.title('IPL:Twitter Sentimental Analysis')
plt.show()