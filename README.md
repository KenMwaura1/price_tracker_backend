# Price Tracker Backend 
A Django api to display items and their current up-to-date prices from different online retailers in one platform.
Utilizing scrapy to periodically scrape the latest prices from different online retailers. Store in a PostgreSQL database and 
make available via an API. 


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### **Note**: This project is a work in progress.

## Setup Instructions / Installation

### Getting Started

### Prerequisites

- Python and pip (I am currently using 3.9.7) Any version above 3.7 should work.
* Git installed on your machine
* Code editor/ IDE
* PostgreSQL installed on your machine

### Installation and Running the App

1. Clone GitHub repository

    ```shell
    git clone 
    ```

2. Change into the folder

    ```shell
   cd price_tracker_backend
    ```

3. Create a virtual environment

   ```shell
      python3 -m venv venv 
   ```

    * Activate the virtual environment

   ```shell
   source ./bin/activate
   ```

* If you are using [pyenv](https://github.com/pyenv/pyenv):

  3a. Create a virtualenv

   ```
       pyenv virtualenv price_tracker_backend
   ```

  3b. Activate the virtualenv

   ```
   pyenv activate price_tracker_backend
   ```

4. Create a `.env` file and add your credentials

   ```
   touch .env 
   ```

   OR Copy the included example

    ```
    cp .env-example .env 
    ```
5. Create a PostgreSQL Database 

    ```
    psql -U postgres
    ```

    * Create a database

    ```
    CREATE DATABASE price_tracker_db;
    ```

    * Create a user

    ```
    CREATE USER price_tracker_user WITH PASSWORD 'password';
    ```

    * Grant privileges to the user

    ```
    GRANT ALL PRIVILEGES ON DATABASE price_tracker_db TO price_tracker_user;
    ```

    * Exit the psql session

    ```
    \q
    ```

6. Add your credentials to the `.env` file

    5a. export db credentials to your environment variables
    
    ```
    export DATABASE_URL=postgres://user:password@localhost:5432/price_tracker
    ```
   

6. Migrate your database
    ```shell
    python manage.py migrate
    ```

7. Install the required dependencies

   ```shell
   pip install -r requirements.txt
   ```

8. Make the shell script executable

    ```shell
   chmod a+x ./run.sh
    ```

9. Run the app

    ```shell
   ./run.sh
    ```
   app should be available on [http://127.0.0.1:8081/](http://127.0.0.1:8081/
)


   OR
   run with python

```shell
   python manage.py runserver
   ```
### To run the scrapy spider
```shell
    cd price_scraper 
    scrapy crawl jumia_spider
   ```
### To Run Scrapd and use a web interface
```shell
    cd price_scraper 
    scrapyd
   ```

### To run ScrapyRT and get a real time API
```shell
    cd price_scraper 
    scrapyrt
   ```
* Test out the api: 
    ```shell
          curl "http://localhost:9080/crawl.json?spider_name=jumia_spider&url=https://jumia.co.ke/"
    ```
    

## Technologies used

* Python-3.9.7
* Django web framework
* PostgreSQL
* Scrapy
