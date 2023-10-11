import requests

# Defina sua chave de API e token de acesso (substitua pelos seus valores reais)
API_KEY = "YOUR_TOKEN"
ACCESS_TOKEN = "YOU_ACESS_TOKEN"

# Defina os critérios de pesquisa
QUERY = "programador"
LOCATION = "São Paulo"

# URL da API de Anúncios do LinkedIn
URL = "https://api.linkedin.com/v2/adAnalyticsV2?q=JOB_POSTING&pivot=JOB_POSTING&timeGranularity=DAILY&startDate=2022-02-01&endDate=2022-02-10&fields=JOB_POSTING"

# Cabeçalhos da solicitação
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0"
}

# Parâmetros de consulta
params = {
    "q": f"{QUERY} {LOCATION}",
    "eventType": "JOB_DETAIL_VIEW",
    "pivot": "JOB_POSTING",
    "count": 10  # Quantidade de resultados desejados
}

# Realize a pesquisa
response = requests.get(URL, headers=headers, params=params)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    # Processar e imprimir os resultados
    for result in data["elements"]:
        job_title = result["jobPosting"]["title"]
        job_description = result["jobPosting"]["description"]
        job_location = result["jobPosting"]["locationName"]
        job_salary = result["jobPosting"]["baseSalary"]["value"]["amount"]
        print(f"Title: {job_title}")
        print(f"Description: {job_description}")
        print(f"Location: {job_location}")
        print(f"Salary: {job_salary}")
else:
    print(f"Erro: {response.status_code} - {response.text}")
