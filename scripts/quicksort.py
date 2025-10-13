# Importa o módulo 'time' para medir o tempo de execução
import time

# Importa 'Path' da biblioteca 'pathlib' para manipular caminhos de arquivo
from pathlib import Path

# Define o caminho do arquivo de entrada
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "lista_desordenada.txt"


# ---------- Função de leitura dos dados ----------
def read_input():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {DATA_FILE}")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if not content:
        return []
    parts = content.replace(",", " ").split()
    return [int(p) for p in parts]


# ---------- Função auxiliar do QuickSort ----------
def _quicksort_inplace(a, lo, hi):
    # Caso base: se o intervalo é inválido ou de um único elemento
    if lo >= hi:
        return

    # Escolhe o pivô como o elemento do meio
    pivot = a[(lo + hi) // 2]

    # i percorre da esquerda, j da direita
    i, j = lo, hi

    # Enquanto os índices não se cruzarem
    while i <= j:
        # Move 'i' até encontrar um elemento >= pivô
        while a[i] < pivot:
            i += 1
        # Move 'j' até encontrar um elemento <= pivô
        while a[j] > pivot:
            j -= 1
        # Se ainda não cruzaram, troca os elementos
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    # Chama recursivamente para as partições à esquerda e à direita do pivô
    if lo < j:
        _quicksort_inplace(a, lo, j)
    if i < hi:
        _quicksort_inplace(a, i, hi)


# ---------- Função para executar o QuickSort ----------
def run():
    data = read_input()
    print(f"Leitura concluída: {len(data)} números.")

    to_sort = data.copy()

    start = time.perf_counter()

    if to_sort:
        _quicksort_inplace(to_sort, 0, len(to_sort) - 1)

    end = time.perf_counter()

    print(f"Tempo de ordenação (QuickSort): {end - start:.9f} s")
