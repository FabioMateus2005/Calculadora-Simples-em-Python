def calcular():
    while True:
        print("\n--- CALCULADORA ---")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Encerrando...")
            break

        n1 = float(input("Primeiro número: "))
        n2 = float(input("Segundo número: "))

        if opcao == "1":
            print("Resultado:", n1 + n2)
        elif opcao == "2":
            print("Resultado:", n1 - n2)
        elif opcao == "3":
            print("Resultado:", n1 * n2)
        elif opcao == "4":
            if n2 != 0:
                print("Resultado:", n1 / n2)
            else:
                print("Erro: divisão por zero!")
        else:
            print("Opção inválida!")

calcular()
