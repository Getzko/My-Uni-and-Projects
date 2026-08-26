import numpy as np
b=100
L1=100
L2=80
L3=70
t1=0
t2=0
t3=0


H_base=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
H01=np.array([[np.cos(t1),-np.sin(t1),0,0],[np.sin(t1),np.cos(t1),0,0],[0,0,1,L1],[0,0,0,1]])
H12=np.array([[1,0,0,0],[0,np.cos(t2),-np.sin(t2),0],[0,np.sin(t2),np.cos(t2),L2],[0,0,0,1 ]])
H23=np.array([[1,0,0,0],[0,np.cos(t3),-np.sin(t3),L2],[0,np.sin(t3),np.cos(t3),0],[0,0,0,1]])
H34=np.array([[1,0,0,0],[0,1,0,L3],[0,0,1,0],[0,0,0,1]])
result=H01@H12@H23@H34
print(result)

