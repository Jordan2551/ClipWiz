from pynput import keyboard
from PyQt5.Qt import QApplication
import DB
import pyperclip
import threading

class KM(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        #Covers keybind for scrolling through clipboard history
        self.SCROLL =[
                {keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.KeyCode(char='c')},
                {keyboard.Key.ctrl_r, keyboard.Key.alt_r, keyboard.KeyCode(char='c')},
        ]
        # Covers ctrl + c for windows and cmd + c for mac
        self.COPY = [
            {keyboard.Key.ctrl_l, keyboard.KeyCode(char='c')},
            {keyboard.Key.ctrl_r, keyboard.KeyCode(char='c')},
        ]
        #Input buffer
        self.key_buffer = set()
        #Start key listener thread
        self.start()

    def run(self):
        self.scroll_counter = 1
        # with clause for keyboard listener to be freed after shutdown
        with keyboard.Listener(on_press=self.press, on_release=self.release) as kb_listen:
            kb_listen.join()

    def press(self, key):
        print(key)
        QApplication.clipboard().setText("Hello")
        if self.check_kb(key, self.SCROLL):
            print('Scroll keybind!')
            #Only scroll through bounds of data
            print(len(DB.data))
            if self.scroll_counter < len(DB.data):
                index = len(DB.data) - 1 - self.scroll_counter
                # Clip content is index 1 of tuple
                clip = DB.data[index][1]
                pyperclip.copy(clip)
                self.scroll_counter += 1

        elif self.check_kb(key, self.COPY):
            print('Copy keybind!')
            DB.insert_clip(QApplication.clipboard().text())

    def check_kb(self, key, kb):
        #Only add initial key in buffer if it exists in a possible combo!
        if any(key in combo for combo in kb):
            self.key_buffer.add(key)
            # If the keystack contains a possible combo from bind then the combo was found!
            if any(all(k in self.key_buffer for k in combo) for combo in kb):
                return True

    def release(self, key):
        try:
            #Note: every time a key is released it is removed from buffer!
            self.key_buffer.remove(key)
            #Only reset the scroll counter when the key buffer is empty!
            #Otherwise it will reset after a single key is released
            if len(self.key_buffer) == 0:
                self.scroll_counter = 1
        except KeyError:
            pass



