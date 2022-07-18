import json
C = 1
try:
    with open('login.txt', 'r') as Login:
        A = json.load(Login)
except:
    A1 = {'admin':'admin'}
    B1 = {}
    with open('login.txt', 'w') as Login:
        json.dump(A1,fp=Login)

    with open('slova.txt', 'w') as Slova:
        json.dump(B1,fp=Slova)

while C:
 with open('login.txt', 'r') as Login:
     A = json.load(Login)
 log = input('Введите логин(для регистрации поставьте цыфру "0"): ')
 pas = input('Введите пароль(для регистрации поставьте цыфру "0"): ')

 for x in A:
     if log == x and pas == A[x]:
        print('Добро пожаловать!')

        while True:
          Vib = input('Добавить слово - 1/Начать обучение - 2: ')
          if Vib == '1':
            with open('slova.txt', 'r') as Slova:
                B = json.load(Slova)
            while True:
             Sl = input('Для возврата назад нажмите "0"\nВведите слово на Английском языке: ')
             if Sl == '0':
                break
             else:
                Rus = input('Введите перевод слова '+str(Sl)+' на Русском языке: ')
                B[str(Sl)] = str(Rus)
                with open('slova.txt', 'w') as Slova:
                    json.dump(B, fp=Slova)
                continue
          elif Vib == '2':
              Gk = 1
              while Gk:
                  with open('slova.txt', 'r') as Slova:
                      B = json.load(Slova)
                  for x in B:
                      Test = input('Для возврата назад нажмите "0"\nВведите перевод слова '+ str(B[x])+ ': ')
                      if Test == str(x):
                          continue
                      elif Test == '0':
                          Gk = 0
                          break

                      else:
                          print('Ошибка, верный перевод: '+ str(x)+ ', запомни его.')
                          continue
          continue

        C = 0
     elif log == '0' or pas == '0':
        print('Регистрация!')
        with open('login.txt', 'r') as Login:
            A = json.load(Login)
        k = input('Введите логин: ')
        j = input('Введите пароль: ')
        A[str(k)] = str(j)
        print('Ваш логин: ' + str(k) + ' \nВаш пароль: ' + str(j))

        with open('login.txt','w') as Login:
            json.dump(A,fp=Login)
        break
     else: continue
print('Следующая ступень')












