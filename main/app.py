# imports
import os
import sys
import importlib # permite importe importar modulos dinamicamente em tempo de execução
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1] # cria um caminho absoluto para a "origem" do progeto: aps_algotimos_estrutura_dados
SCRIPTS_DIR = BASE_DIR / "scripts" # acessa o PATH da pasta scripts 
sys.path.insert(0, str(SCRIPTS_DIR)) # aqui deixo o PATH da pasta scripts como prioridade, assim quando alguem requisitar um moduli, ja vai direto nela

AVAILABLE = {
#   opc |    script | aparace para o USER
    "1": ("quicksort", "QuickSort"),
    "2": ("mergesort", "MergeSort"),
    "3": ("heapsort", "HeapSort")
}

def run_script(option: str):
    if option not in AVAILABLE:
        print("⚠️ Opção inválida.")
        return
    
    # module_name -> script que vai executar
    # label -> o nome do script q vai executar
    # AVAILABLE -> as opcões de algoritmos
    # option -> armazena a opcão que digitou  
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
        module.run()
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
