import pyautogui


def click_accept_button():
    
    print('Procurando por botão.')
    
    accept_button_location = None

    while True:
        try:
            # while accept_button_location is None:
            accept_button_location = pyautogui.locateOnScreen('aceitar.png', confidence=0.7)
            accept_button_center = pyautogui.center(accept_button_location)
            
            pyautogui.click(accept_button_center)
            print('Partida Aceitada! Executando...')
        except pyautogui.ImageNotFoundException:
            print('Botao nao encontrando, tentando novamente...')
            pass
    
        pyautogui.sleep(0.5)
        
if __name__ == "__main__":
    click_accept_button()