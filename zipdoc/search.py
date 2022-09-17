from evaluator import Evaluator

class Search():

    def __init__(self):
        self.evaluator = Evaluator()
        self.pubmedPrefix = "https://pubmed.ncbi.nlm.nih.gov/"

    def search(self, params):
        hits = self.evaluator.most_similar(params, n=3)

        if len(hits) == 0:
            pass
            # TODO: Implement error handling
        
        similars = ["cardial", "cranial", "dope"]
        return hits, similars

if __name__ == "__main__":
    search = Search()
    print(search.search("influenza corona heart"))
