total_alunos = 36
erraram_todas = 4
acertou_so_primeira = 0
acertou_so_segunda = 5
acertou_so_terceira = 7
resto = total_alunos - (acertou_so_segunda + acertou_so_terceira + erraram_todas)
acertou_primeira_segunda = 9
acertou_primeira_terceira = 10
acertou_segunda_terceira = 7
acertou_todas = int((acertou_primeira_segunda + acertou_primeira_terceira + acertou_segunda_terceira - resto) / 2)
print(f"{acertou_todas} alunos acertaram todas as questões.")