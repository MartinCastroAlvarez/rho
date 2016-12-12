#!/usr/bin/python
import sys

positive_words 	= open("./txt/positive.txt").read().split('\n')
negative_words 	= open("./txt/negative.txt").read().split('\n')
punctuation    	= open("./txt/punctuation.txt").read().split('\n')
tweets	  	= open("./txt/obama_tweets.txt").read().split('\n')

interests = {} 
mood = { 
	"positive": 	0,
	"negative": 	0,
}
for tweet in tweets: 
	positive_counter = 0
	negative_counter = 0
	for p in punctuation:
		if p:
			tweet = tweet.replace(p," ")
	for word in tweet.split(" "):
		w = word.lower()
		if w and len(w)>2:
			if w in positive_words:
				positive_counter += 1
			elif w in negative_words:
				positive_counter += 1
		if w and len(w)>4:
			if w in interests:
				interests[w] += 1 
			else:
				interests[w] = 1 
	if positive_counter > negative_counter:
		mood['positive'] += 1
	else:
		mood['negative'] += 1

ordered_interests = []
for k,v in interests.items():
	i=0
	while i<len(ordered_interests) and ordered_interests[i]['value']>v:
		i+=1
	d = { 
		"key": 	 k,
		"value": v, 
	} 
	ordered_interests.insert(i,d)

print "Interests:" 
for i in ordered_interests[0:20]:
	print "%-20.20s %-10i" % (i['key'],i['value']) 
print mood
