def calcular_calorias(peso, altura, idade, genero, nivel_atividade):
    if genero == 'masculino':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    elif genero == 'feminino':
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)
    else:
        raise ValueError("Gênero deve ser 'masculino' ou 'feminino'.")

    fatores_atividade = {
        'sedentario': 1.2,
        'leve': 1.375,
        'moderado': 1.55,
        'intenso': 1.725
    }

    if nivel_atividade not in fatores_atividade:
        raise ValueError("Nível de atividade deve ser 'sedentario', 'leve', 'moderado' ou 'intenso'.")

    calorias_totais = tmb * fatores_atividade[nivel_atividade]
    return calorias_totais


def criar_dieta(calorias, objetivo):
    if objetivo == 'perder_peso':
        calorias -= 500
    elif objetivo == 'ganhar_peso':
        calorias += 500
    elif objetivo != 'manter_peso':
        raise ValueError("Objetivo deve ser 'perder_peso', 'manter_peso' ou 'ganhar_peso'.")

    proteinas = calorias * 0.3 / 4
    carboidratos = calorias * 0.5 / 4
    gorduras = calorias * 0.2 / 9

    return {
        'calorias': round(calorias),
        'proteinas': round(proteinas),
        'carboidratos': round(carboidratos),
        'gorduras': round(gorduras)
    }


def main():
    print("Bem-vindo ao Gerador de Dietas!")
    try:
        peso = float(input("Digite seu peso (kg): "))
        altura = float(input("Digite sua altura (cm): "))
        idade = int(input("Digite sua idade: "))
        genero = input("Digite seu gênero (masculino/feminino): ").strip().lower()
        nivel_atividade = input("Digite seu nível de atividade (sedentario/leve/moderado/intenso): ").strip().lower()
        objetivo = input("Digite seu objetivo (perder_peso/manter_peso/ganhar_peso): ").strip().lower()

        calorias = calcular_calorias(peso, altura, idade, genero, nivel_atividade)
        dieta = criar_dieta(calorias, objetivo)

        print("\nPlano de dieta personalizado:")
        print(f"Calorias: {dieta['calorias']} kcal")
        print(f"Proteínas: {dieta['proteinas']} g")
        print(f"Carboidratos: {dieta['carboidratos']} g")
        print(f"Gorduras: {dieta['gorduras']} g")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
