# scripts/heapsort.py
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

def _sift_down(a, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and a[child] < a[child + 1]:
            child += 1
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            root = child
        else:
            break

def heapsort_inplace(a):
    n = len(a)
    for start in range((n - 2) // 2, -1, -1):
        _sift_down(a, start, n - 1)
    for end in range(n - 1, 0, -1):
        a[end], a[0] = a[0], a[end]
        _sift_down(a, 0, end - 1)

def run():
    data = read_input()
    print(f"Leitura concluída: {len(data)} números.")
    to_sort = data.copy()

    start = time.perf_counter()
    if to_sort:
        heapsort_inplace(to_sort)
    end = time.perf_counter()

    print(f"Tempo de ordenação (HeapSort): {end - start:.9f} s")
