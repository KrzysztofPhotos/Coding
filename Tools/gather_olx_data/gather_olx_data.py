#  -----   INSTRUCTION   ------
# 1. CREATE A .TXT FILE WITH ALL LINKS TO ITEMS FROM OLX (LINE BY LINE WITHOUT ANY SPACES OR EMPTY LINES)
# 2. PUT THE .PY FILE AND TXT FILE IN THE SAME DIRECTORY
# 3. RUN SCRIPT

import os

os.system('cls') # clear console

# Change the current working directory to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
os.chdir(script_dir)  # Change the working directory to that folder
#print(f"Current working directory: {os.getcwd()}")  # Verify the change
# the code above only ensure that we're working in the right catalog

import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm  # Import tqdm for progress bar
from openpyxl import load_workbook
from openpyxl.styles import NamedStyle
from openpyxl.utils.dataframe import dataframe_to_rows

# Define the Excel file name
excel_file = "scraped_data.xlsx"

# Delete the existing file if it exists
if os.path.exists(excel_file):
    os.remove(excel_file)
    print(f"Deleted existing file: {excel_file}")

# Function to read links from a .txt file and remove duplicates
def read_links_from_txt(file_name):
    links = set()  # Use a set to avoid duplicates
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            # Read all lines, strip whitespace, and add to the set
            links = set(line.strip() for line in file.readlines() if line.strip())  # Skip empty lines and whitespace
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    return list(links)  # Convert the set back to a list

# Read the URLs from the 'links.txt' file
urls = read_links_from_txt("links.txt")

# Month names in Polish and their corresponding numbers
months = {
    "stycznia": "01", "lutego": "02", "marca": "03", "kwietnia": "04", 
    "maja": "05", "czerwca": "06", "lipca": "07", "sierpnia": "08", 
    "września": "09", "października": "10", "listopada": "11", "grudnia": "12"
}

# List to store all the extracted data
data = []

# Loop through each URL in the list with tqdm to show progress
for url in tqdm(urls, desc="Processing URLs", unit="url"):
    if not url.startswith("http"):  # Check if the URL is missing a scheme
        print(f"Skipping invalid URL: {url}")
        continue  # Skip invalid URLs
    
    # Send a GET request to the URL
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Raise an error for invalid HTTP status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        continue  # Skip the current URL and move to the next
    
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract the price from h3 class "css-90xrc0"
    price_element = soup.find("h3", class_="css-90xrc0")
    price = price_element.get_text(strip=True) if price_element else "Price not found"
    
    # Remove the "zł" symbol and convert to a number (float)
    if price != "Price not found":
        price = price.replace("zł", "").strip().replace(",", "").replace(" ", "")  # Remove spaces, commas
        try:
            price = float(price)
        except ValueError:
            price = "Invalid price"
    
    # Extract the title from h4 class "css-1kc83jo"
    title_element = soup.find("h4", class_="css-1kc83jo")
    title = title_element.get_text(strip=True) if title_element else "Title not found"
    
    # Extract the ID from span class "css-12hdxwj"
    id_element = soup.find("span", class_="css-12hdxwj")
    ad_id = id_element.get_text(strip=True) if id_element else "ID not found"
    
    # Clean up the ID by removing the "ID:" part but keeping the number
    if ad_id.startswith("ID:"):
        ad_id = ad_id[3:].strip()  # Remove "ID:" and any surrounding spaces
    
    # Extract the description from div class "css-1o924a9"
    description_div = soup.find("div", class_="css-1o924a9")
    
    if description_div:
        # Replace <br> tags with newlines
        for br in description_div.find_all("br"):
            br.replace_with("\n")
        
        # Get the text from the description div
        description_text = description_div.get_text("\n", strip=True)
    else:
        description_text = "Description not found."
    
    # Extract the date of the ad from span class "css-19yf5ek"
    date_element = soup.find("span", class_="css-19yf5ek")
    if date_element:
        date_text = date_element.get_text(strip=True)
        # Split the date and month, and convert the month name to a number
        date_parts = date_text.split(" ")
        if len(date_parts) == 3:
            day = date_parts[0]
            month = date_parts[1]
            year = date_parts[2]
            if month in months:
                month_number = months[month]
                date_converted = f"{day}.{month_number}.{year}"
            else:
                date_converted = "Invalid month"
        else:
            date_converted = "Date format error"
    else:
        date_converted = "Date not found"
    
    # Append the extracted data to the list
    data.append({
        "ID": ad_id,
        "Price": price,
        "Title": title,
        "Date": date_converted,
        "URL": url,
        "Description": description_text
    })

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the data to an Excel file using OpenPyXL for formatting
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Scraped Data')
    workbook = writer.book
    sheet = workbook['Scraped Data']
    
    # Define a currency style
    currency_style = NamedStyle(name="currency_style", number_format='#,##0 "PLN"')
    
    # Apply the currency style to the Price column
    for row in sheet.iter_rows(min_row=2, min_col=2, max_col=2):  # Apply to Price column (2nd column)
        for cell in row:
            cell.style = currency_style

print(f"\033[32mData has been saved to '{excel_file}'\033[0m")