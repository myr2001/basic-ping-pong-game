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
        if keys[K_DOWN] and self.rect.y < 495:
            # aşağıya hareket:
            self.rect.y += self.speed
    # soldaki oyuncunun hareket fonksiyonu
    def update_l(self):
        keys = key.get_pressed()
        # W tuşa basılıysa ve ekranın yukarısına dayanmadıysa:
        if keys["K_w"] and self.rect.y > 5:
            self.rect.y -= self.speed
        # S tuş basılıysa ve ekranın altına dayanmadıysa:
        if keys["K_s"] and self.rect.y < 495:
            self.rect.y += self.speed
