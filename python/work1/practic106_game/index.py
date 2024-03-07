import game
import random

all_words = ["кошка", "собака", "коктейл", "яблоко", "смартфон", "компьютер", "ручка", "университет", "кофе", "чай", "девочка", "мальчик", "посуда", "клавиатура"]

random_num = random.randint(0, len(all_words))

game.hangman(all_words[random_num])