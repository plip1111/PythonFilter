
import threading


def setupAsciiMapping():
    characterSet = list('.,-~:;=!*#$@')
    for i in range(12):
        for j in range(21):
            _asciiMap[i*21+j] = characterSet[i]
    _asciiMap[252] = '@'
    _asciiMap[253] = '@'
    _asciiMap[254] = '@'
    _asciiMap[255] = '@'


_asciiMap = {}


def _multi_thread_ascii(start, end, threadIndex, cols, frame, convertedImg):
    for x in range(start, end):
        if x % 2 == 0:
            tmp = []
            for y in range(cols):
                l = frame[x, y]
                tmp.append(_asciiMap[l])
            convertedImg[threadIndex].append(tmp)


def convertToAscii(frame, threadCount, rowsPerT, cols, oddRows):
    #print("frame", frame[0:3, 4:5])
    convertedImg = []
    threadArr = []
    for t in range(0, threadCount):
        start = t*rowsPerT
        end = (t+1)*rowsPerT if t != (threadCount -
                                      1) else (t+1) * rowsPerT + oddRows
        threadArr.append(threading.Thread(
            target=_multi_thread_ascii, args=(start, end, t, cols, frame, convertedImg,)))
        convertedImg.append([])

    for t in threadArr:
        t.start()

    for t in threadArr:
        t.join()

    ascii = ''

    for threadLines in convertedImg:
        for lines in threadLines:
            ascii += ' '.join(lines)
            ascii += '\n'
    return ascii
