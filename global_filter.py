# Import necessary libraries
import requests

# Define the URL of the configuration file
url = "https://ruleset.skk.moe/List/non_ip/global.conf"

# Define the local file path to save the configuration file
local_file = "global.conf"

# Download the configuration file
response = requests.get(url)

# Save the downloaded content to the local file
with open(local_file, "w", encoding="utf-8") as file:
    file.write(response.text)

# Read the file and filter out the line that contains 'DOMAIN-SUFFIX,pikpak.me'
with open(local_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Filter out the line containing the specific rule
filtered_lines = [line for line in lines if "DOMAIN-SUFFIX,pikpak.me" not in line]

# Write the filtered content back to the file
with open(local_file, "w", encoding="utf-8") as file:
    file.writelines(filtered_lines)
