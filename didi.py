idade = int (input("digite sua idade:"))
print("voce vai ficar doido")
type(idade) 
idade=(idade+10)
moradia = list(input("onde voce mora:"))

menu = 0
 #inicio tratamento do switch case

#menu principal, para retorno
enquanto  menu  !=  5 :
    imprimir ()
    print ( "ESCOLHA NA LISTA A OPERAÇÃO DESEJADA:" )
    imprimir ()
    print ( "<1> - ADIÇÃO" )
    print ( "<2> - SUBTRAÇÃO" )
    print ( "<3> - DIVISÃO" )
    print ( "<4> - MULTIPLICAÇÃO" )
    print ( "<5> - SAIR DO PROGRAMA" )
    menu  =  int ( input ( "Digite sua escolha. \n " ))
 
     menu de jogo :
        
        #inicio tratamento do caso adição
        caso  1 :
            imprimir ()
            print ( "~ADIÇÃO~" )
            imprimir ()
            a  =  float ( input ( "Digito o primeiro valor: \n " ))
            imprimir ()
            b  =  float ( input ( "Digite o próximo valor: \n " ))
            soma  =  float ( a + b )
            print ( soma , "é o valor da soma." )
            imprimir ()
            looP  =  input ( "Pressione <ENTER> para voltar ao menu." )
            
        #inicio tratamento do caso subtração
        caso  2 :
            imprimir ()
            print ( "~SUBTRAÇÃO~" )
            imprimir ()
            a  =  float ( input ( "Digito o primeiro valor: \n " ))
            imprimir ()
            b  =  float ( input ( "Digite o próximo valor: \n " ))
            subt  =  flutuante ( a - b )
            print ( subt , "é o valor da subtração." )
            imprimir ()
            looP  =  input ( "Pressione <ENTER> para voltar ao menu." )
     
        #inicio tratamento do caso divisão
        caso  3 :
            imprimir ()
            print ( "~DIVISÃO~" )
            imprimir ()
            a  =  float ( input ( "Digito o primeiro valor: \n " ))
            imprimir ()
            b  =  float ( input ( "Digite o próximo valor: \n " ))
            diviS  =  float ( a / b )
            diviS  =  rodada ( diviS , 2 )
            print ( diviS , "é o valor da divisão." )
            imprimir ()
            looP  =  input ( "Pressione <ENTER> para voltar ao menu." )

        #inicio do tratamento do caso mutliplicação
        caso  4 :
            imprimir ()
            print ( "~MULTIPLICAÇÃO~" )
            imprimir ()
            a  =  float ( input ( "Digito o primeiro valor: \n " ))
            imprimir ()
            b  =  float ( input ( "Digite o próximo valor: \n " ))
            multP  =  float ( a * b )
            print ( multP , "é o valor da multiplicação." )
            imprimir ()
            looP  =  input ( "Pressione <ENTER> para voltar ao menu." )

#fim do switch case, e do algoritmo
senão :
    print ( "O programa foi executado com sucesso!" )
