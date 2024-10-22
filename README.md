**toSaunaOrNotToSauna**

This small project is a Python-based web scraper designed to fetch Finnish electricity prices for the current day and save them into a .csv file. It serves as a practical exercise to learn web scraping and automate tasks using cron scheduling. 

How to use:
The script is designed to be run once a day with Cron or Task Scheduler. Once run a .csv file will be saved to root folder and the earlier file will be removed in the process.

Technologies Used
    Python for scripting and web scraping.
    BeautifulSoup and requests libraries to parse HTML.
    Cron to schedule the scraper to run at regular intervals.
