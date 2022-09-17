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
            title = sec.find(".//ArticleTitle")
            if title == None:
                continue

            if title.text == None:
                continue

            title = title.text.replace("[", "").replace("]", "")

            pmid = sec.find(".//PMID").text
            authors = extractAuthors(sec.findall(".//Author"))

            text = sec.find(".//AbstractText")
            if text == None:
                continue
                
            if text.text == None:
                continue
                
            documents.append((pmid, title, authors, text.text))
    
    print(f"Finished import. Using {len(documents)} of total {len_overall} documents")
    
    if serialise:
        with open(data_folder + "documents.bin", "wb") as file:
            pickle.dump(documents, file)
            file.close()
    return documents


def preprocess(documents, tokens_only=False):
    print("Preprocessing documents")
    for i, doc in enumerate(documents):
        tokens = simple_preprocess(doc[3])
        if tokens_only:
            yield tokens
        else:
            # For training data, add tags
            yield TaggedDocument(tokens, [i])

def embed(corpus, vector_size=68, window=5, dm=2, min_count=1, epochs=200, workers=10, serialise=True, dbow_words=1, sample=0, hs=0):
    print("Embedding documents")
    model = Doc2Vec(dm=dm, vector_size=vector_size, window=window, hs=hs, min_count=min_count,
                    epochs=epochs, dbow_words=dbow_words, sample=sample, workers=workers)
    model.build_vocab(corpus)
    model.train(corpus, total_examples=model.corpus_count, epochs=model.epochs)
    print("Embedding documents done")
    if serialise:
        model.save(data_folder + "embedding.bin")
        print(f"Serialised documents to {data_folder}/embedding.bin")

def extractAuthors(authorElement):
    if authorElement == None:
        return " "
    
    if len(authorElement) == 0:
        return " "
    
    authorNames = []
    for author in authorElement:
        initials = author.find(".//Initials")
        lastName = author.find(".//LastName")
        if author == None or initials == None or lastName == None:
            authorName = ""
            continue

        authorName = initials.text
        authorName += ". "
        authorName += lastName.text
        authorNames.append(authorName)
        authorNames.append(", ")
    return "".join(authorNames[:-1])

if __name__ == "__main__":
    main()