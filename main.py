import random

opciones = ('piedra', 'papel', 'tijera')

computadora_gana = 0
usuario_gana = 0

rondas = 1

while True:

    print('*' * 10)
    print('RONDAS', rondas)
    print('*' * 10)

    print('Juegos Ganados por la Computadora:', computadora_gana)
    print('Juegos Ganados por el usuario:', usuario_gana)

    usuario_opciones = input('piedra, papel o tijera ==> ')
    usuario_opciones = usuario_opciones.lower()

    rondas += 1

    if not usuario_opciones in opciones:
      print('esa opción no es valida')
      continue

    computador_opciones = random.choice(opciones)

    print('Opción del usuario: =>', usuario_opciones)
    print('Opción de la Computadora =>', computador_opciones)

    if usuario_opciones == computador_opciones:
        print('Empate!')
    elif usuario_opciones == 'piedra':
        if computador_opciones == 'tijera':
            print('piedra gana a tijera')
            print('usuario ganó!')
            usuario_gana += 1
        else:
            print('Papel gana a piedra')
            print('computador ganó!')
            computadora_gana += 1
    elif usuario_opciones == 'papel':
        if computador_opciones == 'piedra':
            print('papel gana a piedra')
            print('usuario ganó')
            usuario_gana += 1
        else:
            print('tijera gana a papel')
            print('computador ganó!')
            computadora_gana += 1
    elif usuario_opciones == 'tijera':
        if computador_opciones == 'papel':
            print('tijera gana a papel')
            print('usuario ganó!')
            usuario_gana += 1
        else:
            print('piedra gana a tijera')
            print('computadora ganó!')
            computadora_gana += 1

    if computadora_gana == 2:
      print('El ganador es la computadora')
      break

    if usuario_gana == 2:
      print('El ganador es el usuario')
      break