
import threading
import sys
import numpy
import cv2


def writeAt(x, y, content, colorBg='\33[40m', color='\33[37m'):
    sys.stdout.write("%s%s\x1b7\x1b[%d;%df%s\x1b8" %
                     (colorBg, color, y, x, content))


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

# pixel = np.mean(frame[
#       2 * int(y * poolingBlockHeight):min(int((y + 1) * poolingBlockHeight), frameHeight),
#       1 * int(x * poolingBlockWidth ):min(int((x + 1) * poolingBlockWidth ), frameWidth)])


def convertToAsciiSingle(frame, rows, cols, poolingBlockWidth, poolingBlockHeight, frameWidth, frameHeight, yAxisBalance):
    convertedImg = []

    for y in range(int(rows/yAxisBalance)):
       # if y % 2 == 0:
        tmp = []
        for x in range(cols):
            pixel = numpy.mean(frame[
                int(yAxisBalance*y * poolingBlockHeight):min(int(yAxisBalance*(y + 1) * poolingBlockHeight), frameHeight),
                int(x * poolingBlockWidth):min(int((x + 1) * poolingBlockWidth), frameWidth)

            ])
            tmp.append(_asciiMap[int(pixel)])
        convertedImg.append(tmp)

    ascii = ''

    for lines in convertedImg:
        ascii += ' '.join(lines)
        ascii += '\n'
    return ascii


def _convertFrameChunksToAscii(start, end, threadIndex, cols, frame, convertedImg, poolingBlockWidth, poolingBlockHeight, frameWidth, frameHeight, yAxisBalance):
    for y in range(int(start/yAxisBalance), int(end/yAxisBalance)):
       # if y % 2 == 0:
        tmp = []
        for x in range(cols):
            pixel = numpy.mean(frame[
                int(yAxisBalance*y * poolingBlockHeight):min(int(yAxisBalance*(y + 1) * poolingBlockHeight), frameHeight),
                int(x * poolingBlockWidth):min(int((x + 1) * poolingBlockWidth), frameWidth)

            ])
            tmp.append(_asciiMap[int(pixel)])
        convertedImg[threadIndex].append(tmp)


def convertToAsciiBlockMulti(frame, rows, cols, poolingBlockWidth, poolingBlockHeight, frameWidth, frameHeight, threadCount, rowsPerT, yAxisBalance):
    convertedImg = []
    threadArr = []
    for t in range(0, threadCount):
        start = t*rowsPerT
        end = (t+1)*rowsPerT if t != (threadCount -
                                      1) else (t+1) * rowsPerT
        threadArr.append(threading.Thread(
            target=_convertFrameChunksToAscii, args=(start, end, t, cols, frame, convertedImg, poolingBlockWidth, poolingBlockHeight, frameWidth, frameHeight, yAxisBalance)))
        convertedImg.append([])

    for t in threadArr:
        t.start()

    for t in threadArr:
        t.join()

    ascii = []

    for threadLines in convertedImg:
        tmp = ''
        for lines in threadLines:
            tmp += ' '.join(lines)
            tmp += '\n'
        ascii.append(tmp)
    return ascii


def standardVid():
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
