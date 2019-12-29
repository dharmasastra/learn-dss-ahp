import numpy as np

model = np.array([[1, 1 / 4, 1 / 2], [4, 1, 3], [2, 1 / 3, 1]])

total = np.array([model[0][0] + model[1][0] + model[2][0],
                  model[0][1] + model[1][1] + model[2][1],
                  model[0][2] + model[1][2] + model[2][2]])

eigen = np.array([[model[0][0] / total[0], model[0][1] / total[1], model[0][2] / total[2]],
                  [model[1][0] / total[0], model[1][1] / total[1], model[1][2] / total[2]],
                  [model[2][0] / total[0], model[2][1] / total[1], model[2][2] / total[2]]])

totalEigen = np.array([eigen[0][0]+eigen[1][0]+eigen[2][0],
                       eigen[0][1]+eigen[1][1]+eigen[2][1],
                       eigen[0][2]+eigen[1][2]+eigen[2][2]])

jumlah = np.array([eigen[0][0]+eigen[0][1]+eigen[0][2],
                   eigen[1][0]+eigen[1][1]+eigen[1][2],
                   eigen[2][0]+eigen[2][1]+eigen[2][2]])

avarage = np.array([jumlah[0]/3, jumlah[1]/3, jumlah[2]/3])

lamdaMax = (total[0] * avarage[0]) + (total[1] * avarage[1]) + (total[2] * avarage[2])

n = 3 #banyak kriteria
CI = (lamdaMax - n)/(n-1)
CR = CI/0.58

print(model)
print(total)

print("\n==== Eigen ===")
print(eigen)
print(totalEigen)

print("\n=== jumlah ===")
print(jumlah)

print("\n=== rata-rata ===")
print(avarage)

print("Lamda Max :", lamdaMax)
print("CI : ", CI)
print("CR : ", CR)
