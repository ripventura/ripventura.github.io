import requests
import urllib.request
import json

def load_json_from_url(url):
	try:
		print(url)
		response = requests.get(url, timeout=2)
		if response.status_code == 200:
			return response.json()
		else:
			print(f"Error: Unable to fetch data. Status code: {response.status_code}")
			print(response.json())
	except Exception as e:
		print(f"Error: {e}")

def load_migration_entries():
	all_data = []
	page_number = 1
	
	while True:
		try:
			url = f"https://api.scryfall.com/migrations?page={page_number}"
			
			json_response = load_json_from_url(url)
			
			filtered_data = [entry for entry in json_response["data"] if entry["migration_strategy"] == "merge"]
			
			all_data.extend(filtered_data)
		
			if not json_response["has_more"]:
				desired_properties = ['old_scryfall_id', 'new_scryfall_id', 'uri']
				
				return [{key: item[key] for key in desired_properties} for item in all_data]
			else:
				page_number += 1
		except Exception as e:
			print(f"Error: {e}")
			break

migration = load_migration_entries()

print(migration)