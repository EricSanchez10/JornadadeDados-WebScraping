import requests

def fetch_page():
    
    response = requests.get(url)
    return response.text

if __name__== "__main__":
    url = "https://lista.mercadolivre.com.br/creatina-growth#trend" 
    page_content = fetch_page()
    print(page_content)
    


