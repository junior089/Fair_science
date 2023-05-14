from tkinter import *
import socket
import RPi.GPIO as GPIO
import time

# Configura os pinos do GPIO para o controle do motor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT) # Pino do motor 1
GPIO.setup(18, GPIO.OUT) # Pino do motor 2

# Define a frequência do PWM
pwm_frequency = 50 # Hz

# Define o tempo mínimo e máximo do PWM
pwm_min_duty_cycle = 5 # %
pwm_max_duty_cycle = 95 # %

# Cria uma janela para o aplicativo
root = Tk()
root.title('Controle de Robô')

# Cria um socket para se comunicar com o servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Função para enviar as instruções para o servidor
def send_command(command):
    try:
        # Conecta ao servidor
        server_address = ('192.168.0.100', 5000) # Endereço IP do servidor
        client_socket.connect(server_address)

        # Envia a instrução para o servidor
        client_socket.sendall(command.encode())

    except Exception as e:
        print('Erro ao enviar comando:', e)

    finally:
        # Fecha a conexão com o servidor
        client_socket.close()

# Função para controlar o motor
def control_motor(duty_cycle_1, duty_cycle_2):
    # Calcula o tempo ligado e desligado do PWM
    on_time_1 = (duty_cycle_1 / 100) * (1 / pwm_frequency)
    off_time_1 = ((100 - duty_cycle_1) / 100) * (1 / pwm_frequency)
    on_time_2 = (duty_cycle_2 / 100) * (1 / pwm_frequency)
    off_time_2 = ((100 - duty_cycle_2) / 100) * (1 / pwm_frequency)

    # Define os pinos do PWM
    pwm_1 = GPIO.PWM(17, pwm_frequency)
    pwm_2 = GPIO.PWM(18, pwm_frequency)

    # Inicia os PWMs
    pwm_1.start(0)
    pwm_2.start(0)

    # Define o tempo ligado e desligado dos PWMs
    pwm_1.ChangeDutyCycle(duty_cycle_1)
    pwm_2.ChangeDutyCycle(duty_cycle_2)
    time.sleep(on_time_1)
    pwm_1.ChangeDutyCycle(0)
    time.sleep(off_time_1)
    pwm_2.ChangeDutyCycle(duty_cycle_2)
    time.sleep(on_time_2)
    pwm_2.ChangeDutyCycle(0)

    # Para os PWMs
    pwm_1.stop()
    pwm_2.stop()

# Função para controlar o robô
def control_robot(direction):
    if direction == 'Frente':
        # Move o robô para frente com velocidade máxima
        control_motor(pwm_max_duty_cycle, pwm_max_duty_cycle)
        send_command('Frente')

    elif direction == 'Trás':
        # Move o robô para trás com velocidade máxima
        control_motor(-pwm_max_duty_cycle, -pwm_max_duty_cycle)
        send_command('Trás')

    elif direction == 'Esquerda':
        # Gira o robô para a esquerda com velocidade máxima
        control_motor(-pwm_max_duty_cycle, pwm_max_duty_cycle)
        send_command('Esquerda')

    elif direction == 'Direita':
        # Gira o robô para a direita com velocidade máxima
        control_motor(pwm_max_duty_cycle, -pwm_max_duty_cycle)
        send_command('Direita')

# Cria os botões para controlar o robô
button_forward = Button(root, text='Frente', command=lambda: control_robot('Frente'))
button_backward = Button(root, text='Trás', command=lambda: control_robot('Trás'))
button_left = Button(root, text='Esquerda', command=lambda: control_robot('Esquerda'))
button_right = Button(root, text='Direita', command=lambda: control_robot('Direita'))

# Adiciona os botões à janela
button_forward.pack()
button_backward.pack()
button_left.pack()
button_right.pack()

# Inicia a janela
root.mainloop()

# Limpa a configuração do GPIO
GPIO.cleanup()
