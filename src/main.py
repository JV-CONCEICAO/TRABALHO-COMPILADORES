texto = input("Digite a entrada: ")
estado = 0
posicao = 0
lexema = ""

# Espaço no final aciona o case de verificação a frente e retrocesso
texto += " "

while estado in [0, 1, 2, 3, 4] and posicao < len(texto):
    caractere = texto[posicao]

    match estado:
        case 0: # Estado Inicial
            match caractere:
                case '-':
                    lexema += caractere
                    posicao += 1
                    estado = 1
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1
                    estado = 2
                case _:
                    posicao += 1

        case 1:
            match caractere:
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1
                    estado = 2
                case _:
                    # Reseta o AFD para continuar procurando na string.
                    estado = 0
                    # Não incrementa a posicao para este caractere ser reavaliado no estado 0.
                    lexema = ""


        case 2:
            match caractere:
                case ',':
                    lexema += caractere
                    posicao += 1
                    estado = 3
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1
                    estado = 2
                case _:
                    # Encontrou [outro]. Transição para o estado final 5.
                    estado = 5

        case 3:
            match caractere:
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1
                    estado = 4
                case _:
                    # Leu uma vírgula, mas não veio dígito depois.
                    # Descarta o que montou e volta a procurar.
                    estado = 0
                    lexema = ""

        case 4:
            match caractere:
                case c if c.isdigit():
                    lexema += caractere
                    posicao += 1
                    estado = 4
                case _:
                    # Encontrou [outro]. Transição para o estado final 5.
                    estado = 5

# Avaliação Final
if estado == 5:
    print(f"Token reconhecido: {lexema}")
else:
    print("Nenhum token reconhecido.")