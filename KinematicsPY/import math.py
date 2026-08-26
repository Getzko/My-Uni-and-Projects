from time import sleep
from machine import UART, Pin

SERVO_ID_A = '23'
SERVO_ID_B = '48'
MIN_ANGLE_A, MAX_ANGLE_A = 0, 180
MIN_ANGLE_B, MAX_ANGLE_B = -120, 120
LINK_1 = 450
LINK_2 = 450

bus = UART(
    0, 
    baudrate=115200, 
    bits=8, 
    parity=None, 
    stop=1, 
    tx=Pin(0), 
    rx=Pin(1))

def create_htmatrix(angle, dx, dy):
    rad = np.radians(angle)
    c = np.cos(rad)
    s = np.sin(rad)
    return np.array([
        [c, -s, dx],
        [s,  c, dy],
        [0,  0,  1]])

bus.write(f'#{SERVO_ID_B}G-1\r'.encode())
bus.write(f'#{SERVO_ID_A}G1\r'.encode())
bus.write(f'#{SERVO_ID_A}LED4\r'.encode())
bus.write(f'#{SERVO_ID_B}LED3\r'.encode())
sleep(1)

try:
    while True:
        try:
            angle1 = int(input(f'Enter angle for pencil servo ({MIN_ANGLE_A}-{MAX_ANGLE_A}): '))
            if not (MIN_ANGLE_A <= angle1 <= MAX_ANGLE_A):
                raise ValueError(f'Angle1 out of range.')
            angle2 = int(input(f'Enter angle for 2nd servo ({MIN_ANGLE_B}-{MAX_ANGLE_B}): '))
            if not (MIN_ANGLE_B <= angle2 <= MAX_ANGLE_B):
                raise ValueError(f'Angle2 out of range.')
            print(f'Moving to {angle1}°, {angle2}°')
            bus.write(f'#{SERVO_ID_A}D{angle1 * 10}T1500\r'.encode())
            bus.write(f'#{SERVO_ID_B}D{angle2 * 10}T1500\r'.encode())
            sleep(3)
        except ValueError as e:
            print(f'Error: {e}')
except KeyboardInterrupt:
    bus.write(f'#{SERVO_ID_A}LED0\r'.encode())
    bus.write(f'#{SERVO_ID_B}LED0\r'.encode())
    bus.close()
    print("\nFinished")