apt update
apt install -y vim jq
pip install scrapy
scrapy runspider /scraper/scraper.py -o /scraper/article.json

