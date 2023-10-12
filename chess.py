"""
chess code main
"""

print("press 1 to quit move. DOES NOT UNDO")
import pygame
import math
import time
import makeboard
import sys, os

# Disable print statements
def blockPrint():
    sys.stdout = open(os.devnull, 'w')
print("welcome to my chess game, i coded this all by my self starting in september of 2023, build 1 was realesed to github on october 13 2023\nif you copy this please give me credit\nuse escape to "
    "quit and 1 to quit move")
blockPrint()
pygame.init()

wpawn = pygame.image.load("chesspawnwhite.png")
bpawn = pygame.image.load("chesspawnblack.png")
bbishop = pygame.image.load("chessbishopblack.png")
wbishop = pygame.image.load("chessbishopwhite.png")
wrook = pygame.image.load("chessrookwhite.png")
brook = pygame.image.load("chessrookblack.png")
wknight = pygame.image.load("chessknightwhite.png")
bknight = pygame.image.load("chessknightblack.png")
wking = pygame.image.load("chesskingwhite.png")
wqueen = pygame.image.load("chessqueenwhite.png")
bking = pygame.image.load("chesskingblack.png")
bqueen = pygame.image.load("chessqueenblack.png")

# white pawns
wp1 = wpawn.get_rect()
wp2 = wpawn.get_rect()
wp3 = wpawn.get_rect()
wp4 = wpawn.get_rect()
wp5 = wpawn.get_rect()
wp6 = wpawn.get_rect()
wp7 = wpawn.get_rect()
wp8 = wpawn.get_rect()
# black pawns
bp1 = bpawn.get_rect()
bp2 = bpawn.get_rect()
bp3 = bpawn.get_rect()
bp4 = bpawn.get_rect()
bp5 = bpawn.get_rect()
bp6 = bpawn.get_rect()
bp7 = bpawn.get_rect()
bp8 = bpawn.get_rect()
# white pieces
wr1 = wrook.get_rect()
wr2 = wrook.get_rect()
wk1 = wknight.get_rect()
wk2 = wknight.get_rect()
wb1 = wbishop.get_rect()
wb2 = wbishop.get_rect()
wk = wking.get_rect()
wq = wqueen.get_rect()
# black pieces
br1 = brook.get_rect()
br2 = brook.get_rect()
bk1 = bknight.get_rect()
bk2 = bknight.get_rect()
bb1 = bbishop.get_rect()
bb2 = bbishop.get_rect()
bk = bking.get_rect()
bq = bqueen.get_rect()


screen_width = 1600
screen_height = 800

window = pygame.display.set_mode([screen_width, screen_height])

clock = pygame.time.Clock()

makeboard.makeboard()




if True:
    wp1f = True
    wp2f = True
    wp3f = True
    wp4f = True
    wp5f = True
    wp6f = True
    wp7f = True
    wp8f = True
    bp1f = True
    bp2f = True
    bp3f = True
    bp4f = True
    bp5f = True
    bp6f = True
    bp7f = True
    bp8f = True
    br1f = True
    br2f = True
    bkf = True
    wkf = True
    wr1f = True
    wr2f = True
    wp1.center = (50, 650)
    wp2.center = (150, 650)
    wp3.center = (250, 650)
    wp4.center = (350, 650)
    wp5.center = (450, 650)
    wp6.center = (550, 650)
    wp7.center = (650, 650)
    wp8.center = (750, 650)
    bp1.center = (50, 150)
    bp2.center = (150, 150)
    bp3.center = (250, 150)
    bp4.center = (350, 150)
    bp5.center = (450, 150)
    bp6.center = (550, 150)
    bp7.center = (650, 150)
    bp8.center = (750, 150)
    wr1.center = (50, 750)
    wk1.center = (150, 750)
    wb1.center = (250, 750)
    wq.center = (350, 750)
    wk.center = (450, 750)
    wb2.center = (550, 750)
    wk2.center = (650, 750)
    wr2.center = (750, 750)
    br1.center = (50, 50)
    bk1.center = (150, 50)
    bb1.center = (250, 50)
    bq.center = (350, 50)
    bk.center = (450, 50)
    bb2.center = (550, 50)
    bk2.center = (650, 50)
    br2.center = (750, 50)
    # white pawns
    window.blit(wpawn, wp1)
    window.blit(wpawn, wp2)
    window.blit(wpawn, wp3)
    window.blit(wpawn, wp4)
    window.blit(wpawn, wp5)
    window.blit(wpawn, wp6)
    window.blit(wpawn, wp7)
    window.blit(wpawn, wp8)
    # white rooks
    window.blit(wrook, wr1)
    window.blit(wrook, wr2)
    # white royalty
    window.blit(wking, wk)
    window.blit(wqueen, wq)
    # white bishops
    window.blit(wbishop, wb1)
    window.blit(wbishop, wb2)
    # white knights
    window.blit(wknight, wk1)
    window.blit(wknight, wk2)
    # black pawns
    window.blit(bpawn, bp1)
    window.blit(bpawn, bp2)
    window.blit(bpawn, bp3)
    window.blit(bpawn, bp4)
    window.blit(bpawn, bp5)
    window.blit(bpawn, bp6)
    window.blit(bpawn, bp7)
    window.blit(bpawn, bp8)
    # black rooks
    window.blit(brook, br1)
    window.blit(brook, br2)
    # black royalty
    window.blit(bking, bk)
    window.blit(bqueen, bq)
    # black bishops
    window.blit(bbishop, bb1)
    window.blit(bbishop, bb2)
    # black knights
    window.blit(bknight, bk1)
    window.blit(bknight, bk2)

    pygame.display.flip()


def boardupdate():
    makeboard.makeboard()
    window.blit(wpawn, wp1)
    window.blit(wpawn, wp2)
    window.blit(wpawn, wp3)
    window.blit(wpawn, wp4)
    window.blit(wpawn, wp5)
    window.blit(wpawn, wp6)
    window.blit(wpawn, wp7)
    window.blit(wpawn, wp8)
    # white rooks
    window.blit(wrook, wr1)
    window.blit(wrook, wr2)
    # white royalty
    window.blit(wking, wk)
    window.blit(wqueen, wq)
    # white bishops
    window.blit(wbishop, wb1)
    window.blit(wbishop, wb2)
    # white knights
    window.blit(wknight, wk1)
    window.blit(wknight, wk2)
    # black pawns
    window.blit(bpawn, bp1)
    window.blit(bpawn, bp2)
    window.blit(bpawn, bp3)
    window.blit(bpawn, bp4)
    window.blit(bpawn, bp5)
    window.blit(bpawn, bp6)
    window.blit(bpawn, bp7)
    window.blit(bpawn, bp8)
    # black rooks
    window.blit(brook, br1)
    window.blit(brook, br2)
    # black royalty
    window.blit(bking, bk)
    window.blit(bqueen, bq)
    # black bishops
    window.blit(bbishop, bb1)
    window.blit(bbishop, bb2)
    # black knights
    window.blit(bknight, bk1)
    window.blit(bknight, bk2)

    pygame.display.flip()


findpos2 = 0  # GARBAGE
my = 0  # mouse y
mx = 0  # mouse x
click = 0  # how many times mouse has been clicked
mfy = 0
mfx = 0
mtx = 0
mty = 0


def picecapw(mtx1, mty1):
    if wp1.collidepoint(mtx1, mty1):
        wp1.center = (850, 150)
        return True
    elif wp2.collidepoint(mtx1, mty1):
        wp2.center = (900, 150)
        return True
    elif wp3.collidepoint(mtx1, mty1):
        wp3.center = (950, 150)
        return True
    elif wp4.collidepoint(mtx1, mty1):
        wp4.center = (1000, 150)
        return True
    elif wp5.collidepoint(mtx1, mty1):
        wp5.center = (1050, 150)
        return True
    elif wp6.collidepoint(mtx1, mty1):
        wp6.center = (1100, 150)
        return True
    elif wp7.collidepoint(mtx1, mty1):
        wp7.center = (1150, 150)
        return True
    elif wp8.collidepoint(mtx1, mty1):
        wp8.center = (1200, 150)
        return True
    elif wr1.collidepoint(mtx1, mty1):
        wr1.center = (850, 50)
        return True
    elif wk1.collidepoint(mtx1, mty1):
        wk1.center = (900, 50)
        return True
    elif wb1.collidepoint(mtx1, mty1):
        wb1.center = (950, 50)
        return True
    elif wq.collidepoint(mtx1, mty1):
        wq.center = (1000, 50)
        return True
    elif wk.collidepoint(mtx1, mty1):
        print("win condition\nking captured\nblack wins!")
        return True
    elif wb2.collidepoint(mtx1, mty1):
        wb2.center = (1100, 50)
        return True
    elif wk2.collidepoint(mtx1, mty1):
        wk2.center = (1150, 50)
        return True
    elif wr2.collidepoint(mtx1, mty1):
        wr2.center = (1200, 50)
        return True
    else:
        return False


def picecapb(mtx1, mty1):
    if bp1.collidepoint(mtx1, mty1):
        bp1.center = 850, 650
        return True
    elif bp2.collidepoint(mtx1, mty1):
        bp2.center = 900, 650
        return True
    elif bp3.collidepoint(mtx1, mty1):
        bp3.center = 950, 650
        return True
    elif bp4.collidepoint(mtx1, mty1):
        bp4.center = 1000, 650
        return True
    elif bp5.collidepoint(mtx1, mty1):
        bp5.center = 1050, 650
        return True
    elif bp6.collidepoint(mtx1, mty1):
        bp6.center = 1100, 650
        return True
    elif bp7.collidepoint(mtx1, mty1):
        bp7.center = 1150, 650
        return True
    elif bp8.collidepoint(mtx1, mty1):
        bp8.center = 1200, 650
        return True
    elif br1.collidepoint(mtx1, mty1):
        br1.center = 850, 750
        return True
    elif bk1.collidepoint(mtx1, mty1):
        bk1.center = 900, 750
        return True
    elif bb1.collidepoint(mtx1, mty1):
        bb1.center = 950, 750
        return True
    elif bq.collidepoint(mtx1, mty1):
        bq.center = 1000, 750
        return True
    elif bk.collidepoint(mtx1, mty1):
        print("win condition\nking captured\nwhite wins!")
        return True
    elif bb2.collidepoint(mtx1, mty1):
        bb2.center = 1100, 750
        return True
    elif bk2.collidepoint(mtx1, mty1):
        bk2.center = 1150, 750
        return True
    elif br2.collidepoint(mtx1, mty1):
        br2.center = 1200, 750
        return True
    else:
        return False


def piceNOTcapw(mtx1, mty1):
    if wp1.collidepoint(mtx1, mty1):
        return True
    elif wp2.collidepoint(mtx1, mty1):
        return True
    elif wp3.collidepoint(mtx1, mty1):
        return True
    elif wp4.collidepoint(mtx1, mty1):
        return True
    elif wp5.collidepoint(mtx1, mty1):
        return True
    elif wp6.collidepoint(mtx1, mty1):
        return True
    elif wp7.collidepoint(mtx1, mty1):
        return True
    elif wp8.collidepoint(mtx1, mty1):
        return True
    elif wr1.collidepoint(mtx1, mty1):
        return True
    elif wk1.collidepoint(mtx1, mty1):
        return True
    elif wb1.collidepoint(mtx1, mty1):
        return True
    elif wq.collidepoint(mtx1, mty1):
        return True
    elif wk.collidepoint(mtx1, mty1):
        return True
    elif wb2.collidepoint(mtx1, mty1):
        return True
    elif wk2.collidepoint(mtx1, mty1):
        return True
    elif wr2.collidepoint(mtx1, mty1):
        return True
    else:
        return False


def piceNOTcapb(mtx1, mty1):
    if bp1.collidepoint(mtx1, mty1):
        return True
    elif bp2.collidepoint(mtx1, mty1):
        return True
    elif bp3.collidepoint(mtx1, mty1):
        return True
    elif bp4.collidepoint(mtx1, mty1):
        return True
    elif bp5.collidepoint(mtx1, mty1):
        return True
    elif bp6.collidepoint(mtx1, mty1):
        return True
    elif bp7.collidepoint(mtx1, mty1):
        return True
    elif bp8.collidepoint(mtx1, mty1):
        return True
    elif br1.collidepoint(mtx1, mty1):
        return True
    elif bk1.collidepoint(mtx1, mty1):
        return True
    elif bb1.collidepoint(mtx1, mty1):
        return True
    elif bq.collidepoint(mtx1, mty1):
        return True
    elif bk.collidepoint(mtx1, mty1):
        return True
    elif bb2.collidepoint(mtx1, mty1):
        return True
    elif bk2.collidepoint(mtx1, mty1):
        return True
    elif br2.collidepoint(mtx1, mty1):
        return True
    else:
        return False
def picenotcapALL(mtx1,mty1):
    if bp1.collidepoint(mtx1, mty1):
        return True
    elif bp2.collidepoint(mtx1, mty1):
        return True
    elif bp3.collidepoint(mtx1, mty1):
        return True
    elif bp4.collidepoint(mtx1, mty1):
        return True
    elif bp5.collidepoint(mtx1, mty1):
        return True
    elif bp6.collidepoint(mtx1, mty1):
        return True
    elif bp7.collidepoint(mtx1, mty1):
        return True
    elif bp8.collidepoint(mtx1, mty1):
        return True
    elif br1.collidepoint(mtx1, mty1):
        return True
    elif bk1.collidepoint(mtx1, mty1):
        return True
    elif bb1.collidepoint(mtx1, mty1):
        return True
    elif bq.collidepoint(mtx1, mty1):
        return True
    elif bk.collidepoint(mtx1, mty1):
        return True
    elif bb2.collidepoint(mtx1, mty1):
        return True
    elif bk2.collidepoint(mtx1, mty1):
        return True
    elif br2.collidepoint(mtx1, mty1):
        return True
    elif wp1.collidepoint(mtx1, mty1):
        return True
    elif wp2.collidepoint(mtx1, mty1):
        return True
    elif wp3.collidepoint(mtx1, mty1):
        return True
    elif wp4.collidepoint(mtx1, mty1):
        return True
    elif wp5.collidepoint(mtx1, mty1):
        return True
    elif wp6.collidepoint(mtx1, mty1):
        return True
    elif wp7.collidepoint(mtx1, mty1):
        return True
    elif wp8.collidepoint(mtx1, mty1):
        return True
    elif wr1.collidepoint(mtx1, mty1):
        return True
    elif wk1.collidepoint(mtx1, mty1):
        return True
    elif wb1.collidepoint(mtx1, mty1):
        return True
    elif wq.collidepoint(mtx1, mty1):
        return True
    elif wk.collidepoint(mtx1, mty1):
        return True
    elif wb2.collidepoint(mtx1, mty1):
        return True
    elif wk2.collidepoint(mtx1, mty1):
        return True
    elif wr2.collidepoint(mtx1, mty1):
        return True
    else:
        return False


def whitepawnmove(pice, picef, mtx1, mty1, mfx1, mfy1):
    if pice.center == (mfx1, mfy1):
        if mtx1 == mfx1 and mty1 == (mfy1 - 100) and not piceNOTcapw(mtx1, mty1) and not piceNOTcapb(mtx1, mty1):
            if mty1 < 800 and mtx1 < 800:
                picecapb(mtx1, mty1)
                pice.center = (mtx1, mty1)
                return True

        elif picef and mty1 == (mfy1 - 200) and mtx1 == mfx1 and not piceNOTcapw(mtx1, mty1) and not piceNOTcapb(mtx1,
        mty1) and not piceNOTcapw(mtx1, (mty1 + 100)) and not piceNOTcapb(mtx1, (mty1 + 100)):
            if mty1 < 800 and mtx1 < 800:
                picecapb(mtx1, mty1)
                pice.center = (mtx1, mty1)
                return True
        elif mty1 == (mfy1 - 100) and mtx1 == mfx1 - 100 and not piceNOTcapw(mtx1, mty1):
            if picecapb(mtx1, mty1) and not piceNOTcapw(mtx1, mty1):
                if mty1 < 800 and mtx1 < 800:
                    picecapb(mtx1, mty1)
                    pice.center = (mtx1, mty1)
                    return True
        elif mty1 == (mfy1 - 100) and mtx1 == mfx1 + 100 and not piceNOTcapw(mtx1, mty1):
            if picecapb(mtx1, mty1) and not piceNOTcapw(mtx1, mty1):
                if mty1 < 800 and mtx1 < 800:
                    picecapb(mtx1, mty1)
                    pice.center = (mtx1, mty1)
                    return True
        else:
            return False


def blackpawnmove(pice, picef, mtx1, mty1, mfx1, mfy1):
    if pice.center == (mfx1, mfy1):
        if mtx1 == mfx1 and mty1 == (mfy1 + 100) and not piceNOTcapb(mtx1, mty1) == True and not piceNOTcapw(mtx1, mty1) == True:
            if mty1 < 800 and mtx1 < 800:
                picecapw(mtx1, mty1)
                pice.center = (mtx1, mty1)
                return True
        elif picef == True and mty1 == (mfy1 + 200) and mtx1 == mfx1 and not piceNOTcapb(mtx1, mty1) == True and not piceNOTcapw(mtx1, mty1) == True\
                and not piceNOTcapb(mtx1, (mty1 - 100)) == True and not piceNOTcapw(mtx1, (
                mty1 - 100)) == True:
            if mty1 < 800 and mtx1 < 800:
                picecapw(mtx1, mty1)
                pice.center = (mtx1, mty1)
                return True
        elif mty1 == (mfy1 + 100) and mtx1 == mfx1 - 100 and not piceNOTcapb(mtx1, mty1) == True:
            if picecapw(mtx1, mty1) == True and not piceNOTcapb(mtx1, mty1) == True:
                if mty1 < 800 and mtx1 < 800:
                    picecapw(mtx1, mty1)
                    pice.center = (mtx1, mty1)
                    return True
        elif mty1 == (mfy1 + 100) and mtx1 == mfx1 + 100 and not piceNOTcapb(mtx1, mty1) == True:
            if picecapw(mtx1, mty1) == True and not piceNOTcapb(mtx1, mty1) == True:
                if mty1 < 800 and mtx1 < 800:
                    picecapw(mtx1, mty1)
                    pice.center = (mtx1, mty1)
                    return True
        else:
            return False


def knightmoveb(pice, mfy1, mfx1, mtx1, mty1):
    if pice.center == (mfx1, mfy1):
        if (mtx1 == mfx1 + 200 and mty1 == mfy1 + 100) or \
                (mtx1 == mfx1 + 200 and mty1 == mfy1 + 100) or \
                (mtx1 == mfx1 + 200 and mty1 == mfy1 - 100) or \
                (mtx1 == mfx1 - 200 and mty1 == mfy1 + 100) or \
                (mtx1 == mfx1 - 200 and mty1 == mfy1 - 100) or \
                (mtx1 == mfx1 + 100 and mty1 == mfy1 + 200) or \
                (mtx1 == mfx1 + 100 and mty1 == mfy1 - 200) or \
                (mtx1 == mfx1 - 100 and mty1 == mfy1 + 200) or \
                (mtx1 == mfx1 - 100 and mty1 == mfy1 - 200):
            if not piceNOTcapb(mtx1, mty1) == True:
                if mty1 < 800 and mtx1 < 800:
                    picecapw(mtx1, mty1)
                    pice.center = (mtx1, mty1)
                    return True


def knightmovew(pice, mfy1, mfx1, mtx1, mty1):
    if pice.center == (mfx1, mfy1):
        if (mtx1 == mfx1 + 200 and mty1 == mfy1 + 100) or \
                (mtx1 == mfx1 + 200 and mty1 == mfy1 + 100) or \
                (mtx1 == mfx1 + 200 and mty1 == mfy1 - 100) or \
                (mtx1 == mfx1 - 200 and mty1 == mfy1 + 100) or \
                (mtx1 == mfx1 - 200 and mty1 == mfy1 - 100) or \
                (mtx1 == mfx1 + 100 and mty1 == mfy1 + 200) or \
                (mtx1 == mfx1 + 100 and mty1 == mfy1 - 200) or \
                (mtx1 == mfx1 - 100 and mty1 == mfy1 + 200) or \
                (mtx1 == mfx1 - 100 and mty1 == mfy1 - 200):
            if not piceNOTcapw(mtx1, mty1):
                if mty1 < 800 and mtx1 < 800:
                    picecapb(mtx1, mty1)
                    pice.center = (mtx1, mty1)
                    return True


def kingmovew(pice, mfx1, mfy1, mtx1, mty1):
    if pice.center == (mfx1, mfy1):
        if mtx1 == mfx1 + 100 or mtx1 == mfx1 - 100 or mtx1 == mfx1:
            if mty1 == mfy1 + 100 or mty1 == mfy1 - 100 or mty1 == mfy1:
                if not piceNOTcapw(mtx1, mty1) == True:
                    if mty1 < 800 and mtx1 < 800:
                        picecapb(mtx1, mty1)
                        pice.center = (mtx1, mty1)
                        return True


def kingmoveb(pice, mfx1, mfy1, mtx1, mty1):
    if pice.center == (mfx1, mfy1):
        if mtx1 == mfx1 + 100 or mtx1 == mfx1 - 100 or mtx1 == mfx1:
            if mty1 == mfy1 + 100 or mty1 == mfy1 - 100 or mty1 == mfy1:
                if not piceNOTcapb(mtx1, mty1) == True:
                    if mty1 < 800 and mtx1 < 800:
                        picecapw(mtx1, mty1)
                        pice.center = (mtx1, mty1)
                        return True



def rookmovew(pice, mfx1, mfy1, mtx1, mty1):
    checker = 0
    if pice.center == (mfx1, mfy1):
        move_y = abs(mty1 - mfy1)
        move_x = abs(mtx1 - mfx1)
        if mtx1 == mfx1 and mfy1 < mty1:
            for i in range(1, int(move_y / 100)):
                if not picenotcapALL(mfx1, mfy1 + (i * 100)) and not piceNOTcapw(mtx1,mty1):
                    checker = 1
                    continue
                else:
                    checker = 0
                    break
        if mtx1 == mfx1 and mfy1 > mty1:
            for i in range(1, int(move_y / 100)):
                if not picenotcapALL(mfx1, mfy1 - (i * 100)) and not piceNOTcapw(mtx1,mty1):
                    checker = 1
                    continue
                else:
                    checker = 0
                    break
        if mty1 == mfy1 and mfx1 < mtx1:
            for i in range(1, int(move_x / 100)):
                if not picenotcapALL(mfx1 + (i * 100), mfy1) and not piceNOTcapw(mtx1,mty1):
                    checker = 1
                    continue
                else:
                    checker = 0
                    break
        if mty1 == mfy1 and mfx1 > mtx1:
            for i in range(1, int(move_x / 100)):
                if not picenotcapALL(mfx1 - (i * 100), mfy1) and not piceNOTcapw(mtx1,mty1):
                    checker = 1
                    continue
                else:
                    checker = 0
                    break
        if mty1 == mfy1 and mfx1 < mtx1 and move_x == 100:
            if not piceNOTcapw(mtx1, mty1):
                checker = 1
            else:
                checker = 0
        if mty1 == mfy1 and mfx1 > mtx1 and move_x == 100:
            if not piceNOTcapw(mtx1, mty1):
                checker = 1
            else:
                checker = 0
        if mtx1 == mfx1 and mfy1 < mty1 and move_y == 100:
            if not piceNOTcapw(mtx1, mty1):
                checker = 1
            else:
                checker = 0
        if mtx1 == mfx1 and mfy1 > mty1 and move_y == 100:
            if not piceNOTcapw(mtx1, mty1):
                checker = 1
            else:
                checker = 0
        if checker == 1:
            if mty1 < 800 and mtx1 < 800:
                picecapb(mtx1, mty1)
                pice.center = (mtx1, mty1)
                return True
        elif checker == 0:
            return False
        else:
            return False


def rookmoveb(pice, mfx1, mfy1, mtx1, mty1):
    checker = 0
    if pice.center == (mfx1, mfy1):
        move_y = abs(mty1 - mfy1)
        move_x = abs(mtx1 - mfx1)
        if mtx1 == mfx1 and mfy1 < mty1:
            for i in range(1, int(move_y / 100)):
                if not picenotcapALL(mfx1, mfy1 + (i * 100)) and not piceNOTcapb(mtx1,mty1):
                    checker = 1
                    continue
                else:
                    checker = 0
                    break
        elif mtx1 == mfx1 and mfy1 > mty1:
            for i in range(1, int(move_y / 100)):
                if not picenotcapALL(mfx1, mfy1 - (i * 100)) and not piceNOTcapb(mtx1,mty1):
                    checker = 1
                    continue
                else:
                    checker = 0
                    break
        elif mty1 == mfy1 and mfx1 < mtx1:
            for i in range(1, int(move_x / 100)):
                if not picenotcapALL(mfx1 + (i * 100), mfy1) and not piceNOTcapb(mtx1,mty1):
                    checker = 1
                    continue
                else:
                    checker = 0
                    break
        elif mty1 == mfy1 and mfx1 > mtx1:
            for i in range(1, int(move_x / 100)):
                if not picenotcapALL(mfx1 - (i * 100), mfy1) and not piceNOTcapb(mtx1,mty1):
                    checker = 1
                    continue
                else:
                    checker = 0
                    break

        if mty1 == mfy1 and mfx1 < mtx1 and move_x == 100:
            if not piceNOTcapb(mtx1, mty1):
                checker = 1
            else:
                checker = 0
        if mty1 == mfy1 and mfx1 > mtx1 and move_x == 100:
            if not piceNOTcapb(mtx1, mty1):
                checker = 1
            else:
                checker = 0
        if mtx1 == mfx1 and mfy1 < mty1 and move_y == 100:
            if not piceNOTcapb(mtx1, mty1):
                checker = 1
            else:
                checker = 0
        if mtx1 == mfx1 and mfy1 > mty1 and move_y == 100:
            if not piceNOTcapb(mtx1, mty1):
                checker = 1
            else:
                checker = 0
        if checker == 1:
            if mty1 < 800 and mtx1 < 800:
                picecapw(mtx1, mty1)
                pice.center = (mtx1, mty1)
                return True
        elif checker == 0:
            return False
        else:
            return False


def bishopmovew(pice, mfx1, mfy1, mtx1, mty1):
    checker = 0
    move2 = False
    range1 = 1
    if pice.center == (mfx1, mfy1):
        move_x = abs(mfx1 - mtx1)
        move_y = abs(mfy1 - mty1)
        if move_x == move_y:
            move = move_x
            if move == 100:
                move2 = True
                range1 = 0
            for i in range(range1, int(move / 100)):
                if mfx1 > mtx1 and mfy1 > mty1:
                    if (move2 == True and not piceNOTcapw(mtx1, mty1)) or (not picenotcapALL(mfx1 - (i * 100), mfy1 - (i * 100)) and not piceNOTcapw(mtx1, mty1)):
                        checker = 1
                        continue
                    else:
                        checker = 0
                        break
                elif mfx1 < mtx1 and mfy1 < mty1:
                    if (move2 == True and not piceNOTcapw(mtx1, mty1)) or (not picenotcapALL(mfx1 + (i * 100), mfy1 + (i * 100)) and not piceNOTcapw(mtx1, mty1)):
                        checker = 1
                        continue
                    else:
                        checker = 0
                        break
                elif mfx1 < mtx1 and mfy1 > mty1:
                    if (move2 == True and not piceNOTcapw(mtx1, mty1)) or (not picenotcapALL(mfx1 + (i * 100), mfy1 - (i * 100)) and not piceNOTcapw(mtx1, mty1)):
                        checker = 1
                        continue
                    else:
                        checker = 0
                        break
                elif mfx1 > mtx1 and mfy1 < mty1:
                    if (move2 == True and not piceNOTcapw(mtx1, mty1)) or (not picenotcapALL(mfx1 - (i * 100), mfy1 + (i * 100)) and not piceNOTcapw(mtx1, mty1)):
                        checker = 1
                        continue
                    else:
                        checker = 0
                        break
            if checker == 1:
                if mty1 < 800 and mtx1 < 800:
                    picecapb(mtx1, mty1)
                    pice.center = (mtx1, mty1)
                    return True
            elif checker == 0:
                return False
            else:
                return False


def bishopmoveb(pice, mfx1, mfy1, mtx1, mty1):
    checker = 0
    move2 = False
    range1 = 1
    if pice.center == (mfx1, mfy1):
        move_x = abs(mfx1 - mtx1)
        move_y = abs(mfy1 - mty1)
        if move_x == move_y:
            move = move_x
            if move == 100:
                move2 = True
                range1 = 0
            for i in range(range1, int(move / 100)):
                if mfx1 > mtx1 and mfy1 > mty1:
                    if (move2 == True and not piceNOTcapb(mtx1, mty1)) or (not picenotcapALL(mfx1 - (i * 100), mfy1 - (i * 100)) and not piceNOTcapb(mtx1, mty1)):
                        checker = 1
                        continue
                    else:
                        checker = 0
                        break
                elif mfx1 < mtx1 and mfy1 < mty1:
                    if (move2 == True and not piceNOTcapb(mtx1, mty1)) or (not picenotcapALL(mfx1 + (i * 100), mfy1 + (i * 100)) and not piceNOTcapb(mtx1, mty1)):
                        checker = 1
                        continue
                    else:
                        checker = 0
                        break
                elif mfx1 < mtx1 and mfy1 > mty1:
                    if (move2 == True and not piceNOTcapb(mtx1, mty1)) or (not picenotcapALL(mfx1 + (i * 100), mfy1 - (i * 100)) and not piceNOTcapb(mtx1, mty1)):
                        checker = 1
                        continue
                    else:
                        checker = 0
                        break
                elif mfx1 > mtx1 and mfy1 < mty1:
                    if (move2 == True and not piceNOTcapb(mtx1, mty1)) or (not picenotcapALL(mfx1 - (i * 100), mfy1 + (i * 100)) and not piceNOTcapb(mtx1, mty1)):
                        checker = 1
                        continue
                    else:
                        checker = 0
                        break
            if checker == 1:
                if mty1 < 800 and mtx1 < 800:
                    picecapw(mtx1, mty1)
                    pice.center = (mtx1, mty1)
                    return True
            elif checker == 0:
                return False
            else:
                return False


def queenw(pice,mfx1,mfy1,mtx1,mty1):
    if rookmovew(pice, mfx1, mfy1, mtx1, mty1) or bishopmovew(pice, mfx1, mfy1, mtx1, mty1):
        return True


def queenb(pice,mfx1,mfy1,mtx1,mty1):
    if rookmoveb(pice, mfx1, mfy1, mtx1, mty1) or bishopmoveb(pice, mfx1, mfy1, mtx1, mty1):
        return True




def play():
    global my, mx, click, event, mfx, mfy, mtx, mty, wp1
    global wp1f, wp2f, wp3f, wp4f, wp5f, wp6f, wp7f, wp8f
    global bp1f, bp2f, bp3f, bp4f, bp5f, bp6f, bp7f, bp8f
    keys = pygame.key.get_pressed()

    # mouse stuffs
    pygame.event.get()
    pygame.mouse.set_visible(True)
    x, y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed() == (1, 0, 0):
        pygame.time.wait(100)
        if click == 0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    click = 1
                    mx = int(int(x / 100) * 100 + 50)
                    my = int(int(y / 100) * 100 + 50)
                    mfx = mx
                    mfy = my
                    print(mfx, mfy)

        elif click == 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    click = 2
                    mx = int(int(x / 100) * 100 + 50)
                    my = int(int(y / 100) * 100 + 50)
                    mtx = mx
                    mty = my
                    print(mtx, mty)
    elif keys[pygame.K_1]:
        click = 0
    if click == 2:
        click = 0
        if whitepawnmove(wp1, wp1f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            wp1f = False
            return True
        elif whitepawnmove(wp2, wp2f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            wp2f = False
            return True
        elif whitepawnmove(wp3, wp3f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            wp3f = False
            return True
        elif whitepawnmove(wp4, wp4f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            wp4f = False
            return True
        elif whitepawnmove(wp5, wp5f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            wp5f = False
            return True
        elif whitepawnmove(wp6, wp6f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            wp6f = False
            return True
        elif whitepawnmove(wp7, wp7f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            wp7f = False
            return True
        elif whitepawnmove(wp8, wp8f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            wp8f = False
            return True
        elif blackpawnmove(bp1, bp1f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            bp1f = False
            return True
        elif blackpawnmove(bp2, bp2f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            bp2f = False
            return True
        elif blackpawnmove(bp3, bp3f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            bp3f = False
            return True
        elif blackpawnmove(bp4, bp4f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            bp4f = False
            return True
        elif blackpawnmove(bp5, bp5f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            bp5f = False
            return True
        elif blackpawnmove(bp6, bp6f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            bp6f = False
            return True
        elif blackpawnmove(bp7, bp7f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            bp7f = False
            return True
        elif blackpawnmove(bp8, bp8f, mtx, mty, mfx, mfy):
            boardupdate()
            pygame.display.flip()
            bp8f = False
            return True
        elif knightmovew(wk1, mfy, mfx, mtx, mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif knightmovew(wk2, mfy, mfx, mtx, mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif knightmoveb(bk1, mfy, mfx, mtx, mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif knightmoveb(bk2, mfy, mfx, mtx, mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif kingmoveb(bk, mfx, mfy, mtx, mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif kingmovew(wk, mfx, mfy, mtx, mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif rookmovew(wr1,mfx,mfy,mtx,mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif rookmovew(wr2,mfx,mfy,mtx,mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif rookmoveb(br1,mfx,mfy,mtx,mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif rookmoveb(br2,mfx,mfy,mtx,mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif bishopmovew(wb1,mfx,mfy,mtx,mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif bishopmovew(wb2,mfx,mfy,mtx,mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif bishopmoveb(bb1,mfx,mfy,mtx,mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif bishopmoveb(bb2,mfx,mfy,mtx,mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif queenw(wq, mfx, mfy, mtx, mty):
            boardupdate()
            pygame.display.flip()
            return True
        elif queenb(bq, mfx, mfy, mtx, mty):
            boardupdate()
            pygame.display.flip()
            return True
        else:
            print("no") 



