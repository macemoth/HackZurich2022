from evaluator import Evaluator
from summarizer import Summarizer

class Search():

    def __init__(self):
        self.evaluator = Evaluator()
        self.summarizer = Summarizer()
        self.pubmedPrefix = "https://pubmed.ncbi.nlm.nih.gov/"

    def search(self, params):
        hits = self.evaluator.most_similar(params, n=10)
        n_summaries=3

        if len(hits) == 0:
            pass
            # TODO: Implement error handling
        
        sure_hits = []
        for hit in hits:
            if len(hit[3]) > 500:
                sure_hits.append(hit)

        summaries = []

        for i in range(min(n_summaries, len(sure_hits))):
            summary = self.summarizer.summarize(hits[i][3])
            summaries.append((self.pubmedPrefix + str(hits[i][0]), summary))

        similars = self.evaluator.get_similars(params, n=5)
        return hits, summaries, similars

if __name__ == "__main__":
    search = Search()
    print(search.search("influenza corona heart"))
