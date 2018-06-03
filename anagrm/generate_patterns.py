import json


def main():
	patterns = {}

	with open('dictionary.txt') as words_file:
		words = words_file.read().strip().split('\n')

	for word in words:
		pattern = ''.join(sorted(word.lower()))
		if pattern in patterns:
			patterns[pattern].append(word)
		else:
			patterns[pattern] = [word]

	with open('patterns.py', 'w') as patterns_file:
		patterns_file.write('patterns = ')
		patterns_file.write(json.dumps(patterns, indent=4))


if __name__ == '__main__':
	main()
