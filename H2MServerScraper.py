import requests
from bs4 import BeautifulSoup
import json
import os

# URL to fetch server data from
API_LINK = "https://master.iw4.zip/servers"
# File path to save the JSON data
FILE_PATH = r"U:\SteamLibrary\steamapps\common\Call of Duty Modern Warfare Remastered\players2\favourites.json"

def fetch_server_list(api_link):
    try:
        response = requests.get(api_link)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print("Fetching from server list.")
        
        # Print out the first 500 characters of the HTML content for inspection
        print(response.text[:500])
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        server_list = []

        # Find the div with id 'H2M_servers'
        h2m_servers = soup.find(id="H2M_servers")
        if not h2m_servers:
            raise ValueError("No 'H2M_servers' section found in the HTML.")
        
        # Find all rows within the div
        rows = h2m_servers.find_all('tr', class_='server-row')

        for row in rows:
            ip = ""
            port = ""

            # Extract IP and port from attributes
            ip_tag = row.get('data-ip')
            port_tag = row.get('data-port')
            if ip_tag:
                ip = ip_tag.strip()
            if port_tag:
                port = port_tag.strip()

            if ip and port:
                server_list.append(f"{ip}:{port}")

        return server_list

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
    except ValueError as e:
        print(f"Error processing HTML: {e}")
        return []

def save_to_json(data, file_path):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Storing server list into \"{file_path}\"")
    except Exception as e:
        print(f"Error writing to file: {e}")

def main():
    server_list = fetch_server_list(API_LINK)
    
    if server_list:
        print("List of fetched servers:")
        for server in server_list:
            print(server)
        
        print("Serializing server list into JSON format.")
        save_to_json(server_list, FILE_PATH)
    else:
        print("No servers found or failed to fetch data.")

    print("Operation Complete. Press Enter to exit.")
    input()

if __name__ == "__main__":
    main()
