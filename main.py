import numpy as np
import matplotlib.pyplot as plt


#a = np.array([1,2,3,4])
#b = np.array([5,6,7,8])

#print(a[0])
#print(b[1])

#c = np.array([
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
#])

#x = np.array([1,2,3,4])
#y = np.array([5,6,7,8])

#print(x+y)
#x = np.arange(0,1000,5)
#y = np.sin(x)
#============================#
#x = np.linspace(0,1000,101)
#y = np.sin(x)
#print(x)

#=============================#

#a = np.array([
#    [
 #       [1,2,3],
  #      [4,5,6]
   # ],
    #[
     #   [10,20,30],
      #  [40,50,60],
    #]
#], dtype=float)

#print (a.ndim)
#print (a)

################################

#a = np.array([
  # [1,2,3],
 #  [4,5,6],
 #  [7,8,9]
#])
#print(np.exp(a))
#print(np.log(a))
#print(np.sqrt(a))
#print(np.sum(a))
#print(np.min(a))
#print(np.mean(a))
#print(np.median(a))
#print(np.std(a))

############################

a = np.array([
   [1,2,3,7],
   [4,5,6,7],
   [7,8,9,7],
   [8,5,3,1]
])

b = [10,20,30,40]

#b = np.array([
    #[10,20,30,40],
#    [50,60,70,80],
  #  [10,20,30,50]
#])

#a = a.reshape((2,6))
#print(a.flatten())

#print(a.transpose())

#for x in a.flat:
   # print(x)


#print(np.split(a,4))

#a = np.append(a, [b], axis = 0)
#a = np.insert(a,1,b,axis=0)
#a = np.insert(a,2,b,axis=1)
#print(a)

######################################

x = np.arange(0,100,0.2)
y1 = np.sin(x)
y2 = x ** 2 + 2 * x
y3 = np.log(x)


plt.figure(1)
ax1 = plt.subplot(211)
ax1.plot(x,y1,'g')
ax2 = plt.subplot(212)
ax2.plot(x,y2,'r')

plt.figure(2)
plt.plot(x,y1)

plt.figure(3)
plt.plot(x,y3)


plt.plot
plt.show()


#plt.plot(x,y1,'r--')
#plt.plot(x,y2,'r--')
#plt.plot(x,y3,'r--')
#plt.show()
