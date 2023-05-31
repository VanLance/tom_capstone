import requests

def fetch_recipes():
    api_key = '962c05fa68eb23f43004c092830548c4189e5bb2'
    api_url = 'https://suggestic.com/api.html?apiKey={api_key}'

    try:
        response = requests.get(api_url, param={'apikey': api_key})
        data= response.json()
        return data['recipes']
    except requests.exceptions.RequestException as error:
        print('Error fetching recipes:', error)
        return []
    
recipes = fetch_recipes()
print(recipes)

# Use the request to make a GET request to the API endpoint.
# d8223141-ffbe-40ca-98c2-8598b80dba77 as the user-ID 
