import pyautogui


def shift_tab(presses):
    """this function presses the combination of keys "shift + tab" in a determined times""" 
    for i in range(presses):
        pyautogui.hotkey("shift", "tab")
        print("pressing key...")
    
    return print(f"The combination of 'shift' + 'tab' has been pressed {presses} times succesfully!")
   

l = shift_tab(2)