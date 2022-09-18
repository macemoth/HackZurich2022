# HackZurich2022: zipdoc

## Installation and usage

1. Run `pip3 -r requirements.txt`
2. Download PubMed XML files from this [URL](https://www.nlm.nih.gov/databases/download/pubmed_medline.html) and place them into `embedding/data`
3. `cd` into `embedding` and run `python3 embedding.py`. The embedding along with the documents are serialized
4. `cd` into `frontend` and run HTTP endpoint using `flask -A server run`
5. Access zipdoc as [http://127.0.0.1:5000](http://127.0.0.1:5000)