import win32gui
import win32api
import win32con
from time import sleep
def get_window_text_and_rect(hwnd):
    text = win32gui.GetWindowText(hwnd)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return text, (left, top, right - left, bottom - top)

def inspect_desktop_field():
    print("Pressione e segure a tecla 'Ctrl' para começar a inspecionar o campo.")

    while True:
        if win32api.GetAsyncKeyState(win32con.VK_CONTROL) & 0x8000:
            print("Tecla Ctrl pressionada")
            hwnd = win32gui.GetForegroundWindow()
            text, rect = get_window_text_and_rect(hwnd)
            print(f"Janela: {text}")
            print(f"Posição: {rect}")

            # Obtem as coordenadas do mouse
            mouse_x, mouse_y = win32api.GetCursorPos()
            print(f"Posição do mouse: ({mouse_x}, {mouse_y})")
            sleep(2)
            if win32api.GetAsyncKeyState(win32con.VK_CONTROL) == 0:
                print("Tecla Ctrl solta")
                break
        else:
            continue

    print("Modo de inspeção encerrado.")

inspect_desktop_field()