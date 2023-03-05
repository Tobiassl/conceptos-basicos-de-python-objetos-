tabla = int(input('Que tabla quieres ver?: '))
contador = 1
max_number = 100

while contador <= max_number:
    print(f'{tabla} X {contador} = {tabla * contador}')
    contador = contador + 1
