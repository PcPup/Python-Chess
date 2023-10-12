mfy1 = 0
mty1= 0
mfx1= 0
mtx1 = 0

if mfy1 == mty1 and not piceNOTcapw(mty1, mty1):
    if (((mfy1 + 100 == mty1 and not piceNOTcapw(mty1, mfy1 + 100)) or (mfy1 - 100 == mty1 and not piceNOTcapw(mty1, mfy1 - 100))
         or (mfy1 + 200 == mty1 and not piceNOTcapw(mty1 + 100, mfy1) and not piceNOTcapb(mfx1 + 100, mfy1) and not piceNOTcapw(mty1, mfy1 + 200))
         or (mfy1 - 200 == mty1 and not piceNOTcapw(mty1 - 100, mfy1) and not piceNOTcapb(mfx1 - 100, mfy1) and not piceNOTcapw(mty1, mfy1 - 200))
         or (mfy1 + 300 == mty1 and not piceNOTcapw(mty1 + 100, mfy1) and not piceNOTcapb(mfx1 + 100, mfy1) and not piceNOTcapw(mty1, mfy1 + 200))
         and not piceNOTcapb(mty1, mfy1 + 200) and not piceNOTcapw(mty1, mfy1 + 300))
            or (mfy1 - 300 == mty1 and not piceNOTcapw(mty1, mfy1 - 100) and not piceNOTcapb(mty1, mfy1 - 100) and not piceNOTcapw(mty1, mfy1 - 200)
                and not piceNOTcapb(mty1, mfy1 - 200) and not piceNOTcapw(mty1, mfy1 - 300))
            or (mfy1 + 400 == mty1 and not piceNOTcapw(mty1, mfy1 + 100) and not piceNOTcapb(mty1, mfy1 + 100) and not piceNOTcapw(mty1, mfy1 + 200)
                and not piceNOTcapb(mty1, mfy1 + 200) and not piceNOTcapw(mty1, mfy1 + 300) and not piceNOTcapb(mty1, mfy1 + 300) and not piceNOTcapw(mty1, mfy1 + 400))
            or (mfy1 - 400 == mty1 and not piceNOTcapw(mty1, mfy1 - 100) and not piceNOTcapb(mty1, mfy1 - 100) and not piceNOTcapw(mty1, mfy1 - 200)
                and not piceNOTcapb(mty1, mfy1 - 200) and not piceNOTcapw(mty1, mfy1 - 300) and not piceNOTcapb(mty1, mfy1 - 300) and not piceNOTcapw(mty1, mfy1 - 400))
            or (mfy1 + 500 == mty1 and not piceNOTcapw(mty1, mfy1 + 100) and not piceNOTcapb(mty1, mfy1 + 100) and not piceNOTcapw(mty1, mfy1 + 200)
                and not piceNOTcapb(mty1, mfy1 + 200) and not piceNOTcapw(mty1, mfy1 + 300) and not piceNOTcapb(mty1, mfy1 + 300) and not piceNOTcapw(mty1, mfy1 + 400)
                and not piceNOTcapb(mty1, mfy1 + 400) and not piceNOTcapw(mty1, mfy1 + 500))
            or (mfy1 - 500 == mty1 and not piceNOTcapw(mty1, mfy1 - 100) and not piceNOTcapb(mty1, mfy1 - 100) and not piceNOTcapw(mty1, mfy1 - 200)
                and not piceNOTcapb(mty1, mfy1 - 200) and not piceNOTcapw(mty1, mfy1 - 300) and not piceNOTcapb(mty1, mfy1 - 300) and not piceNOTcapw(mty1, mfy1 - 400)
                and not piceNOTcapb(mty1, mfy1 - 400) and not piceNOTcapw(mty1, mfy1 - 500))
            or (mfy1 + 600 == mty1 and not piceNOTcapw(mty1, mfy1 + 100) and not piceNOTcapb(mty1, mfy1 + 100) and not piceNOTcapw(mty1, mfy1 + 200)
                and not piceNOTcapb(mty1, mfy1 + 200) and not piceNOTcapw(mty1, mfy1 + 300) and not piceNOTcapb(mty1, mfy1 + 300) and not piceNOTcapw(mty1, mfy1 + 400)
                and not piceNOTcapb(mty1, mfy1 + 400) and not piceNOTcapw(mty1, mfy1 + 500) and not piceNOTcapb(mty1, mfy1 + 500) and not piceNOTcapw(mty1, mfy1 + 600))
            or (mfy1 - 600 == mty1 and not piceNOTcapw(mty1, mfy1 - 100) and not piceNOTcapb(mty1, mfy1 - 100) and not piceNOTcapw(mty1, mfy1 - 200)
                and not piceNOTcapb(mty1, mfy1 - 200) and not piceNOTcapw(mty1, mfy1 - 300) and not piceNOTcapb(mty1, mfy1 - 300) and not piceNOTcapw(mty1, mfy1 - 400)
                and not piceNOTcapb(mty1, mfy1 - 400) and not piceNOTcapw(mty1, mfy1 - 500) and not piceNOTcapb(mty1, mfy1 - 500) and not piceNOTcapw(mty1, mfy1 - 600))
            or (mfy1 + 700 == mty1 and not piceNOTcapw(mty1, mfy1 + 100) and not piceNOTcapb(mty1, mfy1 + 100) and not piceNOTcapw(mty1, mfy1 + 200)
                and not piceNOTcapb(mty1, mfy1 + 200) and not piceNOTcapw(mty1, mfy1 + 300) and not piceNOTcapb(mty1, mfy1 + 300) and not piceNOTcapw(mty1, mfy1 + 400)
                and not piceNOTcapb(mty1, mfy1 + 400) and not piceNOTcapw(mty1, mfy1 + 500) and not piceNOTcapb(mty1, mfy1 + 500) and not piceNOTcapw(mty1, mfy1 + 600)
                and not piceNOTcapb(mty1, mfy1 + 600) and not piceNOTcapw(mty1, mfy1 + 700))
            or (mfy1 - 700 == mty1 and not piceNOTcapw(mty1, mfy1 - 100) and not piceNOTcapb(mty1, mfy1 - 100) and not piceNOTcapw(mty1, mfy1 - 200)
                and not piceNOTcapb(mty1, mfy1 - 200) and not piceNOTcapw(mty1, mfy1 - 300) and not piceNOTcapb(mty1, mfy1 - 300) and not piceNOTcapw(mty1, mfy1 - 400)
                and not piceNOTcapb(mty1, mfy1 - 400) and not piceNOTcapw(mty1, mfy1 - 500) and not piceNOTcapb(mty1, mfy1 - 500) and not piceNOTcapw(mty1, mfy1 - 600)
                and not piceNOTcapb(mty1, mfy1 - 600) and not piceNOTcapw(mty1, mfy1 - 700))):
        picecapb(mty1, mty1)
        pice.center = (mty1, mty1)
