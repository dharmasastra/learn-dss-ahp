from kriteria import avarage as avarageKriteria
from harga import avarage as avarageHarga
from model import avarage as avarageModel
from kualitas import avarage as avarageKualitas


Adidas = (avarageKriteria[0] * avarageHarga[0]) + \
         (avarageKriteria[1] * avarageModel[0]) + \
         (avarageKriteria[2] * avarageKualitas[0])

Nike = (avarageKriteria[0] * avarageHarga[1]) + \
       (avarageKriteria[1] * avarageModel[1]) + \
       (avarageKriteria[2] * avarageKualitas[1])

Puma = (avarageKriteria[0] * avarageHarga[2]) + \
       (avarageKriteria[1] * avarageModel[2]) + \
       (avarageKriteria[2] * avarageKualitas[2])


print("Nike : {} Rank 1".format(str(Nike)))
print("Adidas : {} Rank 2".format(str(Adidas)))
print("Puma : {} Rank 3".format(str(Puma)))
