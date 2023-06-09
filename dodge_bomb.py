
import random
import sys

import pygame as pg


de = {pg.K_UP:(0,-1),#移動の辞書
          pg.K_DOWN:(0,+1),
          pg.K_LEFT:(-1,0),
          pg.K_RIGHT:(+1,0)}


kk_img = pg.image.load("fig/3.png")
kk_imgr = pg.transform.flip(kk_img,True,False)

de2 = {(0,-1):pg.transform.rotozoom(kk_imgr, 90, 2.0),
       (+1,-1):pg.transform.rotozoom(kk_imgr, 45, 2.0),
       (+1,0):pg.transform.rotozoom(kk_imgr, 0, 2.0),
       (+1,+1):pg.transform.rotozoom(kk_img, 135, 2.0),
       (0,+1):pg.transform.rotozoom(kk_img, 90, 2.0),
       (-1,+1):pg.transform.rotozoom(kk_img, 135, 2.0),
       (-1,0):pg.transform.rotozoom(kk_img, 0, 2.0),
       (-1,-1):pg.transform.rotozoom(kk_img, 45, 2.0),
       }


def check_bound(screen_rect: pg.rect,obj_rect:  pg.rect) -> tuple[bool,bool]: 
    """
    オブジェクトが画面内か画面外かを判定
    引数１ 画面surfaceのRect
    引数２ オブジェクトSurfaceのRect
    戻り値 画面内:True 画面外:False
    """
    yoko, tate = True, True
    if obj_rect.left < screen_rect.left or screen_rect.right < obj_rect.right:
        yoko = False
    if obj_rect.top < screen_rect.top or screen_rect.bottom < obj_rect.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kk_img = pg.image.load("fig/3.png")
    kk_img2 = pg.image.load("fig/4.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0

    kk_rct = kk_img.get_rect()#rectクラスの生成と値ゲット
    kk_rct.center = 900,400#コウカトンの最初の位置

    bb_img = pg.Surface((20,20))#爆弾の書かれているスクリーン
    pg.draw.circle(bb_img,(255,0,0),(10,10),10)#爆弾のスクリーンに爆弾を書く
    bb_img.set_colorkey((0,0,0))#爆弾スクリーンの透過
    bb_x = random.randint(0,1600)
    bb_y = random.randint(0,900)
    vx = +1
    vy = +1
    bb_rect = bb_img.get_rect()#rectクラスの生成と値ゲット
    bb_rect.center = bb_x,bb_y#rectクラスのcenterインスタンスの変更
    accs = [a for a in range(1,11) ]
    bb_imgs = []
    for r in range(1,11) :#追加機能２
        bb_img = pg.Surface((20*r, 20*r))
        bb_img.set_colorkey((0,0,0))
        pg.draw.circle(bb_img, (255,0,0), (10*r, 10*r), 10*r)
        bb_imgs.append(bb_img)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        key_lst = pg.key.get_pressed()
        for k,v in de.items():#kが押されたキー、ｖが移動方向
            if key_lst[k]:
                kk_rct.move_ip(v)#移動
                for mk,mv in de2.items():#追加機能１
                    if (v[0],v[1]) == mk:
                        kk_img2=mv
                        screen.blit(kk_img2, kk_rct)
        if check_bound(screen.get_rect(),kk_rct) != (True,True):
             for k,v in de.items():#kが押されたキー、ｖが移動方向
                if key_lst[k]:
                    kk_rct.move_ip(-v[0], -v[1])#移動
                    
        yoko , tate = check_bound(screen.get_rect(),bb_rect)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        avx = vx*accs[min(tmr//1000, 9)]
        avy = vy*accs[min(tmr//1000, 9)]
        bb_img = bb_imgs[min(tmr//1000, 9)]
        bb_rect.move_ip(avx,avy)
        screen.blit(bb_img,bb_rect)
        if  kk_rct.colliderect(bb_rect):#追加機能３
            kk_img = pg.image.load("fig/4.png")
            screen.blit(kk_img,kk_rct)
            clock.tick(0.1)
            return
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()