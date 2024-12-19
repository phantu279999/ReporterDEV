from bs4 import BeautifulSoup


def count_word(text):
	if not text:
		return 0
	soup = BeautifulSoup(text, 'html.parser')
	texts = [len(it.strip().split(" ")) for it in soup.strings if it.strip()]
	return sum(texts)


def reading_time(word_count, words_per_minute=200):
	if word_count <= 0:
		return 0
	return round(word_count / words_per_minute)
