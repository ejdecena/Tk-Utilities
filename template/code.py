#!/usr/bin/env python3
import time

def run(echo=print, **kwargs):
    i = 0
    while i<10:
        i += 1
        echo("output {}".format(i))
        time.sleep(0.3)

if __name__ == "__main__":
    # Testing ...
    
    run(print)