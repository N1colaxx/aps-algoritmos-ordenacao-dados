# === IMPORTAÇÕES DE BIBLIOTECAS ===
import os                     # Fornece funções para interagir com o sistema operacional
import sys                    # Permite manipular o sistema e o interpretador (ex: caminhos de módulos)
import importlib              # Usado para importar módulos dinamicamente em tempo de execução
import time                   # Usado para medir o tempo de execução de algoritmos
from pathlib import Path      # Facilita o trabalho com caminhos de arquivos e diretórios
import pandas as pd           # Biblioteca para manipulação de dados em tabelas
import matplotlib.pyplot as plt  # Biblioteca para criar gráficos
from datetime import datetime # Para capturar data e hora atuais

# === DEFINIÇÃO DE CAMINHOS BASE ===
BASE_DIR = Path(__file__).resolve().parents[1]  # Caminho da pasta "pai" do arquivo atual
SCRIPTS_DIR = BASE_DIR / "scripts"              # Caminho da pasta onde estão os scripts de algoritmos
RESULTS_FILE = BASE_DIR / "resultados.xlsx"     # Caminho do arquivo Excel onde os resultados são salvos
GRAFICO_FILE = BASE_DIR / "grafico_medias.png"  # Caminho do arquivo de imagem do gráfico

# Adiciona a pasta 'scripts' ao caminho de módulos do Python
sys.path.insert(0, str(SCRIPTS_DIR))

# Dicionário com as opções de algoritmos disponíveis
AVAILABLE = {
    "1": ("quicksort", "QuickSort"),
    "2": ("mergesort", "MergeSort"),
    "3": ("heapsort", "HeapSort")
}


# === FUNÇÃO PARA SALVAR RESULTADOS NO EXCEL ===
def salvar_resultado_excel(algoritmo: str, tempo_execucao: float):
    """Salva o tempo de execução no arquivo Excel e atualiza o gráfico de médias."""
    
    # Cria um dicionário com os dados da execução
    dados = {
        "Algoritmo": [algoritmo],
        "Tempo (s)": [tempo_execucao],
        "Data/Hora": [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]  # Data e hora formatadas
    }

    # Converte o dicionário em um DataFrame (tabela)
    df_novo = pd.DataFrame(dados)

    # Se o arquivo de resultados já existir, ele é lido e atualizado
    if RESULTS_FILE.exists():
        df_existente = pd.read_excel(RESULTS_FILE)
        # Junta os dados novos aos antigos
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
    else:
        # Se o arquivo não existe, cria um novo
        df_final = df_novo

    # Salva a tabela atualizada no Excel
    df_final.to_excel(RESULTS_FILE, index=False)

    print(f"📊 Resultado salvo em: {RESULTS_FILE.name}")

    # Atualiza o gráfico de médias com os novos dados
    gerar_grafico_medias(df_final)


# === FUNÇÃO PARA GERAR GRÁFICO DE MÉDIAS ===
def gerar_grafico_medias(df):
    """Gera e salva um gráfico mostrando o tempo médio de execução de cada algoritmo."""
    
    # Calcula a média dos tempos de execução por algoritmo
    medias = df.groupby("Algoritmo")["Tempo (s)"].mean().sort_values()

    # Define o tamanho da figura
    plt.figure(figsize=(7, 5))
    
    # Cria as barras do gráfico (cor preta)
    barras = plt.bar(medias.index, medias.values, color='black')

    # Define título e rótulos dos eixos
    plt.title("Tempo médio das execuções", fontsize=15)
    plt.ylabel("Tempo médio (segundos)")
    plt.xlabel("Algoritmo")

    # Adiciona o valor de cada barra acima dela
    for barra in barras:
        plt.text(barra.get_x() + barra.get_width()/2,  # posição X central da barra
                 barra.get_height(),                   # altura da barra
                 f"{barra.get_height():.4f}s",         # valor formatado (4 casas decimais)
                 ha='center', va='bottom',             # alinhamento horizontal e vertical
                 color='black', fontsize=9, fontweight='bold')  

    # Ajusta o layout e salva o gráfico em arquivo
    plt.tight_layout()
    plt.savefig(GRAFICO_FILE)
    plt.close()

    print(f"📈 Gráfico de médias atualizado: {GRAFICO_FILE.name}")


# === FUNÇÃO PARA EXECUTAR O SCRIPT ESCOLHIDO ===
def run_script(option: str):
    """Executa o algoritmo escolhido pelo usuário e mede seu tempo."""
    
    if option not in AVAILABLE:
        print("⚠️ Opção inválida.")
        return

    # Obtém o nome do módulo (arquivo .py) e o rótulo amigável
    module_name, label = AVAILABLE[option]

    try:
        # Importa dinamicamente o módulo (ex: quicksort.py)
        module = importlib.import_module(module_name)
    except Exception as e:
        print(f"❌ Erro ao importar o script '{module_name}': {e}")
        return

    # Verifica se o módulo possui uma função chamada run()
    if not hasattr(module, "run"):
        print(f"❌ O módulo '{module_name}' não possui a função run().")
        return

    print(f"\n--- {label} ---")

    try:
        # Marca o início da execução
        inicio = time.perf_counter()

        # Executa o algoritmo (função run() do script)
        module.run()

        # Marca o final e calcula o tempo total
        fim = time.perf_counter()
        tempo_exec = fim - inicio

        print(f"✅ Tempo de execução: {tempo_exec:.6f} segundos")

        # Salva o resultado no Excel e atualiza o gráfico
        salvar_resultado_excel(label, tempo_exec)

    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")


# === FUNÇÃO PRINCIPAL (MENU INTERATIVO) ===
def main():
    """Exibe o menu principal e permite ao usuário escolher o algoritmo para executar."""
    
    while True:
        print("\n===== MENU PRINCIPAL =====")
        for k, (_, label) in AVAILABLE.items():
            print(f"{k} - {label}")
        print("0 - Sair")

        # Solicita a escolha do usuário
        opc = input("Escolha uma opção: ").strip()

        # Encerra o programa
        if opc == "0":
            print("Saindo...")
            break

        # Valida entrada
        if opc not in AVAILABLE:
            print("⚠️ Entrada inválida! Digite um número entre 0 e 3.")
            continue

        # Executa o algoritmo selecionado
        run_script(opc)


# === PONTO DE ENTRADA DO PROGRAMA ===
if __name__ == "__main__":
    main()
