from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.5)
        print('Piloto: {} Km: {} \n'.format(piloto, trajeto))

t_carro1 = Thread(target=carro, args=[1, 'Bruno'])
t_carro2 = Thread(target=carro, args=[1.5, 'Python'])

t_carro1.start()
t_carro2.start()

# def carro2(velocidade):
#     trajeto = 0
#     while trajeto <= 100:
#         print('Carro 2: ', trajeto)
#         trajeto+=velocidade