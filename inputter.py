from pynput.keyboard import Listener, Key, Controller as KeyController
from time import sleep
from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()
keyboard = KeyController()
sleep(2)
for i in range(1):
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.2)
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    sleep(0.2)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    sleep(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    sleep(2)
    #mouse.press(Button.left)
    #mouse.release(Button.left)
    sleep(1)

'''
# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))
'''
'''# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))
'''
'''
# Move pointer relative to current position
mouse.move(5, -5)
'''
# Press and release

# Double click; this is different from pressing and releasing
# twice on macOS
'''
mouse.click(Button.left, 2)
# Scroll two steps down
mouse.scroll(0, 2)
#time.sleep(3)
'''

'''
message="Spam"
for i in range(30):
    keyboard.type('Spam')
    print("Sending message",i)
    time.sleep(1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
'''
# Press and release space

# Type a lower case A; this will work even if no key on the
# physical keyboard is labelled 'A'
'''
with keyboard.pressed(Key.shift):
    keyboard.press('a')
    keyboard.release('a')
'''
"""
# Type 'Hello World' using the shortcut type method
def on_press(key):
    print("Key pressed: {0}".format(key))
def on_release(key):
    print("Key released: {0}".format(key))
'''
def on_press(key):
    print("Key pressed: {0}".format(key))
    if(key==Key.left):print("Left")
    elif(key==Key.right):print("Right")
    elif(key==Key.up):print("Up")
    elif(key==Key.down):print("Down")
    #print(key)
def on_release(key):
    #print("Key released: {0}".format(key))
    #print(key)
    pass
'''
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
"""