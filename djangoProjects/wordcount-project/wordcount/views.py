# need this lib for responding with http
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request, 'home.html')

def eggs(request):
	return HttpResponse('<h1>Eggs</h1>')

def about(request):
	return render(request, 'about.html')

def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()

	worddict = {}
	# count the number of individual words
	for word in wordlist:
		if word in worddict:
			# increemetn amount
			worddict[word] += 1
		else:
			worddict[word] = 1

	sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})
