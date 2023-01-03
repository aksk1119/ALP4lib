import ALP4 as alp
import numpy as np
import time

if __name__ == "__main__":
    _alp = alp.ALP4("4.3", "C:\\Program Files\\ALP-4.3\\ALP-4.3 API")
    _alp.Initialize()
    # nSizeX = _alp.DevInquire(alp.ALP_DEV_DISPLAY_WIDTH)
    # nSizeY = _alp.DevInquire(alp.ALP_DEV_DISPLAY_HEIGHT)
    # print(f"{nSizeX}x{nSizeY}")
    bitDepth = 1
    imgBlack = np.zeros([_alp.nSizeY, _alp.nSizeX])
    imgWhite = np.ones([_alp.nSizeY, _alp.nSizeX]) * (2**8 - 1)
    imgSeq = np.concatenate([imgBlack.ravel(), imgWhite.ravel()])
    blackSeq = _alp.SeqAlloc(nbImg=1, bitDepth=bitDepth)
    whiteSeq = _alp.SeqAlloc(nbImg=1, bitDepth=bitDepth)
    _alp.SeqPut(SequenceId=blackSeq, imgData=imgBlack)
    _alp.SeqPut(SequenceId=whiteSeq, imgData=imgWhite)
    _alp.SetTiming(whiteSeq, pictureTime=200000)

    _alp.SeqControl(alp.ALP_BIN_MODE, alp.ALP_BIN_NORMAL, whiteSeq)
    _alp.SeqControl(alp.ALP_BIN_MODE, alp.ALP_BIN_NORMAL, blackSeq)

    _alp.Run(whiteSeq)
    # time.sleep(5)
    _on = False
    while True:
        key = input("Press x for toggle:\n")[0]
        if key == " ":
            break
        elif key == "x":
            _on = not _on
            print("_on", _on)
            if _on:
                _alp.Run(blackSeq)
            else:
                _alp.Run(whiteSeq)

    _alp.Halt()
    _alp.FreeSeq()
    _alp.Free()
