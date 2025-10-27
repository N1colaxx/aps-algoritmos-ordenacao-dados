# imports
import os
import sys
import importlib
import time
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = BASE_DIR / "scripts"
RESULTS_FILE = BASE_DIR / "resultados.xlsx"
GRAFICO_FILE = BASE_DIR / "grafico_medias.png"

sys.path.insert(0, str(SCRIPTS_DIR))

AVAILABLE = {
    "1": ("quicksort", "QuickSort"),
    "2": ("mergesort", "MergeSort"),
    "3": ("heapsort", "HeapSort")
}


def salvar_resultado_excel(algoritmo: str, tempo_execucao: float):
    """Salva o tempo no Excel e atualiza o gráfico de médias."""
    dados = {
        "Algoritmo": [algoritmo],
        "Tempo (s)": [tempo_execucao],
        "Data/Hora": [datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
    }

    df_novo = pd.DataFrame(dados)

    if RESULTS_FILE.exists():
        df_existente = pd.read_excel(RESULTS_FILE)
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
    else:
        df_final = df_novo

    df_final.to_excel(RESULTS_FILE, index=False)

    print(f"📊 Resultado salvo em: {RESULTS_FILE.name}")
    gerar_grafico_medias(df_final)

def gerar_grafico_medias(df):
    """Gera e salva um gráfico de médias de tempo de cada algoritmo."""
    medias = df.groupby("Algoritmo")["Tempo (s)"].mean().sort_values()

    plt.figure(figsize=(7, 5))
    barras = plt.bar(medias.index, medias.values, color='black')

    plt.title("Tempo médio das execuções", fontsize=15)
    plt.ylabel("Tempo médio (segundos)")
    plt.xlabel("Algoritmo")

    # Adiciona os valores acima das barras
    for barra in barras:
        plt.text(barra.get_x() + barra.get_width()/2,
                 barra.get_height(),
                 f"{barra.get_height():.4f}s",
                 ha='center', va='bottom',
                 color='black', fontsize=9, fontweight='bold')  

    plt.tight_layout()
    plt.savefig(GRAFICO_FILE)
    plt.close()
    print(f"📈 Gráfico de médias atualizado: {GRAFICO_FILE.name}")


def run_script(option: str):
    if option not in AVAILABLE:
        print("⚠️ Opção inválida.")
        return

    module_name, label = AVAILABLE[option]

    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        print(f"❌ Erro ao importar o script '{module_name}': {e}")
        return

    if not hasattr(module, "run"):
        print(f"❌ O módulo '{module_name}' não possui a função run().")
        return

    print(f"\n--- {label} ---")

    try:
        inicio = time.perf_counter()
        module.run()
        fim = time.perf_counter()

        tempo_exec = fim - inicio
        print(f"✅ Tempo de execução: {tempo_exec:.6f} segundos")

        salvar_resultado_excel(label, tempo_exec)

    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")


def main():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        for k, (_, label) in AVAILABLE.items():
            print(f"{k} - {label}")
        print("0 - Sair")

        opc = input("Escolha uma opção: ").strip()

        if opc == "0":
            print("Saindo...")
            break

        if opc not in AVAILABLE:
            print("⚠️ Entrada inválida! Digite um número entre 0 e 3.")
            continue

        run_script(opc)


if __name__ == "__main__":
    main()
