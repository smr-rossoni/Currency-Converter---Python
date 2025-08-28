# Currency Converter in Python

def converter_moeda(valor, de_moeda, para_moeda):
    # Taxas de câmbio fixas (exemplo)
    taxas = {
        "BRL": {"USD": 0.20, "EUR": 0.18, "BRL": 1},
        "USD": {"BRL": 5.0, "EUR": 0.90, "USD": 1},
        "EUR": {"BRL": 5.5, "USD": 1.1, "EUR": 1}
    }

    if de_moeda not in taxas or para_moeda not in taxas[de_moeda]:
        return None
    
    return valor * taxas[de_moeda][para_moeda]

def main():
    print("=== CONVERSOR DE MOEDAS ===")
    valor = float(input("Digite o valor: "))
    de_moeda = input("De qual moeda? (BRL, USD, EUR): ").upper()
    para_moeda = input("Para qual moeda? (BRL, USD, EUR): ").upper()

    resultado = converter_moeda(valor, de_moeda, para_moeda)
    if resultado is None:
        print("Moeda inválida!")
    else:
        print(f"{valor} {de_moeda} = {resultado:.2f} {para_moeda}")

if __name__ == "__main__":
    main()
