# importing time and threading
import time
import threading
# from pynput import mouse
from pynput.keyboard import Listener, Controller, Key
# pynput.keyboard is used to watch events of 
# keyboard for start and stop of auto-clicker
# from pynput.keyboard import KeyCode
  
  
# four variables are created to 
# control the auto-clicker
delay = 1
stop_key = '='
trigger_key_1 = 's'
trigger_key_2 = Key.f7
# threading.Thread is used 
# to control clicks
class SpamButton(threading.Thread):
    
  # delay and button is passed in class 
  # to check execution of auto-clicker
    def __init__(self, delay, key):
        super(SpamButton, self).__init__()
        self.key = key
        self.delay = delay
        self.running = False
        self.program_running = True
  
    def start_clicking(self):
        self.running = True
  
    def stop_clicking(self):
        self.running = False
  
    def exit(self):
        self.stop_clicking()
        self.program_running = False
  
    # method to check and run loop until 
    # it is true another loop will check 
    # if it is set to true or not, 
    # for mouse click it set to button 
    # and delay.
    def run(self):
        while self.program_running:
            while self.running:
                keyboard.press(self.key)
                keyboard.release(self.key)
                time.sleep(self.delay)
            time.sleep(0.1)
  
  
# instance of mouse controller is created
keyboard = Controller()
click_thread_1 = SpamButton(delay, 's')
click_thread_1.start()

click_thread_2 = SpamButton(delay, Key.f7)
click_thread_2.start()
 
# on_click method takes 
# key as argument
def on_press(key):
    print(key)
    print(type(key))
    print(key == stop_key)
  # start_stop_key will stop clicking 
  # if running flag is set to true
    if 'char' in dir(key):
        key = key.char

    if key == trigger_key_1:
        if click_thread_1.running:
            click_thread_1.stop_clicking()
        else:
            click_thread_1.start_clicking()
    if key == trigger_key_2:
        if click_thread_2.running:
            click_thread_2.stop_clicking()
        else:
            click_thread_2.start_clicking()   
    # here exit method is called and when 
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        print('stop')
        click_thread_1.exit()
        click_thread_2.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()