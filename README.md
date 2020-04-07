# fundscraper

[![CircleCI](https://circleci.com/gh/suddi/fundscraper.svg?style=svg)](https://circleci.com/gh/suddi/fundscraper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d43e89675ba64685ad3635b884bf4957)](https://www.codacy.com/app/Suddi/fundscraper)
[![license](https://img.shields.io/github/license/suddi/fundscraper.svg)](https://github.com/suddi/fundscraper/blob/master/LICENSE)

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
