# Lizard run

### Импорт библиотек и подключение модулей

    `from pygame import *
    font.init()

* pygame - для создания интерфейса и функционала игры
* font - для дальнейшей работы с текстом

### Создание классов

    class GameSprite(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_speed, player_w, player_h):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (player_w, player_h))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y

* self.image - Свойство,  отвечающее за отображение спрайтов
* self.speed - -Свойство, отвечающее за скорость перемещения объекта
* self.rect - Свойство, получающее границы объекта
* self.rect.x - Свойство, обозначающее X координату объекта
* self.rect.y - Свойство, обозначающее Y координату объекта

