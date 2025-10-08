# scripts/mergesort.py
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

def mergesort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def run():
    data = read_input()
    print(f"Leitura concluída: {len(data)} números.")
    to_sort = data.copy()

    start = time.perf_counter()
    result = mergesort(to_sort)
    end = time.perf_counter()

    print(f"Tempo de ordenação (MergeSort): {end - start:.9f} s")
