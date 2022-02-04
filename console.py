import pdb
from models.vet import Vet
from models.pet import Pet
from models.owner import Owner

import repositories.vet_repository as vet_repository
import repositories.pet_repository as pet_repository
import repositories.owner_repository as owner_repository

# pet_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()


vet1 = Vet("Bradley Jiles", "Dogs")
vet_repository.save(vet1)

vet2 = Vet("Philipa Bronhime", "Cats")
vet_repository.save(vet2)

owner1 = Owner("Clive Boggs", "23 lonely lane, LL12 6BG", "clive@gmail.com", "07898533267")
owner_repository.save(owner1)

owner2 = Owner("Bob Hope", "17 Mosley Close, AB16 9JO", "Bob@gmail.com", "07794609239")
owner_repository.save(owner2)


pdb.set_trace()