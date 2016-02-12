ssid = "hellogoodbye"
dictionary = set(["hell", "hello", "good", "bye", "goodbye"])

# Generator that produces every possible sentence
def combos(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield (start, end)
        for split in combos(end):
            result = [start]
            result.extend(split)
            yield result


# Get each sentence, rank it, and display top n
def split(ssid, words, top):
	sentences = list()

	for combo in combos(ssid):
		wordcnt = 0
		sentences.append((score(combo, words), combo))
	sentences.sort(reverse=True)

	for i in range(0, top):
		print(sentences[i])



# Ranking function to get the best sentences
def score(sentence, words):
	# set to desired function
	wordcnt = 0
	for word in sentence:
		if word in words:
			wordcnt += 1
	return wordcnt


split(ssid, dictionary, 10)
