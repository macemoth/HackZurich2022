import gensim # TODO: define exact libraries

class Search():

    def __init__(self):
        self.load_embedding(filepath="../embeddings.pb")

    def load_embedding(self, filepath):
        pass
        # TODO

    def search(self, params):
        pass
        # TODO e.g. results = gensim.similarity(params)