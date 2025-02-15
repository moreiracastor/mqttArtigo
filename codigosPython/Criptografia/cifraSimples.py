# Função que criptografe uma string com base na cifra Atbash
# As frases devem ser escrita com as suas letras contrárias, a = z : b = y : c = x ..... 

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alfaInvert = alfabeto[::-1]

desCripto = []


def cripto(string="", selecao=0):
    indexString = []
    criptoString = []

    # -------------Criptografia-------------
    for x in string.lower():
        indexString.append(alfaInvert.index(x))


    if selecao == 0:
        for x in indexString:
            criptoString.append(alfabeto[x])

        return "".join(criptoString)
    else:
        # -------------Descriptografia-------------
        for x in indexString:
            desCripto.append(alfaInvert[x])

        return "".join(desCripto)
