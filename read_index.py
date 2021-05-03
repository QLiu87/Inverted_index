# This file should contain code to receive either a document-id or word or both and output the required metrics. See the assignment description for more detail.
import sys
import parsing

if (len(sys.argv) - 1 < 4):
    term = sys.argv[2]
    if (sys.argv[1] == "--doc"):
        print(f'Listing for document: {term}')
        print(f'DOCID: {parsing.docs_info[term][0]}')
        print(f'Total terms: {parsing.docs_info[term][1]}')
    else:
        print(f'Listing for term: {term}')
        print(f'TERMID: {parsing.term_id[term][0]}')
        print(f'Number of documents containing term: {parsing.get_num_doc_freq(term)}')
        print(f'Term frequency in corpus: {parsing.term_id[term][1]}')
else:
    d_id = parsing.docs_info[sys.argv[4]][0]
    term = sys.argv[2]
    t_id = parsing.term_id[term][0]
    print(f'Inverted list for term: {term}')
    print(f'In document: {sys.argv[4]}')
    print(f'TERMID: {t_id}')
    print(f'DOCID: {d_id}')
    print(f'Term frequency in document: {parsing.get_term_doc_freq(term, sys.argv[4])}')
    print(f'Positions: {parsing.get_term_pos(term, sys.argv[4])}')
 
parsing.create_term_index()