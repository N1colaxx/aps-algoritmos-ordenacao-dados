# Importa o módulo 'time' para medir o tempo de execução
import time

# Importa 'Path' da biblioteca 'pathlib' para manipular caminhos de arquivo de forma segura
from pathlib import Path

# Define o caminho absoluto do arquivo de entrada que contém a lista desordenada
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "lista_desordenada.txt"


# ---------- Função de leitura dos dados ----------
def read_input():
    # Verifica se o arquivo existe
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {DATA_FILE}")
    
    # Abre o arquivo para leitura em modo texto e codificação UTF-8
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        # Lê todo o conteúdo e remove espaços e quebras de linha extras
        content = f.read().strip()
    
    # Caso o arquivo esteja vazio, retorna uma lista vazia
    if not content:
        return []
    
    # Substitui vírgulas por espaços e separa o texto em partes
    parts = content.replace(",", " ").split()
    
    # Converte cada parte em um número inteiro
    return [int(p) for p in parts]


# ---------- Função principal: MergeSort ----------
def mergesort(a):
    # Caso base: listas com 0 ou 1 elemento já estão ordenadas
    if len(a) <= 1:
        return a

    # Divide a lista no meio
    mid = len(a) // 2

    # Chama recursivamente o mergesort para a metade esquerda e direita
    left = mergesort(a[:mid])
    right = mergesort(a[mid:])

    # Cria uma nova lista para armazenar o resultado da fusão
    merged = []
    i = j = 0  # índices de controle das listas esquerda e direita

    # Enquanto houver elementos em ambas as listas
    while i < len(left) and j < len(right):
        # Compara o menor elemento de cada lado e adiciona o menor à lista final
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Se ainda restarem elementos em um dos lados, adiciona todos ao final
    merged.extend(left[i:])
    merged.extend(right[j:])

    # Retorna a lista fundida e ordenada
    return merged


# ---------- Função para executar o processo completo ----------
def run():
    data = read_input()
    print(f"Leitura concluída: {len(data)} números.")

    to_sort = data.copy()  # cria uma cópia da lista

    start = time.perf_counter()  # marca o tempo inicial

    # Executa o algoritmo
    result = mergesort(to_sort)

    end = time.perf_counter()  # marca o tempo final

    print(f"Tempo de ordenação (MergeSort): {end - start:.9f} s")
