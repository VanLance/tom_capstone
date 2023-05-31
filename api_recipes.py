import requests

def fetch_recipes():
    api_key = '962c05fa68eb23f43004c092830548c4189e5bb2'
    api_url = 'https://suggestic.com/api.html?creative=518345329904&keyword=recipe%20api&matchtype=p&network=g&device=c&utm_feeditemid=&utm_device=c&utm_term=recipe%20api&utm_source=google&utm_medium=ppc&utm_campaign=Food+API&hsa_cam=12911761359&hsa_grp=128492773624&hsa_mt=p&hsa_src=g&hsa_ad=518345329904&hsa_acc=4758559608&hsa_net=adwords&hsa_kw=recipe%20api&hsa_tgt=kwd-431070768166&hsa_ver=3&gclid=EAIaIQobChMInbnk68Se_wIV2FdyCh2edQuPEAAYASAAEgIgs_D_BwE'

    try:
        response = requests.get(api_url, param={'apikey': api_key})
        data= response.json()
        return data['recipes']
    except requests.exceptions.RequestException as error:
        print('Error fetching recipes:', error)
        return []
    
recipes = fetch_recipes()
print(recipes)
