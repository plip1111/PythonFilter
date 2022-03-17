import cv2
from utils import helper

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

rows, cols = grayFrame.shape
threadCount = 4
rowsPerT = (int)((rows - (rows % threadCount)) / threadCount)
oddRows = rows % threadCount


def frameToAscii():
    # this probably should return a value and be given to the main convert function
    helper.setupAsciiMapping()
    while(True):
        ret, frame = cap.read()
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(helper.convertToAscii(
            grayFrame, threadCount, rowsPerT, cols, oddRows))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


frameToAscii()
