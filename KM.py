from pynput import keyboard

#Covers ctrl + c for windows and cmd + c for mac
COPY =[
        {keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.KeyCode(char='c')},
        {keyboard.Key.ctrl_r, keyboard.Key.alt_r, keyboard.KeyCode(char='c')},
]



#Input buffer
key_buffer = set()

def press(key):
    print(key)
    #Only add initial key in buffer if it exists in a possible combo!
    if any(key in combo for combo in COPY):
        key_buffer.add(key)
        #If the keystack contains a possible combo from COPY then the combo was found!
        if any(all(k in key_buffer for k in combo) for combo in COPY):
            print('Ctrl+alt+c')

def release(key):
    try:
        key_buffer.remove(key)
    except KeyError:
        pass

#with clause for keyboard listener to be freed after shutdown
with keyboard.Listener(on_press=press, on_release=release) as kb_listen:
    kb_listen.join()


