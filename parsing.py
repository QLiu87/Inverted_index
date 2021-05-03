import re
import os
import zipfile
import string
from nltk.stem import *

# Regular expressions to extract data from the corpus
doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)

#initialize variables
docs_list = {}
docs_info = {}
term_info = {}
termID = 1
docID = 1
term_id = {}
stemmer = PorterStemmer()

#read stop words
stop_words = []
with open(os.path.dirname(__file__) + "/stopwords.txt", 'r') as f:
	for line in f:
		stop_words.append(line.strip())


with zipfile.ZipFile("ap89_collection_small.zip", 'r') as zip_ref:
    zip_ref.extractall()

# Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
#for dir_path, dir_names, file_names in os.walk("TEST"):
    allfiles = [os.path.join(dir_path, filename).replace("\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]

for file in allfiles:
    with open(file, 'r', encoding='ISO-8859-1') as f:
        filedata = f.read()
        result = re.findall(doc_regex, filedata)  # Match the <DOC> tags and fetch documents

        for document in result[0:]:
            # Retrieve contents of DOCNO tag
            docno = re.findall(docno_regex, document)[0].replace("<DOCNO>", "").replace("</DOCNO>", "").strip()
            
            # Retrieve contents of TEXT tag
            text = "".join(re.findall(text_regex, document))\
                      .replace("<TEXT>", "").replace("</TEXT>", "")\
                      .replace("\n", " ").lower().translate(str.maketrans('', '', string.punctuation))

            # step 1 - lower-case words, remove punctuation, remove stop-words, etc.
            # remove stop words
            for word in stop_words:
                text = re.sub(r'\b'+ word + r'\b', '', text)
            
             # stemming
            text = stemmer.stem(text)
            text = text.split()
            #print(text)
            # step 2 - create tokens\
            docno = docno.lower()
            # step 3 - build index
            pos = 1
            for term in text:
                if term not in term_id.keys():
                    term_id[term] = (termID, 1) # id, freq
                    termID += 1
                else:
                    term_id[term] = (termID, term_id[term][1] + 1)
                if term in docs_list:
                    if docno in docs_list[term].keys():
                        docs_list[term][docno].append(pos)
                        pos += 1
                    else:
                        docs_list[term][docno] = [pos]
                        pos += 1
                else:
                    doc_term = dict()
                    posting_list = []
                    posting_list.append(pos)
                    doc_term[docno] = (posting_list)
                    docs_list[term] = (doc_term)
                    pos += 1
            docs_info[docno] = (docID, len(text)) #doc ID, total terms
            docID += 1


def get_num_doc_freq(t):
    return len(docs_list[t].keys())

def get_term_doc_freq(t, d):
    return len(docs_list[t][d])

def get_term_pos(t, d):
    return docs_list[t][d]

print(docs_list['celluloid'])


def create_term_index():
    f = open("term_index.txt", "w")
    for t in term_id.keys():
        output = ""
        output += str(term_id[t][0]) + "\t"
        for doc in docs_list[t]:
            #print(doc)
            for p in docs_list[t][doc]:
                output += str(docs_info[doc][0]) + ":" + str(p) +"\t"
        f.write(output + "\n")
    f.close()







