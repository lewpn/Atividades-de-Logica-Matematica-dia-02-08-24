compram_nenhum = 100
compram_ABC = 20
compram_AB = 60 - compram_ABC
compram_AC = 70 - compram_ABC
compram_BC = 50 - compram_ABC
compram_A = 210 - compram_AB - compram_AC - compram_ABC
compram_B = 210 - compram_BC - compram_AB - compram_ABC
compram_C = 250 - compram_AC - compram_BC - compram_ABC
total_entrevistados = compram_ABC + compram_A + compram_B + compram_C + compram_AB + compram_AC + compram_BC + compram_nenhum
print(f"{total_entrevistados} pessoas foram entrevistadas.")