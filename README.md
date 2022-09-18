# HackZurich2022: zipdoc

## Installation and usage

1. Run `pip3 -r requirements.txt`
2. Download PubMed XML files from this [URL](https://www.nlm.nih.gov/databases/download/pubmed_medline.html) and place them into `data`
3. Run `python3 embedding.py`. The embedding along with the documents are serialized (this may take a long time)
4. Run HTTP endpoint using `flask -A server run`
5. Access zipdoc as [http://127.0.0.1:5000](http://127.0.0.1:5000)
