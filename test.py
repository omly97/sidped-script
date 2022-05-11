from Models.Efficience import Efficience
from Repositories.EfficienceRepository import EfficienceRepository


repo = EfficienceRepository()
data = repo.select_all__efficience()

print(data)

# new_data = []
# for item in data:
#     new_data.append({
#         'annee': item[1],
#         'PE1': (item[2] * 100) / (item[2] + item[3]),
#         'PE2': ((item[4] + item[5]) * 100) / item[6],
#         'PE3': (item[7] * item[8] * 100) / (item[9] + 10),
#     })

# print(new_data)

# eff = Efficience()
# eff.set_annee(1999)
# eff.set_pe1_tr(78)
# eff.set_pe1_ta(98)
# eff.set_pe2_cp(5)
# eff.set_pe2_ca(98)
# eff.set_pe2_b(12)
# eff.set_pe3_d1(86)
# eff.set_pe3_sa(20)
# eff.set_pe3_cp(20)
# eff.set_pe3_ca(29)

# repo.create_efficience(eff)
