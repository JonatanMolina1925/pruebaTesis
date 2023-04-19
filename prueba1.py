import pywt
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy import signal
import math
#Variables para el calculo de caracteristicas
min = 0.0
max = 0.0
avgA = 0.0
avgd1 = 0.0
avgd2 = 0.0
avgd3 = 0.0
avgd4 = 0.0
enA = 0.0
end1 = 0.0
end2 = 0.0
end3 = 0.0
end4 = 0.0
rmsA = 0.0
rmsd1 = 0.0
rmsd2 = 0.0
rmsd3 = 0.0
rmsd4 = 0.0
desEstA = 0.0
desEstd1 = 0.0
desEstd2 = 0.0
desEstd3 = 0.0
desEstd4 = 0.0
skA = 0.0
skd1 = 0.0
skd2 = 0.0
skd3 = 0.0
skd4 = 0.0
krA = 0.0
krd1 = 0.0
krd2 = 0.0
krd3 = 0.0
krd4 = 0.0

rmsX = 0.0
rmsRuido=0.0

#señal senoidal 
x = np.loadtxt('flicker.csv', delimiter=',')
for n in x:
    rmsX=rmsX+math.pow(n,2)
# rmsX=math.sqrt(rmsX/len(x))
# plt.plot(x)
# plt.show()

#ruido 
ruido=np.random.randn(len(x))
ruido = ruido*0.8
for n in x:
    rmsRuido=rmsRuido+math.pow(n,2)
# rmsRuido=math.sqrt(rmsRuido/len(ruido))
# plt.plot(ruido)
# plt.show()
snr=math.pow(rmsX/rmsRuido,2)
snrDB=10*math.log10(snr)
print("RMSX: "+str(rmsX)+"\n")
print("RMSRUIDO: "+str(rmsRuido)+"\n")
print("SNR: "+str(snrDB)+"\n")

sr=x+ruido
# plt.plot(sr)
# plt.show()

inicio=time.time()
#Calculo de transformada
cA,CD1,CD2,CD3,CD4 = pywt.wavedec(sr, 'db3', level=4)

#Calculo de promedio y rms
for n in cA:
    avgA=avgA+n
    rmsA=rmsA+math.pow(n,2)
    enA=enA+math.pow(n,2)
for n in CD1:
    avgd1=avgd1+n
    rmsd1=rmsd1+math.pow(n,2)
    end1=end1+math.pow(n,2)
for n in CD2:
    avgd2=avgd2+n
    rmsd2=rmsd2+math.pow(n,2)
    end2=end2+math.pow(n,2)
for n in CD3:
    avgd3=avgd3+n
    rmsd3=rmsd3+math.pow(n,2)
    end3=end3+math.pow(n,2)
for n in CD4:
    avgd4=avgd4+n
    rmsd4=rmsd4+math.pow(n,2)
    end4=end4+math.pow(n,2)

avgA=avgA/len(cA)
avgd1=avgd1/len(CD1)
avgd2=avgd2/len(CD2)
avgd3=avgd3/len(CD3)
avgd4=avgd4/len(CD4)

rmsA=math.sqrt(rmsA/len(cA))
rmsd1=math.sqrt(rmsA/len(CD1))
rmsd2=math.sqrt(rmsA/len(CD2))
rmsd3=math.sqrt(rmsA/len(CD3))
rmsd4=math.sqrt(rmsA/len(CD4))

for n in cA:
    desEstA=desEstA+math.pow(n-avgA,2)
for n in CD1:
    desEstd1=desEstd1+math.pow(n-avgd1,2)
for n in CD2:
    desEstd2=desEstd2+math.pow(n-avgd2,2)
for n in CD3:
    desEstd3=desEstd3+math.pow(n-avgd3,2)
for n in CD4:
    desEstd4=desEstd4+math.pow(n-avgd4,2)

desEstA=math.sqrt(desEstA/len(cA))
desEstd1=math.sqrt(desEstd1/len(CD1))
desEstd2=math.sqrt(desEstd2/len(CD2))
desEstd3=math.sqrt(desEstd3/len(CD3))
desEstd4=math.sqrt(desEstd4/len(CD4))

for n in cA:
    skA=skA+math.pow(n-avgA/desEstA,3)
    krA=krA+math.pow(n-avgA/desEstA,4)
for n in CD1:
    skd1=skd1+math.pow(n-avgd1/desEstd1,3)
    krd1=krd1+math.pow(n-avgd1/desEstd1,4)
for n in CD2:
    skd2=skd2+math.pow(n-avgd2/desEstd2,3)
    krd2=krd2+math.pow(n-avgd2/desEstd2,4)
for n in CD3:
    skd3=skd3+math.pow(n-avgd3/desEstd3,3)
    krd3=krd3+math.pow(n-avgd3/desEstd3,4)
for n in CD4:
    skd4=skd4+math.pow(n-avgd4/desEstd4,3)
    krd4=krd4+math.pow(n-avgd4/desEstd4,4)

skA=skA/len(cA)
skd1=skd1/len(CD1)
skd2=skd2/len(CD2)
skd3=skd3/len(CD3)
skd4=skd4/len(CD4)

krA=krA/len(cA)
krd1=krd1/len(CD1)
krd2=krd2/len(CD2)
krd3=krd3/len(CD3)
krd4=krd4/len(CD4)

fin=time.time()
print(str(fin-inicio)+" segundos\n")
print("El promedio de cA es: "+str(avgA)+"\n")
print("El promedio de CD1 es: "+str(avgd1)+"\n")
print("El promedio de CD2 es: "+str(avgd2)+"\n")
print("El promedio de CD3 es: "+str(avgd3)+"\n")
print("El promedio de CD4 es: "+str(avgd4)+"\n")

print("El rms de cA es: "+str(rmsA)+"\n")
print("El rms de CD1 es: "+str(rmsd1)+"\n")
print("El rms de CD2 es: "+str(rmsd2)+"\n")
print("El rms de CD3 es: "+str(rmsd3)+"\n")
print("El rms de CD4 es: "+str(rmsd4)+"\n")

print("El energia de cA es: "+str(enA)+"\n")
print("El energia de CD1 es: "+str(end1)+"\n")
print("El energia de CD2 es: "+str(end2)+"\n")
print("El energia de CD3 es: "+str(end3)+"\n")
print("El energia de CD4 es: "+str(end4)+"\n")

print("El Skewness de cA es: "+str(skA)+"\n")
print("El Skewness de CD1 es: "+str(skd1)+"\n")
print("El Skewness de CD2 es: "+str(skd2)+"\n")
print("El Skewness de CD3 es: "+str(skd3)+"\n")
print("El Skewness de CD4 es: "+str(skd4)+"\n")

print("El Kurtosis de cA es: "+str(krA)+"\n")
print("El Kurtosis de CD1 es: "+str(krd1)+"\n")
print("El Kurtosis de CD2 es: "+str(krd2)+"\n")
print("El Kurtosis de CD3 es: "+str(krd3)+"\n")
print("El Kurtosis de CD4 es: "+str(krd4)+"\n")

print("La desviacion estandar de cA es: "+str(desEstA)+"\n")
print("La desciacion estandar de CD1 es: "+str(desEstd1)+"\n")
print("La desviacion estandar de CD2 es: "+str(desEstd2)+"\n")
print("La desviacion estandar de CD3 es: "+str(desEstd3)+"\n")
print("La desviacion estandar de CD4 es: "+str(desEstd4)+"\n")

plt.subplot(7,1,1), plt.plot(x)
plt.subplot(7,1,2), plt.plot(sr)
plt.subplot(7,1,3), plt.plot(cA)
plt.subplot(7,1,4), plt.plot(CD1)
plt.subplot(7,1,5), plt.plot(CD2)
plt.subplot(7,1,6), plt.plot(CD3)
plt.subplot(7,1,7), plt.plot(CD4)
# plt.subplot(7,1,8), plt.plot(CD4)
plt.show()
