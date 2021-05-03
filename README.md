# CS172 - Assignment 1 (Tokenization)

## Team member 1 - Qi Liu
## Team member 2 - None

###### Provide a short explanation of your design
This program is implemented using Python and provided base code for parsing. There are two .py tles in total:
1.  parsing.py
2.  read_index.py

Parsing.py file parses the given data file, and outputs a .txt file named `term_index.txt`.

read_index.py is the user interface, and it exits upon any incorrect input or empty result.

Data structure: term_id[] is a dictionary that stores every term's id and total frequency.
docs_list is a dictionary that uses term as its key, and another dictionary as its value. This inner dictionary then uses docno as its key and a list of positions as its value.
docs_info is a dictionary that uses docno as its key, and docID, and total terms in each doc as its values.
###### Language used, how to run your code, if you attempted the extra credit (stemming), etc. 
The language used is Python3. 

Extra Credit attempted and finished:
1.  Stemming(used PorterStemmer from nltk library)
2.  Extra Credit option 1: term_index.txt

To run the code:
1.  `$ python ./read_index.py --term returning`
2.  `$ python ./read_index.py --doc AP890101-0001`
3.  `$ python ./read_index.py --doc AP890101-0001 --term celluloid`

For option 2 and 3, make sure docno is lower case.