texto = input("Digite a entrada: ")
estado = 0
posicao = 0
lexema = "" # Variável para guardar o número que estamos montando

# Adicionamos um espaço no final da string. 
# Isso garante que a transição [outro] funcione se o número for a última coisa digitada.
texto += " " 

# Estrutura exata do "TIPO 2" da imagem do professor
while estado in [0, 1, 2, 3, 4] and posicao < len(texto):
    caractere = texto[posicao]
    match estado:
        case 0: # Estado Inicial
            match caractere:
                case '-':
                    lexema += caractere
                    posicao += 1 # avance entrada
                    estado = 1
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1 # avance entrada
                    estado = 2
                case _:
                    # Como ele quer ignorar lixo antes do número (ex: "var :="), 
                    # se não for dígito nem '-', apenas avançamos procurando o início.
                    posicao += 1 

        case 1:
            match caractere:
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1 # avance entrada
                    estado = 2
                case _:
                    print("Erro léxico: Sinal de menos solto.")
                    break
        case 2:
            match caractere:
                case ',':
                    lexema += caractere
                    posicao += 1 # avance entrada
                    estado = 3
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1 # avance entrada
                    estado = 2
                case _:
                    # Encontrou [outro]. Transição para o estado final 5.
                    # IMPORTANTE: Não colocamos 'posicao += 1' aqui!
                    estado = 5 

        case 3:
            match caractere:
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1 # avance entrada
                    estado = 4
                case _:
                    print("Erro léxico: Vírgula sem número depois.")
                    estado = -1 # Estado de erro
                    break

        case 4:
            match caractere:
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1 # avance entrada
                    estado = 4
                case _:
                    # Encontrou [outro]. Transição para o estado final 5.
                    estado = 5

if estado == 5:
    print(f"Token reconhecido: {lexema}")
else:
    print("Nenhum token reconhecido.")