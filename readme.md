
##Installation steps for SkyHub Crawler in Python

### install Miniconda
1. https://conda.io/miniconda.html
2. `wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`
3. `bash Miniconda3-latest-Linux-x86_64.sh`
4. Restart terminal

### install other libraries
```
conda create -n crawler3
source activate crawler3
pip install scrapy
pip install dateparser
pip install parsel
pip install requests
pip install ujson
```

Optionals
```
    pip install beautifulsoup4
```

## Running

`python3 main.py`