"""Read in the file specified on the command line. Do a simple split() on whitespace to obtain all the words in the file. Rather than read the file line by line, it's easier to read it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file to a list of all the words that immediately follow that word in the file. The list of words can be be in any order and should include duplicates. So for example the key "and" might have the list ["then", "best", "then", "after", ...] listing all the words which came after "and" in the text. We'll say that the empty string is what comes before the first word in the file.

With the mimic dict, it's fairly easy to emit random text that mimics the original. Print a word, then look up what words might come next and pick one at random as the next work. Use the empty string as the first word to prime things. If we ever get stuck with a word that is not in the dict, go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a random.choice(list) method which picks a random element from a non-empty list.
"""

import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  f = open('enText.txt','r').read()
  dict=[]
  dict=f.split()
  l2=list(set(dict))
  cidian={}
  for danci in l2:
	  m=[]
	  for i in range(len(dict)-1):
		  if dict[i]==danci:
			  m.append(dict[i+1])
	  cidian[danci]=m	  
  return cidian


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  word = 'London'
  print(word,end=' ')
  for i in range(100):
	  for keys in mimic_dict.keys():
		  if keys==word:
			  if len(mimic_dict[keys])==0:
				  word='London'
				  print(word,end=' ')
			  else:
				  d=random.choice(mimic_dict[keys])
				  print(d,end=' ')
				  word=d
  return 


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print('command line usage: python ex1.py file-to-read')
    sys.exit(1)

  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
