from colorama import init, Fore
from timeit import default_timer as timer

from patterns import patterns


def main():
	init()
	with open('input.txt', 'r') as input_file:
		words = input_file.read().strip().split('\n')

	start_time = timer()
	for word in words:
		print('%s: %s' % (
			word,
			', '.join(patterns[''.join(sorted(word.lower()))]) if ''.join(sorted(word.lower())) in patterns else ''
		))
	end_time = timer()

	print()
	print("Solved %s anagram(s)" % (Fore.GREEN + str(len(words)) + Fore.WHITE))
	print("In %s second(s)." % (Fore.GREEN + str(end_time - start_time) + Fore.WHITE))
	print("Which is approximately %s anagram(s) per second" % (Fore.GREEN + str(len(words) / (end_time - start_time)) + Fore.WHITE))
	print("Or %s second(s) to solve 1 anagram." % (Fore.GREEN + str((end_time - start_time) / len(words)) + Fore.WHITE))


if __name__ == '__main__':
	main()
