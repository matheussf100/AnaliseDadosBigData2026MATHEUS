import sys
import pandas as pd
import numpy as np

# A convenção é "import pandas as pd"
try:
    import pandas as pd
    print("Tentando importar a biblioteca Pandas...")
    print("Pandas importado com sucesso!")

    # É uma boa prática verificar a versão
    print(f"Versão do pandas instalada: {pd.__version__}")
    print(f"Versão do Python: {sys.version.split()[0]}")

except ImportError:
    print("\n--- ERRO ---")
    print("A biblioteca Pandas não foi encontrada. ")
    print("Por favor, instale-a usando o comando no seu terminal:")
    print("pip install pandas")