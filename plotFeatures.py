import matplotlib.pyplot as plt
import pylab
import numpy as np
import pandas as pd

location = 'plots\\' 
features = ['urlsCount', 'numOfUrlTweets', 'hashtagsCount', 'repliesCount', 'retweetsCount', 'tweetSimilarity', 'spamWordsRatio', \
		'followers', 'followings', 'followerFollowingRatio', 'averageFollowingRate', 'screenNameLength']

featuresFile = "features.csv"

df = pd.read_csv(featuresFile, header = 0)

spammers = []
legitimate = []
for index, row in df.iterrows():
	if row[-1] == 'spammers':
		spammers.append(row[:-1])
	else:
		legitimate.append(row)

spamArray = np.array(spammers).T
legitArray = np.array(legitimate).T

for feature in features:
	spamLine = spamArray[features.index(feature)]
	legitLine = legitArray[features.index(feature)]
	plt.plot(spamLine, color = 'r', label = 'Spammers')
	plt.plot(legitLine, color = 'b', label = 'Non-Spammers')
	plt.title(feature)
	pylab.legend(loc = 'upper right')
	plt.show()
	filename = location + feature + "Plot"
	#plt.savefig(filename)
