import tkinter as tk
from tkinter import ttk

# Funções de conversão
def converter():
    try:
        valor = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        # Dicionário de conversões
        conversions = {
            "Área": {
                "m²": 1,
                "km²": 1e6,
                "ha": 1e4,
                "ft²": 0.092903,
            },
            "Taxa de Transferência de Dados": {
                "bps": 1,
                "kbps": 1e3,
                "Mbps": 1e6,
                "Gbps": 1e9,
            },
            "Armazenamento Digital": {
                "B": 1,
                "KB": 1e3,
                "MB": 1e6,
                "GB": 1e9,
                "TB": 1e12,
            },
            "Frequência": {
                "Hz": 1,
                "kHz": 1e3,
                "MHz": 1e6,
                "GHz": 1e9,
            },
            "Economia de Combustível": {
                "km/L": 1,
                "L/100km": 1 / 100,
            },
            "Comprimento": {
                "m": 1,
                "km": 1e3,
                "cm": 0.01,
                "mm": 0.001,
                "ft": 0.3048,
                "in": 0.0254,
            },
            "Massa": {
                "kg": 1,
                "g": 0.001,
                "mg": 1e-6,
                "lb": 0.453592,
            },
            "Ângulo Plano": {
                "graus": 1,
                "radianos": 57.2958,
            },
            "Pressão": {
                "Pa": 1,
                "kPa": 1e3,
                "bar": 1e5,
                "atm": 101325,
            },
            "Velocidade": {
                "m/s": 1,
                "km/h": 3.6,
                "mi/h": 2.237,
            },
            "Temperatura": {
                "Celsius": lambda c: c,
                "Fahrenheit": lambda c: (c * 9/5) + 32,
                "Kelvin": lambda c: c + 273.15,
            },
            "Tempo": {
                "segundos": 1,
                "minutos": 60,
                "horas": 3600,
                "dias": 86400,
            },
            "Volume": {
                "L": 1,
                "mL": 0.001,
                "gal": 3.78541,
                "ft³": 28.3168,
            }
        }

        if from_unit in conversions[category]:
            if callable(conversions[category][from_unit]):
                intermediate_value = conversions[category][from_unit](valor)
            else:
                intermediate_value = valor * conversions[category][from_unit]

            if callable(conversions[category][to_unit]):
                result = conversions[category][to_unit](intermediate_value)
            else:
                result = intermediate_value / conversions[category][to_unit]

            # Verifica se o resultado é inteiro ou decimal e formata a saída
            if result.is_integer():
                result_text = f"Resultado: {int(result)} {to_unit}"
            else:
                result_text = f"Resultado: {result:.6f} {to_unit}"

            label_result.config(text=result_text)
    except ValueError:
        label_result.config(text="Por favor, insira um valor numérico válido.")

# Função para atualizar as unidades
def update_units(event):
    global category
    category = combo_category.get()
    combo_from['values'] = list(conversions[category].keys())
    combo_to['values'] = list(conversions[category].keys())

# Dicionário de categorias
category = "Área"
conversions = {
    "Área": {
        "m²": 1,
        "km²": 1e6,
        "ha": 1e4,
        "ft²": 0.092903,
    },
    "Taxa de Transferência de Dados": {
        "bps": 1,
        "kbps": 1e3,
        "Mbps": 1e6,
        "Gbps": 1e9,
    },
    "Armazenamento Digital": {
        "B": 1,
        "KB": 1e3,
        "MB": 1e6,
        "GB": 1e9,
        "TB": 1e12,
    },
    "Frequência": {
        "Hz": 1,
        "kHz": 1e3,
        "MHz": 1e6,
        "GHz": 1e9,
    },
    "Economia de Combustível": {
        "km/L": 1,
        "L/100km": 1 / 100,
    },
    "Comprimento": {
        "m": 1,
        "km": 1e3,
        "cm": 0.01,
        "mm": 0.001,
        "ft": 0.3048,
        "in": 0.0254,
    },
    "Massa": {
        "kg": 1,
        "g": 0.001,
        "mg": 1e-6,
        "lb": 0.453592,
    },
    "Ângulo Plano": {
        "graus": 1,
        "radianos": 57.2958,
    },
    "Pressão": {
        "Pa": 1,
        "kPa": 1e3,
        "bar": 1e5,
        "atm": 101325,
    },
    "Velocidade": {
        "m/s": 1,
        "km/h": 3.6,
        "mi/h": 2.237,
    },
    "Temperatura": {
        "Celsius": lambda c: c,
        "Fahrenheit": lambda c: (c * 9/5) + 32,
        "Kelvin": lambda c: c + 273.15,
    },
    "Tempo": {
        "segundos": 1,
        "minutos": 60,
        "horas": 3600,
        "dias": 86400,
    },
    "Volume": {
        "L": 1,
        "mL": 0.001,
        "gal": 3.78541,
        "ft³": 28.3168,
    }
}

# Configuração da GUI
root = tk.Tk()
root.title("Conversor de Unidades")
root.geometry("450x300")

# Adiciona estilo
style = ttk.Style(root)
style.theme_use('clam')  # Define um tema mais moderno

style.configure("TLabel", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TCombobox", font=("Helvetica", 12))

# Frame principal
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Seleção de categoria
ttk.Label(frame, text="Categoria:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
combo_category = ttk.Combobox(frame, values=list(conversions.keys()), state="readonly")
combo_category.bind("<<ComboboxSelected>>", update_units)
combo_category.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
combo_category.current(0)

# Entrada de valor
ttk.Label(frame, text="Valor:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_value = ttk.Entry(frame)
entry_value.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Unidades de origem
ttk.Label(frame, text="De:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
combo_from = ttk.Combobox(frame, state="readonly")
combo_from.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Unidades de destino
ttk.Label(frame, text="Para:").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
combo_to = ttk.Combobox(frame, state="readonly")
combo_to.grid(row=3, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

update_units(None)  # Atualiza as unidades iniciais

# Botão de conversão
button_convert = ttk.Button(frame, text="Converter", command=converter)
button_convert.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

# Label para resultado
label_result = ttk.Label(frame, text="Resultado:")
label_result.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Ajusta o layout
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
