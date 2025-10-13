# Importa o módulo 'time' para medir o tempo de execução do algoritmo.
import time

# Importa 'Path' da biblioteca 'pathlib' para lidar com caminhos de arquivos de forma mais segura e multiplataforma.
from pathlib import Path

# Define o caminho do arquivo que contém os números a serem ordenados.
# __file__ representa o caminho do arquivo atual (scripts/heapsort.py).
# .resolve() gera o caminho absoluto.
# .parents[1] sobe um nível de pasta (volta para o diretório pai do script).
# Em seguida, entra na pasta 'data' e pega o arquivo 'lista_desordenada.txt'.
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "lista_desordenada.txt"


# ---------- Função para ler os dados do arquivo ----------
def read_input():
    # Verifica se o arquivo realmente existe. Caso contrário, lança um erro.
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {DATA_FILE}")
    
    # Abre o arquivo em modo leitura com codificação UTF-8.
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        # Lê todo o conteúdo e remove espaços e quebras de linha extras.
        content = f.read().strip()
    
    # Se o arquivo estiver vazio, retorna uma lista vazia.
    if not content:
        return []
    
    # Substitui vírgulas por espaços, depois divide o texto em pedaços (tokens).
    # Isso permite aceitar tanto "1,2,3" quanto "1 2 3".
    parts = content.replace(",", " ").split()
    
    # Converte cada token para inteiro e retorna a lista de números.
    return [int(p) for p in parts]


# ---------- Função auxiliar do HeapSort ----------
# Essa função é chamada de "sift down" (ou "afundar"), e ajusta o heap.
def _sift_down(a, start, end):
    root = start  # Começa pela raiz do sub-heap.
    while True:
        # Calcula o índice do filho esquerdo (fórmula: 2*i + 1).
        child = 2 * root + 1

        # Se o índice do filho for maior que o final do heap, paramos.
        if child > end:
            break

        # Verifica se o filho direito existe e é maior que o filho esquerdo.
        # Se for, usamos o filho direito como referência para a troca.
        if child + 1 <= end and a[child] < a[child + 1]:
            child += 1

        # Se o filho for maior que o pai (root), fazemos a troca.
        if a[root] < a[child]:
            a[root], a[child] = a[child], a[root]
            # Depois da troca, o elemento desce e continua o processo.
            root = child
        else:
            # Caso contrário, o heap já está ajustado.
            break


# ---------- Função principal do HeapSort ----------
def heapsort_inplace(a):
    n = len(a)  # Pega o tamanho da lista.

    # --- Etapa 1: Construção do heap máximo ---
    # Começa do último nó que tem filhos até a raiz (índice 0).
    # range((n-2)//2, -1, -1) percorre todos os nós internos de trás para frente.
    for start in range((n - 2) // 2, -1, -1):
        _sift_down(a, start, n - 1)

    # --- Etapa 2: Extração dos elementos do heap ---
    # Move o maior elemento (no topo do heap) para o final da lista.
    for end in range(n - 1, 0, -1):
        # Troca o primeiro (maior) com o último elemento não ordenado.
        a[end], a[0] = a[0], a[end]
        # Ajusta o heap novamente, ignorando o elemento já ordenado.
        _sift_down(a, 0, end - 1)


# ---------- Função para executar o processo completo ----------
def run():
    # Lê os dados do arquivo.
    data = read_input()
    print(f"Leitura concluída: {len(data)} números.")

    # Cria uma cópia para ordenar (mantém os dados originais intactos).
    to_sort = data.copy()

    # Marca o tempo inicial.
    start = time.perf_counter()

    # Só executa se houver números.
    if to_sort:
        heapsort_inplace(to_sort)

    # Marca o tempo final.
    end = time.perf_counter()

    # Exibe o tempo total gasto na ordenação.
    print(f"Tempo de ordenação (HeapSort): {end - start:.9f} s")
