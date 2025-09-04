clear
pacman -S --no-confirm python python-pip git
pip install bs4 requests
git clone https://github.com/pironha2/planoz-odziej/
cd /planoz-odziej
python knsrefresh.py
