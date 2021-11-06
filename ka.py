import random
import time
stavka=float(input('Введите ,сколько  фишек  хотите получить (1 фишка = 1 р)   '))
print (' На что вы хотите поставить:')
print('1) Чётная цифра ')
print("2) Нечётная цифра")
print('3) Зелёный цвет(0,10,20,30)')
print('4) Красный цвет(0-15)')
print('5) Чёрный цвет(16-30)')
print('6) На 0-10')
print('7) На 11-20')
print('8) На 21-30')
print('9) На определённое число ')
VaborNashtoStavit = int(input('Введите номер вашей ставки (1-9)  '))
if VaborNashtoStavit == 9 :
    a=int(input('Введите число на которое вы будите ставить (0-30)')) 
    Vapalo = random.randint(0, 30) 
    print('█10%█')
    time.sleep(1)
    print('█30%█')
    time.sleep(1)
    print('█80%█')
    time.sleep(1)
    print('█100%█')
    time.sleep(1)
    if a == Vapalo:
        stavka*=30
        print('Выпало число',Vapalo)
        print('Твой выигрыш',stavka)
        exit()
    else:
        print('Выпало число',Vapalo)
        print('Ты проиграл')
        exit()

print('█10%█')
time.sleep(1)
print('█30%█')
time.sleep(1)
print('█80%█')
time.sleep(1)
print('█100%█')
time.sleep(1)
Vapalo = random.randint(0, 30) 
print('ВАМ ВЫПАЛО:  ',Vapalo)
if VaborNashtoStavit ==1:
    if Vapalo%2 == 0 :
        stavka*=1.9
        print('Твой выигрыш',stavka)
    else:
        print('Ты проиграл')
if VaborNashtoStavit ==2:
    if Vapalo%2 == 1 :
        stavka*=1.9
        print('Твой выигрыш',stavka)
    else:
        print('Ты проиграл')
if VaborNashtoStavit ==3:
    if Vapalo==10 or Vapalo==20 or Vapalo == 30 or Vapalo == 0:
        stavka*=7
        print('Твой выигрыш',stavka)
    else:
        print('Ты проиграл')
if VaborNashtoStavit ==4:
    if Vapalo<15:
        stavka*=1.9
        print('Твой выигрыш',stavka)
    else:
        print('Ты проиграл')  
if VaborNashtoStavit ==5:
    if Vapalo >15:
        stavka*=1.9
        print('Твой выигрыш',stavka)
    else:
        print('Ты проиграл')
if VaborNashtoStavit ==6:
    if 0<=Vapalo<=10:
        stavka*=2.9
        print('Твой выигрыш',stavka)
    else:
        print('Ты проиграл')
if VaborNashtoStavit ==7:
    if 11<=Vapalo<=20:
        stavka*=2.9
        print('Твой выигрыш',stavka)
    else:
        print('Ты проиграл')
if VaborNashtoStavit ==8:
    if 21<=Vapalo<=30:
        stavka*=2.9
        print('Твой выигрыш',stavka)
    else:
        print('Ты проиграл')
