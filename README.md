# xdze2.github.io-src
source for the website


## Install ubuntu

```bash
sudo apt-get install virtualenv
virtualenv -p /usr/bin/python3 py3

source ./py3/bin/activate

pip install jupyter
pip install matplotlib
pip install pelican
pip install Markdown
pip install scipy numpy

```
or
```bash
pip install -r requirements.txt 
```


then

```bash
make devserver
firefox http://0.0.0.0:8000/
```


