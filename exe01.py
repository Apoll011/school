"""
O exercício era para fazer um programa em que o utilizador entrava com um data nesse formato DD/MM/AAAA e depois cria três variáveis para guardar o dia o ano e o mês dessa data.
Antes disso ver se as variáveis são numéricas e imprimir a data na tela no mesmo formato
"""

def parseDate(date: str):
	dateSplited = date.split("/")
	try:
		year = int(dateSplited[2])
		month = int(dateSplited[1])
		day = int(dateSplited[0])
		
		print(f"A data foi: {day}/{month}/{year}")
    
    	return day, month, year
	except Exception as e:
		print(e)


data = input("Insira uma data")
dia, mes, ano = parseDate(data)