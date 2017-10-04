# fundscraper

[Scrapy](https://scrapy.org/) web crawlers to collect fund data

## Installation

If you have `virtualenvwrapper`, set up a virtual environment with the following command:

````
mkvirtualenv fundscraper
````

Install dependencies:

````
pip install -r requirements.txt
````

Install dev dependencies:

````
python install -r test_requirements.txt
````

## Usage

To crawl utilizing a spider:

````
scrapy crawl aia.com.hk
````

To calculate returns from historic data:

````
python setup.py compute_returns
````

To compute most performant funds:

````
python setup.py compute_performing_funds
````
