print("digite seu peso")
peso = float(input())
print("digite sua altura")
altura = float(input())


imc = peso / (altura * altura)
if imc < 18.5:
    print (imc)
    print("Peso baixo")
elif imc > 18.5 and imc < 24.9:
    print (imc)
    print("Peso normal")
elif imc > 25.0 and imc < 29.9:
    print (imc)
    print("Sobrepeso")
elif imc > 30:
    print (imc)
    print("obesidade")
