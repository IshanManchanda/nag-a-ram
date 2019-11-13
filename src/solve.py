from timeit import default_timer as timer

from colorama import Fore, init

from patterns import patterns


def main():
	with open('input.txt', 'r') as input_file:
		words = input_file.read().strip().split('\n')
	out = []
	start_time = timer()

	for word in words:
		key = ''.join(sorted(word.lower()))
		out.append('%s: %s' % (
			word,
			', '.join(patterns[key]) if key in patterns else ''
		))

	end_time = timer()
	init()
	print('\n'.join(out))

	print("\nSolved %s anagram(s)" % (
		Fore.GREEN + str(len(words)) + Fore.WHITE
	))
	print("In %s second(s)." % (
		Fore.GREEN + str(end_time - start_time) + Fore.WHITE
	))
	print("Which is approximately %s anagram(s) per second" % (
		Fore.GREEN + str(len(words) / (end_time - start_time)) + Fore.WHITE
	))
	print("Or %s second(s) to solve 1 anagram." % (
		Fore.GREEN + str((end_time - start_time) / len(words)) + Fore.WHITE
	))


if __name__ == '__main__':
	main()
