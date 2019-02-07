# Movie_Details_Scraper
The python script helps in scraping details of 300 movies off the OmdB Website.The Details are then stored in a MongoDB Atlas Cluster.The Script Scrapes the Name of the Movie,Overview Section and Link of the Display Image.Further Changes can be done by changing the script.

## Running the Script
Open you terminal and copy the below instructions
```terminal
$git clone https://github.com/avinsit123/Movie_Details_Scraper.git
$cd Movie_Details_Scraper
$mkdir ~/virtualenvironment
$source activate
$python ScraperBot.py
```
Wait till all 300 files are stored in the Atlas Cluster.

## Directory Structure
```terminal
.
├── LICENSE
├── README.md
├── ScraperBot.py
├── imdbid.csv
└── movie_details.json
```

## Important Details
movie_details.json is the collections file of the entire movie_details database .
