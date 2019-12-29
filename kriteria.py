import numpy as np

kriteria = np.array([[1, 1 / 4, 1 / 2], [4, 1, 3], [2, 1 / 3, 1]])

total = np.array([kriteria[0][0] + kriteria[1][0] + kriteria[2][0],
                  kriteria[0][1] + kriteria[1][1] + kriteria[2][1],
                  kriteria[0][2] + kriteria[1][2] + kriteria[2][2]])

eigen = np.array([[kriteria[0][0]/total[0], kriteria[0][1]/total[1], kriteria[0][2]/total[2]],
                  [kriteria[1][0]/total[0], kriteria[1][1]/total[1], kriteria[1][2]/total[2]],
                  [kriteria[2][0]/total[0], kriteria[2][1]/total[1], kriteria[2][2]/total[2]]])

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

print(kriteria)
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
