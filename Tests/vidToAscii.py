import sys
import cv2
import os
import threading
from pynput.keyboard import Key, Listener
import time
from utils import helper
# from termcolor import colored

run = True

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
frameHeight, frameWidth = grayFrame.shape
compressionRatio = 0.25
yAxisBalance = 1.75  # increases the compression block scoope for the y-axis
frameHeight, frameWidth = grayFrame.shape

rows = int(frameHeight * compressionRatio)
cols = int(frameWidth * compressionRatio)
poolingBlockWidth = frameWidth // cols
poolingBlockHeight = frameHeight // rows

threadCount = 4
rowsPerT = int((rows - (rows % threadCount)) / threadCount)
oddRows = frameWidth % threadCount

consoleColorBg = '\33[40m'
infoTextBg = '\33[46m'
consoleColor = '\33[37m'


def _update_parameters():
    global rows, cols, poolingBlockWidth, poolingBlockHeight, rowsPerT
    rows = int(frameHeight * compressionRatio)
    cols = int(frameWidth * compressionRatio)
    poolingBlockWidth = frameWidth // cols
    poolingBlockHeight = frameHeight // rows
    rowsPerT = int((rows - (rows % threadCount)) / threadCount)


def on_release(key):
    global compressionRatio, run, consoleColor, yAxisBalance
    helper.writeAt(0, 2, '{0} release'.format(
        key), infoTextBg)
    try:
        if key:
            if key.char == ('1') and (compressionRatio - 0.05) > 0:
                helper.writeAt(0, 3, compressionRatio, infoTextBg)
                compressionRatio -= 0.05
                _update_parameters()
                os.system("cls")
            if key.char == ('2') and (compressionRatio + 0.05) < 1:
                helper.writeAt(0, 3, compressionRatio, infoTextBg)
                compressionRatio += 0.05
                _update_parameters()
                os.system("cls")
            if key.char == ('3') and (yAxisBalance - 0.25) >= 1:
                helper.writeAt(0, 3, yAxisBalance, infoTextBg)
                yAxisBalance -= 0.25
                _update_parameters()
                os.system("cls")
            if key.char == ('4') and (yAxisBalance + 0.25) <= 2:
                helper.writeAt(0, 3, yAxisBalance, infoTextBg)
                yAxisBalance += 0.25
                _update_parameters()
                os.system("cls")
            if key.char == ('w'):
                consoleColor = '\33[97m'  # white
            if key.char == ('r'):
                consoleColor = '\33[91m'  # light red
            if key.char == ('g'):
                consoleColor = '\33[92m'  # light green
            if key.char == ('b'):
                consoleColor = '\33[94m'  # light blue
            if key.char == ('y'):
                consoleColor = '\33[93m'  # light yellow
            if key.char == ('l'):
                tmp = int(consoleColor[2]+consoleColor[3])
                tmp = (tmp+60) if tmp <= 90 else (tmp-60)
                consoleColor = '\33['+str(tmp)+'m'
        if key == Key.space:
            helper.writeAt(0, 3, "space if")
        if key == Key.esc:
            run = False
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


# ratio
# frameWidth 1920
# frameHeight 1080
# rows = int(frameWidth * ratio) 540
# cols = int(frameHeight * ratio) 960
# poolingBlockWidth = frameWidth // cols 2
# poolingBlockHeight = frameHeight // rows 2


def frameToAscii():
    os.system("cls")
    # this probably should return a value and be given to the main convert function
    helper.setupAsciiMapping()
    listener = Listener(on_release=on_release)
    listener.start()
    while(run):
        ret, frame = cap.read()
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        output = helper.convertToAsciiBlockMulti(grayFrame, rows,
                                                 cols, poolingBlockWidth, poolingBlockHeight, frameWidth, frameHeight, threadCount, rowsPerT, yAxisBalance)

        helper.writeAt(0, 0, "rows:", infoTextBg)
        helper.writeAt(8, 0, rows, infoTextBg)
        helper.writeAt(16, 0, "cols:", infoTextBg)
        helper.writeAt(24, 0, cols, infoTextBg)

        threadArr = []
        for t in range(0, threadCount):
            y = 4+int(t*rowsPerT/yAxisBalance)

            threadArr.append(threading.Thread(
                target=helper.writeAt, args=(0, y, output[t], consoleColorBg, consoleColor)))

        for t in threadArr:
            t.start()

        sys.stdout.flush()

    cap.release()
    cv2.destroyAllWindows()


frameToAscii()
# helper.standardVid()
