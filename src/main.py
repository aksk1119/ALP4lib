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
    seq_id = _alp.SeqAlloc(nbImg=2, bitDepth=bitDepth)
    _alp.SeqPut(SequenceId=seq_id, imgData=imgSeq)
    _alp.SetTiming(seq_id, pictureTime=200000)

    _alp.SeqControl(alp.ALP_BIN_MODE, alp.ALP_BIN_NORMAL, seq_id)

    _alp.Run(seq_id)
    time.sleep(5)

    _alp.Halt()
    _alp.FreeSeq()
    _alp.Free()
