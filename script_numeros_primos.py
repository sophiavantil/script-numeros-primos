def numero_primo(numero_verificar):
    if numero_verificar <= 1:
        return False
    
    for divisor in range(2, int(numero_verificar**0.5) + 1):
        if numero_verificar % divisor == 0:
            return False
        
    return True

with open("results.txt", "w") as arquivo:
    for numero in range(1, 251):
        if numero_primo(numero):
            arquivo.write(str(numero) + "\n")
