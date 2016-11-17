'''
parse.py
Parse json file and create pickle file for processing by pagerank.py
'''
import json
import pickle
from pprint import pprint
pages = {}
counter = 0
with open("sample.input.json") as inputfile:
	for line in inputfile:
		line = json.loads(line)		
		site = line['artist']

		links = line['influencedby']
		links_dict = {}
		for l in links:
			to_insert = {}
			to_insert[l] = 0
			links_dict.update(to_insert)

		pages[site] = links_dict
		if counter % 1000 == 0:  # Progress track
			print counter
		counter += 1
outfile = open("sample.pickle", "w")
pickle.dump(pages, outfile)
print "Done"
# pprint(pages)
