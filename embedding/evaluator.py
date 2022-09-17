from gensim.utils import simple_preprocess
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import xml.etree.ElementTree as ET
import os
import pickle

class Evaluator():

    def __init__(self):
        documents_file = "data/documents.bin"
        model_file = "data/embedding.bin"
        self.model = Doc2Vec.load(model_file)
        with open(documents_file, "rb") as file:
            self.documents = pickle.load(file)
        print(len(self.documents))

    def most_similar(self, text, n=2):
        processed_query = simple_preprocess(text)
        v1 = self.model.infer_vector(processed_query)
        similar_doc = self.model.dv.most_similar([v1], topn=n)
        print("similar_doc", similar_doc)
        hits = []
        for i in range(len(similar_doc)):
            print()
            hits.append(self.documents[similar_doc[i][0]])
        return hits

    def most_similar_debug(self, text):
        processed_query = simple_preprocess(text)
        v1 = self.model.infer_vector(processed_query)
        similar_doc = self.model.docvecs.most_similar([v1])
        return similar_doc

if __name__ == "__main__":
    evaluator = Evaluator()
    query = "cancer leukemia malignant"
    print(evaluator.most_similar(query))