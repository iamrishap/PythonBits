# Import Libraries and Modules here...
# Written by Pratik Sharma
# z5199295

from spacy import load
from itertools import permutations
from math import log


class InvertedIndex:
    def __init__(self):
        # You should use these variable to store the term frequencies for tokens and entities...
        self.tf_tokens = {}
        self.tf_entities = {}

        # You should use these variable to store the inverse document frequencies for tokens and entities...
        self.idf_tokens = {}
        self.idf_entities = {}

    # Your implementation for indexing the documents...
    def index_documents(self, documents):
        nlp = load("en_core_web_sm")

        for key in documents.keys():
            doc = nlp(documents[key])

            for entity in doc.ents:
                if entity.text not in self.tf_entities:
                    self.tf_entities[entity.text] = {key: documents[key].count(entity.text)}
                else:
                    self.tf_entities[entity.text].update({key: documents[key].count(entity.text)})

            for token in doc:
                if token.text in self.tf_entities:
                    continue
                if not token.is_stop and not token.is_punct:
                    if token.text not in self.tf_tokens:
                        self.tf_tokens[token.text] = {key: documents[key].count(token.text)}
                    else:
                        self.tf_tokens[token.text].update({key: documents[key].count(token.text)})

        num_of_docs = len(documents)

        for token in self.tf_tokens:
            self.idf_tokens[token] = 1.0 + log(num_of_docs / (1.0 + len(self.tf_tokens[token])))

        for entity in self.tf_entities:
            self.idf_entities[entity] = 1.0 + log(num_of_docs / (1.0 + len(self.tf_entities[entity])))

    # Your implementation to split the query to tokens and entities...
    def split_query(self, Q, DoE):

        query_splits = {1: {'tokens': Q.split(' '), 'entities': []}}

        key = 1
        entities = []
        for i in range(1, (len(DoE) + 1)):
            entities += list(permutations(DoE, i))
        # print(entities)

        query = Q
        skip = False

        for entity in entities:
            t = []
            for word in entity:
                for w in word.split(' '):
                    if w in query:
                        query = query[query.index(w) + len(w) + 1:]
                        t.append(w)
                    else:
                        skip = True
                        break
                if skip:
                    break
            if not skip:
                ent = [x for x in entity]
                tok = query_splits[1]['tokens'].copy()
                for x in t:
                    tok.remove(x)
                query_splits.update({len(query_splits) + 1: {'tokens': tok,
                                                             "entities": ent
                                                             }
                                     })
            query = Q
            skip = False

        return query_splits

    # Your implementation to return the max score among all the query splits...
    def max_score_query(self, query_splits, doc_id):
        max_score = 0
        id = 0
        for key, splits in query_splits.items():
            si1 = 0.0
            si2 = 0.0
            for entity in splits['entities']:
                if entity in self.tf_entities and entity in self.idf_entities and doc_id in self.tf_entities[entity]:
                    si1 += (1.0 + log(self.tf_entities[entity][doc_id])) * self.idf_entities[entity]

            for token in splits['tokens']:
                if token in self.tf_tokens and token in self.idf_tokens and doc_id in self.tf_tokens[token]:
                    si2 += (1.0 + log(1.0 + log(self.tf_tokens[token][doc_id]))) * self.idf_tokens[token]

            combined_score = si1 + (0.4 * si2)
            if combined_score > max_score:
                max_score = combined_score
                id = key

        return (max_score, query_splits[id])
        # Output should be a tuple (max_score, {'tokens': [...], 'entities': [...]})


# print("index.tf_tokens:")
# print(index.tf_tokens)
#
# print("\n index.tf_entities:")
# print(index.tf_entities)


# Test Case 1 (Toy Example)
documents = {1: 'President Trump was on his way to new New York in New York City.',
             2: 'New York Times mentioned an interesting story about Trump.',
             3: 'I think it would be great if I can travel to New York this summer to see Trump.'}
index = InvertedIndex()
index.index_documents(documents)
Q = 'New York Times Trump travel'
DoE = {'New York Times': 0, 'New York': 1, 'New York City': 2}
query_splits = index.split_query(Q, DoE)
doc_id = 3

# Test Case 2 (Test Case-1)
documents = {
    1: 'According to Times of India, President Donald Trump was on his way to New York City after his address at UNGA.',
    2: 'The New York Times mentioned an interesting story about Trump.',
    3: 'I think it would be great if I can travel to New York this summer to see Trump.'}
index = InvertedIndex()
index.index_documents(documents)
Q = 'The New New York City Times of India'
DoE = {'Times of India': 0, 'The New York Times': 1, 'New York City': 2}
query_splits = index.split_query(Q, DoE)
doc_id = 1

# Test Case 3 (Test Case-2)
# documents = {1: 'According to Los Angeles Times, The Boston Globe will be experiencing another recession in 2020.
# However, The Boston Globe decales it a hoax.',
#             2: 'The Washington Post declines the shares of George Washington.',
#             3: 'According to Los Angeles Times, the UNSW COMP6714 students should be able
#             to finish project part-1 now.'}
# index = InvertedIndex()
# index.index_documents(documents)
# Q = 'Los The Angeles Boston Times Globe Washington Post'
# DoE = {'Los Angeles Times':0, 'The Boston Globe':1,'The Washington Post':2, 'Star Tribune':3}
# query_splits = index.split_query(Q, DoE)
# doc_id = 1


# Test Case 4
# documents = {1:'President Trump was on his way to new New York in New York City.',
#             2:'New York Times mentioned an interesting story about Trump.',
#             3:'I think it would be great if I can travel to New York this summer to see Trump.'}
# index = InvertedIndex()
# index.index_documents(documents)
# Q = 'The New New York City The Times of India'
# DoE = {'The Times of India':0, 'The New York Times':1,'New York City':2, 'The New':3}
# query_splits = index.split_query(Q, DoE)
# doc_id=3


result = index.max_score_query(query_splits, doc_id)
print('The maximum score:')
print(result)
