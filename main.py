def somar():
    print("Digite numeros a serem somados: ")
    x = input()
    y = input()
    resultado = x + y
    print x,"+",y,"=", resultado
    return 0; 

def subtrair():
    print("Digite numeros a serem subtraidos: ")
    x = input()
    y = input()
    resultado = x - y
    print x,"-",y,"=", resultado
    return 0;

def dividir():
    print("Digite numeros a serem divididos: ")
    x = input()
    y = input()
    resultado = x / y
    print x,"/",y,"=", resultado
    return 0;

def multiplicar():
    print("Digite numeros a serem multiplicados: ")
    x = input()
    y = input()
    resultado = x * y
    print x,"*",y,"=", resultado
    return 0;

print("Ola, seja bem vindo a calculadora do Yan");
print("Por favor, escolha alguma das opcoes abaixo");

print("1: Adicao\n2: Subtracao\n3: Divisao\n4: Multiplicacao")

print("Deseja fazer outra operacao? S/N": )
continuar = input();

option =  input();
print "Voce escolheu: ", option

if option == 1:
    somar()

if option == 2:
    subtrair()

if option == 3:
    dividir()
    
if option == 4:
    multiplicar()

if option != 1 or 2 or 3 or 4:
    print "Escolha uma opcao valida"
    option = input();