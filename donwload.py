import requests
import os
from tkinter import filedialog
from tqdm import tqdm

# selecionar o arquivo e o diretório
if __name__ == '__main__':
    dir_txt = filedialog.askopenfile().name
    dir_destination = filedialog.askdirectory()

# ler as urls no arquivo txt
with open(dir_txt, 'r') as f:
    urls = f.readlines()

# remove os espaços em branco e caracteres de nova linha das URLs
urls = [url.strip() for url in urls]

# Faz o download dos arquivos um por um
for url in tqdm(urls):
    # Define o caminho completo do arquivo de destino
    file_name = os.path.basename(url)
    file_path = os.path.join(dir_destination, file_name)

    # Faz o dowload do arquivo
    response = requests.get(url)

    # Grava o conteudo no disco
    with open(file_path, 'wb') as f:
        f.write(response.content)

print('Download Completo!')