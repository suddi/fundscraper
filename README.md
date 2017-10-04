# fundscraper

[![CircleCI](https://img.shields.io/circleci/project/suddi/fundscraper/master.svg)](https://circleci.com/gh/suddi/fundscraper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4aaafdcb86574c709f856f2e00d3a809)](https://www.codacy.com/app/Suddi/fundscraper)
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
