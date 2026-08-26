import numpy as np
def create_htmatrix(angle, dx, dy):
    theta_rad = np.radians(angle)
    c = np.cos(theta_rad)
    s = np.sin(theta_rad)
    return np.array([
        [c, -s, dx],
        [s,  c, dy],
        [0,  0, 1 ]])

a1 = 45
a2 = 45
theta1 = float(input("Enter theta1: "))
theta2 = float(input("Enter theta2: "))
dx1 = a1 * np.cos(np.radians(theta1))
dy1 = a1 * np.sin(np.radians(theta1))
H_01 = create_htmatrix(theta1, dx1, dy1)

dx2 = a2 * np.cos(np.radians(theta2))
dy2 = a2 * np.sin(np.radians(theta2))
H_12 = create_htmatrix(theta2, dx2, dy2)


H_02=np.dot(H_01,H_12)

cordinates = np.dot(H_02, np.array([0, 0, 1]))

print(f": X = {cordinates[0]:.2f}, Y = {cordinates[1]:.2f}")