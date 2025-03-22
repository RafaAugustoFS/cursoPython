import requests #Responsavel por enviar a requisição
from bs4 import BeautifulSoup # Responsavel por tratar a requisição



url = "https://identidadecorinthiana.com"

headers = {
    "User-agent" : "Mozilla/5.0(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# fazendo requisição HTTP
resposta = requests.get(url, headers=headers)


if resposta.status_code == 200:
    # codigo 200 -> sucesso
    print("Requisição feita com sucesso")
   # print(resposta.text) # retorno


    soup = BeautifulSoup(resposta.text, "html.parser")


    # encontrando as noticias
    noticias = soup.find_all("a", class_="eael-grid-post-link")


    print("Ultimas noticias da IDC:")
    print(noticias)
    for index, artigo in enumerate(noticias):
            titulo = artigo.text.strip()
            if titulo:
                print(f"{index + 1}. {titulo}")
            else:
                print(f"{index + 1}. Título não encontrado")
else:
    print("Não rodou")
    print(resposta.status_code)