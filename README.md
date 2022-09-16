# HackZurich2022

## Installation

*TODO:* Download, preprocessing and embedding of publication data

1. Run `pip3 -r requirements.txt``
2. Download Google's Pegasus file from [here](https://console.cloud.google.com/storage/browser/pegasus_ckpt/pubmed?pageState=(%22StorageObjectListTable%22:(%22f%22:%22%255B%255D%22))&prefix=&forceOnObjectsSortingFiltering=false)
3. Import the pretrained Pegasus model using

```bash
python pegasus/flax/main.py \
    --config pegasus/flax/configs/examples/summscreen_eval.py \
    --workdir path/to/fine_tuning_output
```

4. `cd` into `frontend` and run HTTP endpoint using `flask -A server run`