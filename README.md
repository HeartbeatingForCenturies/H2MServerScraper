# H2M Server Scraper

This script is designed to fetch a list of game servers specifically for the H2M-Mod from the URL `https://master.iw4.zip/servers`. It extracts server information, including IP addresses and ports, and saves it into the favourites.json file.
so you can seamlessly join lobbies through the server browser

## Features

- Fetches H2M game server list from `https://master.iw4.zip/servers`.
- Extracts IP addresses and ports of game servers.
- Saves the server list to a specified JSON file.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the Repository**

   ```sh
   pip install requests beautifulsoup4
   git clone [https://github.com/yourusername/server-list-scraper](https://github.com/HeartbeatingForCenturies/H2MServerScraper).git
   cd H2MServerScraper
   py H2MServerScraper.py
