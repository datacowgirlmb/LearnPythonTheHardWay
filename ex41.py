import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []      # build an empty list

PHRASES = {
	"class %%%(%%%):":
	 "Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)" :
	 "class %%% has-a __init__ that takes self and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	 "class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
	 "Set *** to an instance of class %%%.",
	"***.***(@@@)":
	 "From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
	 "From *** get the *** attribute and set it to '***'."
}
	
# do they want to drill phrases first
# If argv contains 2 arguments & the first is equal to "english"
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website
# read all the lines from the webpage
# for each line in the webpage, strip the word (i.e., remove leading & trailing spaces), & append it to the WORDS list using utf-8 encoding
for word in urlopen(WORD_URL).readlines():
	WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]  # get a list of random values from the WORDS list containing as many values as "%%%" occurs in the capitalized snippet string
	other_names = random.sample(WORDS, snippet.count("***"))    # get a list of random values from the WORDS list containing as many values as "***" occurs in the snippet string
	results = []        # build an empty list
	param_names = []    # build an empty list
	
	for i in range(0, snippet.count("@@@")):        # loop for the number of times "@@@" occurs in the snippet string
		param_count = random.randint(1,3)           # get a random integer between 1 & 3; assign it to the param_count list
		param_names.append(', '.join(
            random.sample(WORDS, param_count)))     # get a random sample of param_count words in the WORDS array & join these values into a comma-separated string
		
		
	for sentence in snippet, phrase:                # for each value in lists snippet & phrase
		# this is how you duplicate a list or string
		result = sentence[:]                        # make a copy of the sentence list
		
		# fake class names
		for word in class_names:                    # for each item in the class_names list
			result = result.replace("@@@", word, 1) # update the result list by replacing the first occurence of "@@@" with the value of word
			
		# fake other names
		for word in other_names:                    # for each item in other_names list
			result = result.replace("***", word, 1) # update the result list by replacing the first occurrence of "***" with the value of word
			
		# fake parameter lists
		for word in param_names:                    # for each item in param_names list
			result = result.replace("@@@", word, 1) # update result list by replacing the first occurrence of "@@@" with the value of word
			
		results.append(result)                      # append result to the results list
		
	return results
	
	
# keep going until they hit ctrl-d
try:
	while True:
		snippets = list(PHRASES.keys())             # get keys from PHRASES dictionary & make them into a list
		random.shuffle(snippets)                    # reorganize the items in the snippets list
		
		for snippet in snippets:                    # loop through each item in the snippets list
			phrase = PHRASES[snippet]               # get the value corresponding to key snippet in dictionary PHRASES & assign it to phrase
			question, answer = convert(snippet, phrase) # run the convert function & assign the results to question & answer, respectively
			if PHRASE_FIRST:
				question, answer = answer, question
				
			print(question)
			
			input("> ")
			print(f"ANSWER:  {answer}\n\n")	
except EOFError:
    print("\nbye")