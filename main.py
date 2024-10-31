from tkinter import Tk, ttk

# operações disponíveis nas calculadoras
from modulo_de_operacoes import *

# adicionar o caractere na calculadora simples
def adicionar_caractere(caractere):
    entrada.insert("end", caractere)

# função com o eval para calcular a expressão da calculadora simples
def calcular_simples():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, "end")
        entrada.insert("end", str(resultado))
    except Exception:
        entrada.delete(0, "end")
        entrada.insert("end", "Erro")
    except ValueError:
        entrada.delete(0, "end")
        entrada.insert("end", "Erro, entrada inválida")

# janela da calculadora simples
def frame_calculadora_simples(frame1):
    frame_principal.grid_forget()
    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()

    frame1.grid()
    root.title("Calculadora Simples")

    global entrada
    entrada = ttk.Entry(frame1, width=20)
    entrada.grid(row=0, column=0, columnspan=4)
    entrada.bind("<Return>", lambda event: calcular_simples())

    # criação dos botões numéricos e de operação
    botoes = [
        ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
        ('4', 4, 0), ('5', 4, 1), ('6', 4, 2),
        ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('0', 6, 1), ('.', 6, 2),
        ('+', 2, 0), ('-', 2, 1), ('*', 2, 2), ('/', 2, 3)
    ]

    for (text, row, col) in botoes:
        button = ttk.Button(frame1, text=text, command=lambda t=text: adicionar_caractere(t))
        button.grid(row=row, column=col)

    # botão de igual para calcular o resultado
    igual = ttk.Button(frame1, text="=", command=calcular_simples)
    igual.grid(row=6, column=3)

    # botão de limpar
    limpar = ttk.Button(frame1, text="Limpar", command=lambda: entrada.delete(0, "end"))
    limpar.grid(row=6, column=0)
    



# janela da calculadora matemática
def frame_calculadora_matematica(frame2):
    frame_principal.grid_forget()
    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()
    
    label_1.grid(column=0, row=1)
    entrada_1.grid(column=1, row=1)

    label_2.grid(column=0, row=2)
    entrada_2.grid(column=1, row=2)

    label_3.grid(column=0, row=3)
    entrada_3.grid(column=1, row=3)
    
    frame2.grid()
    root.title("Calculadora Matemática")

    # função para atualizar as labels das operações
    def atualizar_labels(funcao):
        
        global operacao_selecionada
        operacao_selecionada = funcao  # salvar a operação escolhida

        if funcao == "Exponenciação":
            label_1.config(text="Base:")
            label_2.config(text="Expoente:")
            label_3.config(text="---:")
        elif funcao == "Radiciação":
            label_1.config(text="Radicando:")
            label_2.config(text="Índice:")
            label_3.config(text="---:")
        elif funcao == "Porcentagem":
            label_1.config(text="Valor:")
            label_2.config(text="Porcentagem do Valor(%):")
            label_3.config(text="---:")
        elif funcao == "Fatorial":
            label_1.config(text="Fatorial de:")
            label_2.config(text="---:")
            label_3.config(text="---:")
        elif funcao == "Regra de 3 Simples Direta":
            label_1.config(text="Valor Inicial: ")
            label_2.config(text="Porcentagem Inicial(%):")
            label_3.config(text="Novo Valor:")
        elif funcao == "Regra de 3 Simples Inversa":
            label_1.config(text="Valor Inicial: ")
            label_2.config(text="Porcentagem Inicial(%):")
            label_3.config(text="Nova Porcentagem(%):")
        elif funcao == "Logaritmo":
            label_1.config(text="Logaritmando:")
            label_2.config(text="Base:")
            label_3.config(text="---:")

    # função para calcular o resultado com base na operação selecionada
    def calcular_resultado():
        try:
            valor1 = float(entrada_1.get())
            valor2 = float(entrada_2.get())
            valor3 = float(entrada_3.get())
            
            if operacao_selecionada == "Exponenciação":
                resultado = exponenciacao(valor1, valor2)
                descricao = "Exponenciação"
            elif operacao_selecionada == "Radiciação":
                resultado = radiciacao(valor1, valor2)
                descricao = "Radiciação"
            elif operacao_selecionada == "Porcentagem":
                resultado = porcentagem(valor1, valor2)
                descricao = "Porcentagem"
            elif operacao_selecionada == "Fatorial":
                resultado = fatorial(valor1)
                descricao = "Fatorial"
            elif operacao_selecionada == "Regra de 3 Simples Direta":
                resultado = regra_3_simples_direta(valor1, valor2, valor3)
                descricao = "Regra de 3 Simples Direta"
            elif operacao_selecionada == "Regra de 3 Simples Inversa":
                resultado = regra_3_simples_inversa(valor1, valor2, valor3)
                descricao = "Regra de 3 Simples Inversa"
            elif operacao_selecionada == "Logaritmo":
                resultado = logaritmo(valor1, valor2)
                descricao = "Logaritmo"
                
            else:
                resultado_label.config(text="Selecione uma operação.")
                return
            
            # exibir o resultado
            resultado_label.config(text=f"{descricao}: {resultado:.2f}")
        
        except ValueError:
            resultado_label.config(text="Insira valores válidos para o cálculo.")

    # botões para selecionar operação e calcular
    opcoes = [
        ("Exponenciação", 0, 5), ("Radiciação", 0, 6), ("Porcentagem", 0, 7), ("Fatorial", 0, 8),
        ("Regra de 3 Simples Direta", 1, 5), ("Regra de 3 Simples Inversa", 1, 6), ("Logaritmo", 1, 7)
        ]
    for (opcao, col, row) in opcoes:
        button = ttk.Button(frame2, text=opcao, command=lambda option=opcao: atualizar_labels(option))
        button.grid(row=row, column=col)

    ttk.Button(frame2, text="Calcular Resultado", command=calcular_resultado).grid(column=0, row=9, columnspan=2)

    # faz com que calcule o resultado ao pressionar enter
    entrada_1.bind("<Return>", lambda event: calcular_resultado())
    entrada_2.bind("<Return>", lambda event: calcular_resultado())
    entrada_3.bind("<Return>", lambda event: calcular_resultado())

    # rótulo para exibir o resultado
    resultado_label = ttk.Label(frame2, text="Resultado:")
    resultado_label.grid(column=0, row=10, columnspan=2)




# janela da calculadora financeira
def frame_calculadora_financeira(frame3):
    frame_principal.grid_forget()
    frame1.grid_forget()
    frame2.grid_forget()

    label_4.grid(column=0, row=1)
    entrada_4.grid(column=1, row=1)

    label_5.grid(column=0, row=2)
    entrada_5.grid(column=1, row=2)

    label_6.grid(column=0, row=3)
    entrada_6.grid(column=1, row=3)

    frame3.grid()
    root.title("Calculadora Financeira")
    
    # função para atualizar as labels das operações
    def atualizar_labels(funcao):
        global operacao_selecionada
        operacao_selecionada = funcao  # salvar a operação escolhida
        
        if funcao == "Valor Presente":
            label_4.config(text="Valor Futuro(R$):")
            label_5.config(text="Taxa de Juros(%):")
            label_6.config(text="Período(ano):")
        elif funcao == "Valor Futuro":
            label_4.config(text="Valor Presente(R$):")
            label_5.config(text="Taxa de Juros(%):")
            label_6.config(text="Período(ano):")
        elif funcao == "Taxa de Juros":
            label_4.config(text="Valor Presente(R$):")
            label_5.config(text="Valor Futuro(R$):")
            label_6.config(text="Período(ano):")
        elif funcao == "Período Composto":
            label_4.config(text="Valor Presente(R$):")
            label_5.config(text="Valor Futuro(R$):")
            label_6.config(text="Taxa de Juros(%):")
        elif funcao == "Pagamento por Anuidade":
            label_4.config(text="Valor Presente(R$):")
            label_5.config(text="Taxa de Juros(%):")
            label_6.config(text="Periodos(ano):")
        elif funcao == "Juros":
            label_4.config(text="Capital Inicial(R$): ")
            label_5.config(text="Taxa de Juros(%):")
            label_6.config(text="Tempo(ano):")
        elif funcao == "Juros Simples":
            label_4.config(text="Capital Inicial(R$):")
            label_5.config(text="Juros(%):")
            label_6.config(text="-------:")
        elif funcao == "Juros Compostos":
            label_4.config(text="Capital Inicial(R$):")
            label_5.config(text="Taxa de Juros(%):")
            label_6.config(text="Periodos(ano):")

    # função para calcular o resultado com base na operação selecionada
    def calcular_resultado():
        try:
            valor1 = float(entrada_4.get())
            valor2 = float(entrada_5.get())
            valor3 = float(entrada_6.get())
            
            if operacao_selecionada == "Valor Presente":
                resultado = valor_presente(valor1, valor2, valor3)
                descricao = "Valor Presente"
            elif operacao_selecionada == "Valor Futuro":
                resultado = valor_futuro(valor1, valor2, valor3)
                descricao = "Valor Futuro"
            elif operacao_selecionada == "Taxa de Juros":
                resultado = taxa_de_juros(valor1, valor2, valor3)
                descricao = "Taxa de Juros"
            elif operacao_selecionada == "Período Composto":
                resultado = periodo_composto(valor1, valor2, valor3)
                descricao = "Período Composto"
            elif operacao_selecionada == "Pagamento por Anuidade":
                resultado = pagamento_anuidade(valor1, valor2, valor3)
                descricao = "Pagamento por Anuidade"
            elif operacao_selecionada == "Juros":
                resultado = juros(valor1, valor2, valor3)
                descricao = "Juros"
            elif operacao_selecionada == "Juros Simples":
                resultado = juros_simples(valor1, valor2)
                descricao = "Juros Simples"
            elif operacao_selecionada == "Juros Compostos":
                resultado = juros_compostos(valor1, valor2, valor3)
                descricao = "Juros Compostos"
                
            else:
                resultado_label.config(text="Selecione uma operação.")
                return
            
            # exibir o resultado
            resultado_label.config(text=f"{descricao}: {resultado:.2f}")
        
        except ValueError:
            resultado_label.config(text="Insira valores válidos para o cálculo.")

    

    # botões para selecionar operação e calcular
    opcoes = [
        ("Valor Presente", 0, 5), ("Valor Futuro", 0, 6), ("Taxa de Juros", 0, 7), ("Período Composto", 0, 8),
        ("Pagamento por Anuidade", 1, 5), ("Juros", 1, 6), ("Juros Simples", 1, 7), ("Juros Compostos", 1, 8)
        ]
    for (opcao, col, row) in opcoes:
        button = ttk.Button(frame3, text=opcao, command=lambda option=opcao: atualizar_labels(option))
        button.grid(row=row, column=col)

    ttk.Button(frame3, text="Calcular Resultado", command=calcular_resultado).grid(column=0, row=10, columnspan=2)
    
    # faz com que calcule o resultado ao pressionar enter
    entrada_4.bind("<Return>", lambda event: calcular_resultado())
    entrada_5.bind("<Return>", lambda event: calcular_resultado())
    entrada_6.bind("<Return>", lambda event: calcular_resultado())

    # rótulo para exibir o resultado
    resultado_label = ttk.Label(frame3, text="Resultado:")
    resultado_label.grid(column=0, row=11, columnspan=2)


def limpar_grid():
    label_1.grid_forget()
    entrada_1.grid_forget()
    label_2.grid_forget()
    entrada_2.grid_forget()
    label_3.grid_forget()
    entrada_3.grid_forget()



# janela de menu
def frame_menu(frame_principal): # argumento
    frame_principal.grid_forget()  # esconder o frame principal
    frame1.grid_forget()  # esconder o frame 1
    frame2.grid_forget()  # esconder o frame 2
    frame3.grid_forget()  # esconder o frame 3

    frame_principal.grid()  # mostrar o frame passado como argumento
    root.title("Calculadoras") # definir o nome da guia


root = Tk()
root.title("Calculadora")

# janela principal
frame_principal = ttk.Frame(root, padding=10)
frame_principal.grid()

ttk.Label(frame_principal, text="Menu").grid(column=0, row=0, columnspan=2)
ttk.Button(frame_principal, text="Calculadora Simples", command=lambda: frame_calculadora_simples(frame1)).grid(column=0, row=1, columnspan=2)
ttk.Button(frame_principal, text="Calculadora Matemática", command=lambda: frame_calculadora_matematica(frame2)).grid(column=0, row=2, columnspan=2)
ttk.Button(frame_principal, text="Calculadora Financeira", command=lambda: frame_calculadora_financeira(frame3)).grid(column=0, row=3, columnspan=2)

# frame 1 = calculadora simples
frame1 = ttk.Frame(root, padding=10) # espaçamento de 10 para os cantos da janela
ttk.Label(frame1, text="Calculadora Simples").grid(column=0, row=0, columnspan=2)
ttk.Button(frame1, text="Voltar ao Menu", command=lambda: frame_menu(frame_principal)).grid(column=0, row=20, columnspan=2)


# frame 2 - calculadora matemática
frame2 = ttk.Frame(root, padding=10)
ttk.Label(frame2, text="Calculadora Matemática").grid(column=0, row=0, columnspan=2)
ttk.Button(frame2, text="Voltar ao Menu", command=lambda: (frame_menu(frame_principal), limpar_grid())).grid(column=0, row=20, columnspan=2)

label_1 = ttk.Label(frame2, text="Valor 1:")
label_1.grid(column=0, row=1)
entrada_1 = ttk.Entry(frame2)
entrada_1.grid(column=1, row=1)

label_2 = ttk.Label(frame2, text="Valor 2:")
label_2.grid(column=0, row=2)
entrada_2 = ttk.Entry(frame2)
entrada_2.grid(column=1, row=2)

label_3 = ttk.Label(frame2, text="Valor 3:")
label_3.grid(column=0, row=3)
entrada_3 = ttk.Entry(frame2)
entrada_3.grid(column=1, row=3)


# frame 3 - calculadora financeira
frame3 = ttk.Frame(root, padding=10) 
ttk.Label(frame3, text="Calculadora Financeira").grid(column=0, row=0, columnspan=2)
ttk.Button(frame3, text="Voltar ao Menu", command=lambda: (frame_menu(frame_principal), limpar_grid())).grid(column=0, row=20, columnspan=2)

label_4 = ttk.Label(frame3, text="Valor 1:")
label_4.grid(column=0, row=1)
entrada_4 = ttk.Entry(frame3)
entrada_4.grid(column=1, row=1)

label_5 = ttk.Label(frame3, text="Valor 2:")
label_5.grid(column=0, row=2)
entrada_5 = ttk.Entry(frame3)
entrada_5.grid(column=1, row=2)

label_6 = ttk.Label(frame3, text="Valor 3:")
label_6.grid(column=0, row=3)
entrada_6 = ttk.Entry(frame3)
entrada_6.grid(column=1, row=3)

root.mainloop()


""" finalizado em 427 linhas de código em 28/10/2024 """