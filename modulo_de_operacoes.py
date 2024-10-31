import math

# operações

def exponenciacao(base, expoente):
    return base ** expoente

def radiciacao(radicando, indice):
    return radicando ** (1/indice)

def porcentagem(numero, porcentagem):
    return (numero * porcentagem) / 100

def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

def regra_3_simples_direta(valor_inicial, porcentagem_inicial, novo_valor):
    return (porcentagem_inicial * novo_valor) / valor_inicial 

def regra_3_simples_inversa(valor_inicial, porcentagem_inicial, nova_porcentagem):
    return (valor_inicial * nova_porcentagem) / porcentagem_inicial 

def logaritmo(logaritmando, base):
    if logaritmando <= 0:
        raise ValueError("O logaritmo só é definido para números positivos.")
    if base <= 0 or base == 1:
        raise ValueError("A base deve ser maior que 0 e diferente de 1.")
    return math.log(logaritmando, base)

def valor_presente(valor_futuro, taxa_juros, periodos):
    return valor_futuro / (1 + (taxa_juros / 100)) ** periodos

def valor_futuro(valor_presente, taxa_juros, periodos):
    return valor_presente * (1 + (taxa_juros / 100)) ** periodos

def taxa_de_juros(valor_presente, valor_futuro, periodos):
    return ((valor_futuro - valor_presente) / (periodos * valor_presente)) * 100

def periodo_composto(valor_futuro, valor_presente, taxa_juros):
    return math.log(valor_presente / valor_futuro) / math.log(1 + (taxa_juros / 100))

def pagamento_anuidade(valor_presente, taxa_juros, periodos):
    return (valor_presente * taxa_juros) / (1 - (1 + (taxa_juros / 100)) ** - periodos)

def juros_simples(capital_inicial, juros):
    return capital_inicial + juros

def juros(capital_inicial, taxa_juros, tempo):
    return capital_inicial * (taxa_juros / 100) * tempo

def juros_compostos(capital_inicial, taxa_juros, periodos):
    return capital_inicial * (1 + (taxa_juros / 100)) ** periodos