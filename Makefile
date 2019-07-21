start:
	docker run --rm -v "${PWD}:/scraper" -it python:2 bash

run:
	scrapy runspider /scraper/scraper.py -o /scraper/output.json

clean:
	rm /scraper/output.json

