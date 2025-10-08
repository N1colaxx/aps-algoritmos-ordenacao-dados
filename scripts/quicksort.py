# scripts/quicksort.py
import time
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "lista_desordenada.txt"

def read_input():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {DATA_FILE}")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if not content:
        return []
    parts = content.replace(",", " ").split()
    return [int(p) for p in parts]

def _quicksort_inplace(a, lo, hi):
    if lo >= hi:
        return
    pivot = a[(lo + hi) // 2]
    i, j = lo, hi
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if lo < j:
        _quicksort_inplace(a, lo, j)
    if i < hi:
        _quicksort_inplace(a, i, hi)

def run():
    data = read_input()
    print(f"Leitura concluída: {len(data)} números.")
    to_sort = data.copy()

    start = time.perf_counter()
    if to_sort:
        _quicksort_inplace(to_sort, 0, len(to_sort)-1)
    end = time.perf_counter()

    print(f"Tempo de ordenação (QuickSort): {end - start:.9f} s")
