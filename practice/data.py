import pandas as pd
import numpy
import matplotlib.pyplot as plt

data = {
  'Nama': ['Zaenal', 'Alfian', 'Haikal'],
  'Usia': [20, 21, 22],
  'Pekerjaan': ['Full-Stack','Front-End','Back-End']
}

df = pd.DataFrame(data)
print(df)

matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriks)

x = [1,2,3,4,5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.title("Contoh plot garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu y")
plt.show()