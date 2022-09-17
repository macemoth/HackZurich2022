import xml.etree.ElementTree as ET
import numpy as np
import os
import pickle
from gensim.test.utils import common_texts, simple_preprocess
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string

data_folder = "data/"

def main():
    documents = import_xml_docs()
    corpus = list(preprocess(documents))
    embed(corpus)

def import_xml_docs(serialise=True):
    documents = []
    len_overall = 0

    content = os.listdir(data_folder)
    files = []
    for file in content:
        if file.split(".")[1] == "xml":
            files.append(file)
    
    print(f"Importing pubmed files. Found {len(files)}")

    for file in files:
        tree = ET.parse(data_folder + file)
        root = tree.getroot()
        len_overall += len(root)
        for sec in root:
            # if len(documents) > 1000:
            #     break
            text = sec.find(".//AbstractText")
            if text != None:
                if text.text != None:
                    if len(text.text) > 5:
                        documents.append(text.text)
    
    print(f"Finished import. Using {len(documents)} of total {len_overall} documents")
    
    if serialise:
        with open(data_folder + "documents.bin", "wb") as file:
            pickle.dump(documents, file)
            file.close()
    return documents


def preprocess(documents, tokens_only=False):
    print("Preprocessing documents")
    for i, doc in enumerate(documents):
        tokens = simple_preprocess(doc)
        if tokens_only:
            yield tokens
        else:
            # For training data, add tags
            yield TaggedDocument(tokens, [i])

def embed(corpus, vector_size=800, window=20, dm=1, min_count=2, epochs=50, workers=1, serialise=True):
    print("Embedding documents")
    model = Doc2Vec(vector_size=vector_size, window=window, dm=1, min_count=min_count, epochs=epochs, workers=workers)
    model.build_vocab(corpus)
    model.train(corpus, total_examples=model.corpus_count, epochs=model.epochs)
    print("Embedding documents done")
    if serialise:
        model.save(data_folder + "embedding.bin")


if __name__ == "__main__":
    main()