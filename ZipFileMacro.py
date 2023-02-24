import os
from tkinter import filedialog
from zipfile import ZipFile, ZIP_DEFLATED

def compress_all(dir_local):
    namefile = os.listdir(dir_local)

    for name in namefile:
        noextension = name.split('.')[0]
        namezip = os.path.join(dir_local, noextension + '.zip')
        filezip = ZipFile(namezip, 'w', compression=ZIP_DEFLATED)
        filezip.write(os.path.join(dir_local, name), name)
        filezip.close()
    
    return len(namefile)

if __name__ == '__main__':
    # folder = input("Digite o endereço da pasta a ser compactada: ")
    folder = filedialog.askdirectory()
    print(f'Arquivos compactados em {folder}')
    n = compress_all(folder)
    print(f'{n} arquivos compactados com sucesso')