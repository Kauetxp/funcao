def anoBi(ano):
    if ano%4 != 0:
        return False
    elif ano %100 !=0:
        return True
    elif ano %400 !=0:
        return False
    else:
        return True
    
# Anos para comparar

dadosTeste = [1900,2000,2016,1987,2020]

#Resultado

resultadosReais = [False,True,True,False,True]

#Checar função

for i in range(len(dadosTeste)):
    yr = dadosTeste[i]
    print(yr," -> ",end = "")
    result = anoBi(yr)
    if result == resultadosReais[i]:
        print("OK")
    else:
        print("Falha")

