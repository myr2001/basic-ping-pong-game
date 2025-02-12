from pygame import * # pygame kütüphanesinden her şeyi al
from random import randint
from time import time as timer

# ----- OYUN PENCERESİ VE ARKAPLAN -----
window = display.set_mode((700,500)) # arkaplan boyutu
display.set_caption("Ping Pong") # Başlık
# Arkaplan rengi:
background_color = (130, 210, 255) # RGB
window.fill(background_color)

# ----- MÜZİK -----
mixer.init() # initialize (başlat)
mixer.music.load("retromusic.ogg")
mixer.music.play() # arkaplan olarak ayarla
mixer.music.set_volume(0.05) # müzik sesi kısma (0: ses yok, 1: en yüksek)

# ----- GAMESPRITE SINIFI -----
class GameSprite(sprite.Sprite): # üst sınıf: Sprite, alt sınıf: GameSprite
    # constructor fonksiyonu:
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y): # özellikler listesi
        super().__init__() # üst sınıfın özelliklerini devral
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    # ekrana yeniden yükleme fonksiyonu:
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# ----- PLAYER SINIFI -----
class Player(GameSprite):
    # sağdaki oyuncunun hareket fonksiyonu
    def update_r(self):
        keys = key.get_pressed()
        # yukarı tuşa basılıysa ve ekranın yukarısına dayanmadıysa:
        if keys[K_UP] and self.rect.y > 5:
            # yukarıya belirlenmiş hız kadar hareket et:
            self.rect.y -= self.speed
        # aşağı tuş basılıysa ve ekranın altına dayanmadıysa:
        if keys[K_DOWN] and self.rect.y < (500 - self.rect.height):
            # aşağıya hareket:
            self.rect.y += self.speed
    # soldaki oyuncunun hareket fonksiyonu
    def update_l(self):
        keys = key.get_pressed()
        # W tuşa basılıysa ve ekranın yukarısına dayanmadıysa:
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        # S tuş basılıysa ve ekranın altına dayanmadıysa:
        if keys[K_s] and self.rect.y < (500 - self.rect.height):
            self.rect.y += self.speed

# ----- SPRITE TANIMLAMA -----
racket1 = Player("racket1.png", 4, 30, 200, 50, 150) # oyuncu 1
racket2 = Player("racket2.png", 4, 620, 200, 50, 150) # oyuncu 2
ball = GameSprite("ball.png", 4, 200, 200, 50, 50) # top

# ----- YAZILAR -----
font.init()
font = font.Font(None, 35)
lose1 = font.render("PLAYER 1 LOST!", True, (180,0,0))
lose2 = font.render("PLAYER 2 LOST!", True, (180,0,0))

speed_x = 3
speed_y = 3

# ----- OYUN DÖNGÜSÜ -----
game = True # döngü değişkeni (çarpıya basınca oyun kapansın)
finish = False # döngü değişkeni (oyunu kazanınca oyun kapansın)
clock = time.Clock() #zamanlayıcı yarat
FPS = 60 # frames per second (saniye başına düşen kare)

while game: # oyun döngüsü
    # ----- OYUNDAN ÇIKMA -----
    for e in event.get(): # oyundaki olayları tara
        if e.type == QUIT: # oyundan çık olayı varsa:
            game = False # döngüyü durdur
    
    # ----- OYUN BİTMEDİYSE: -----
    if finish != True:
        window.fill(background_color) # arkaplan rengini güncelle
        racket1.update_l() # oyuncu 1'in hareketlerini güncelle
        racket2.update_r() # oyuncu 2'nin hareketlerini güncelle
        # topun hareketlerini güncelle:
        ball.rect.x += speed_x # topun x pozisyonuna speed x kadar ekle (yatay)
        ball.rect.y += speed_y # topun y pozisyonuna speed y kadar ekle (dikey)

        # ----- ÇARPIŞMALAR -----
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        # oyuncu 1 ve top çarpışıyorsa yada oyuncu 2 ve top çarpışıyorsa:
            speed_x *= -1 # yatay hızı ters çevir (sektir)
        
        if ball.rect.y > 450 or ball.rect.y < 0:
        # eğer top pencerenin en aşağısına yada en yukarısına çarptıysa:
            speed_y *= -1 # dikey hızı ters çevir (sektir)
        
        if ball.rect.x < 0:
        # eğer top pencerenin sol tarafına dokunduysa:
            finish = True # oyun bitsin
            window.blit(lose1, (200,200)) # oyuncu 1 kaybetti yazısını pencerenin ortasına getir
        
        if ball.rect.x > 700:
        # eğer top pencerenin sağ tarafına dokunduysa:
            finish = True # oyun bitsin
            window.blit(lose2, (200,200)) # oyuncu 2 kaybetti yazısını pencerenin ortasına getir
    
    # ekrandaki konumların güncellenmesi:
    racket1.reset()
    racket2.reset()
    ball.reset()

    clock.tick(FPS) # zamanlayıcının çalıştırılması
    display.update() # ekran güncellenmesi
