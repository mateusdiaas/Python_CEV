#Faca um programa que leia um valor em metro e o exiba em milimetro, centimetros e km.

n1 = float(input('Digite uma mediada em metros: '))
km = n1/1000
hm = n1/100
dam = n1/10
dm = n1*10
cm = n1*100
mm = n1*1000
print('A medida de {:.1f}m corresponde a \n{:.3f}km \n{:.3f}hm \n{:.3f}dam\n{:.3f}dm \n{:.3f}cm \n{:.3f}mm'.format(n1, km, hm, dam, dm, cm, mm))
