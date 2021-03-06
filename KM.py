from pynput import keyboard
from PyQt5.Qt import QApplication
import threading
import time

class KM(threading.Thread):
    def __init__(self, master):
        threading.Thread.__init__(self)
        self.master = master
        #Covers keybind for scrolling through clipboard history
        self.SCROLL =[
                {keyboard.Key.ctrl_l, keyboard.Key.shift_l, keyboard.KeyCode(char='z')},
                {keyboard.Key.ctrl_r, keyboard.Key.shift_r, keyboard.KeyCode(char='z')},
                {keyboard.Key.cmd_l, keyboard.Key.shift_l, keyboard.KeyCode(char='z')},
                {keyboard.Key.cmd_r, keyboard.Key.shift_r, keyboard.KeyCode(char='z')},
        ]
        # Covers ctrl + c for windows and cmd + c for mac
        self.COPY = [
            {keyboard.Key.ctrl_l, keyboard.KeyCode(char='c')},
            {keyboard.Key.ctrl_r, keyboard.KeyCode(char='c')},
            {keyboard.Key.cmd_l, keyboard.KeyCode(char='c')},
            {keyboard.Key.cmd_r, keyboard.KeyCode(char='c')},
        ]
        #Input buffer
        self.key_buffer = set()
        #Start key listener thread
        self.start()

    def run(self):
        self.scroll_counter = 0
        # with clause for keyboard listener to be freed after shutdown
        with keyboard.Listener(on_press=self.press, on_release=self.release) as self.kb_listen:
            self.kb_listen.join()

    def stop(self):
        self.kb_listen.stop()

    def press(self, key):
        if self.check_kb(key, self.SCROLL):
            #Only scroll through bounds of data
            if self.scroll_counter < len(self.master.getData()):
                index = len(self.master.getData()) - 1 - self.scroll_counter
                dat = self.master.getData()
                # Clip content is index 1 of tuple
                clip = self.master.getData()[index][1]
                self.master.copy(clip)
                self.scroll_counter += 1
        elif self.check_kb(key, self.COPY):
            #Sleep timer so we can grab the text after os inserted into clipboard
            time.sleep(0.1)
            self.master.insert_clip((QApplication.clipboard().text()))

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
                self.scroll_counter = 0
        except KeyError:
            pass



