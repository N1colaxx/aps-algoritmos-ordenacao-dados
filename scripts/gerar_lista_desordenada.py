import random
from pathlib import Path

path_saida = Path("data/lista_desordenada.txt")
path_saida.parent.mkdir(parents=True, exist_ok=True)

lista = list(range(30001))  
random.shuffle(lista)  # embaralha a lista

try:
    with path_saida.open("w") as f:
        for num in lista:
            f.write(str(num) + "\n")

except Exception as e:
    print(f"\nERRO ao salvar em {path_saida}: {e}")
else:
    print(f"\nSUCESSO! Lista embaralhada salva em: {path_saida}")
finally:
    print("Operação finalizada.")
