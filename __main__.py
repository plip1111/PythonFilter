import logging
import threading
import time

def thread_function(name, age):
    logging.info("Thread %s: starting", name)
    time.sleep(age)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,2,))
    y = threading.Thread(target=thread_function, args=(2,4,))
    logging.info("Main    : before running thread")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish")
    y.join()
    x.join()
    logging.info("Main    : all done")