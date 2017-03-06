"""
This computes cosine distances for a subset of fruits/vegs
based on GloVe data.

mcrae_fruitveg.txt is hand-picked list of fruits/vegs
from the McRae concept dataset.

- input: vocabulary, glove data
- output: cosine similarities in a txt
"""

from collections import defaultdict
from scipy import spatial

GLOVE_INPUT = "../glove/glove.6B.300d.txt"
VOCAB = "mcrae_fruitveg.txt"
OUTPUT = "fruitveg_sim_glove.txt"

def main():
	vocab_file = open(VOCAB, 'r')
	vocabulary = set()
	for line in vocab_file:
		vocabulary.add(line.strip())
		
	f = open(GLOVE_INPUT, 'r')
	vectors = defaultdict(list)
	for line in f:
		word_vec = line.split()
		if word_vec[0] in vocabulary:
			vectors[word_vec[0]] = [float(x) for x in word_vec[1:]]

	output = open(OUTPUT, 'w')
	words = vectors.keys()
	for i in range(len(words)):
		for j in range(i+1, len(words)):
			dist = 1- spatial.distance.cosine(vectors[words[i]], vectors[words[j]])
			output.write(words[i] + ' ' + words[j] + ' ' + str(dist) + '\n')

if __name__ == '__main__':
	main()
