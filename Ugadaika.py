import random

def get_word():
    word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ',
                 'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА',
                 'СКОВОРОДА',
                 'МНОГОНОЖКА', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК',
                 'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА',
                 'ОВЦА', 'БАНАН',
                 'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН',
                 'ТЕЛЕФОН',
                 'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК',
                 'ОМАР',
                 'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'МЕШОК', 'ТЮБИК',
                 'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ',
                 'ПИЦЦА',
                 'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ',
                 'ДИСК']

    return play(random.choice(word_list))

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    tries = 6
    print('Давайте играть в угадайку слов!')
    # print(word)
    print(display_hangman(tries))
    print(len(word) * '*')
    w1 = list(word)
    w2 = list(len(word) * '*')
    w3 = []
    count_wrong = 0
    alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    while tries != 0:
        t = input().upper()
        if t in w3:
            print(f'Давай другую, такая уже была!\n{w3}')

        else:
            if len(t) != 1 or t not in alph:
                count_wrong += 1
                if count_wrong < 4:
                    print('Введите одну русскую букву!')
                elif count_wrong == 4:
                    print('ТЫ ЧО ТУПОЙ?!! ИЛИ ТУПАЯ?')
                else:
                    print('Дурилка, букву, русскую, одну!')

            else:

                if t in w1:
                    for i in range(len(w1)):
                        if w1[i] == t:
                                w2[i] = w1[i]
                        else:
                            continue
                else:
                    tries -= 1
                print(display_hangman(tries))
                print(*w2, sep = '')
                if '*' not in w2:
                    print('ПОБЕДА!!!')
                    break
                w3.append(t)

    if tries == 0:
        print('LOOOOOOOOSEEEEEER')
        print('Это было слово', word)


get_word()
while True:
    q = input('Хочешь ещё сыграть?(есть только один правильный ответ - ДА. Введи маленькую д):')
    if q == 'д':
        get_word()
    else:
        print('Может всё таки ДА?')