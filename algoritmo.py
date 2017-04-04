def algoritmo_banqueiro():
	print("\n-----------------------------------------------------------------------------\n")
	quantidade_processo = input("\nQuantidade de processos: ")
	quantidade_recurso = input("\nQuantidade de recursos: ")
	Existentes = []
	Disponiveis = []
	Alocados = []
	Requeridos = []

	print("\n-----------------------------------------------------------------------------\n")
	for i in range(quantidade_recurso):
		quantidade = input("Quantidade de recursos existente do {} recurso: ".format(i+1))
		Existentes.append(quantidade)
	print("\n-----------------------------------------------------------------------------\n")
	for i in range(quantidade_recurso):
		quantidade = input("Quantidade de recursos disponivel do {} recurso: ".format(i+1))
		Disponiveis.append(quantidade)
	print("\n-----------------------------------------------------------------------------\n")
	for i in range(quantidade_processo):
		linha = []
		for j in range(quantidade_recurso):
			quantidade = input("Quantidade de recursos alocados do processo {}: ".format(i+1))
			linha.append(quantidade)
		Alocados.append(linha)
	print("\n-----------------------------------------------------------------------------\n")
	for i in range(quantidade_processo):
		linha = []
		for j in range(quantidade_recurso):
			quantidade = input("Quantidade de recursos requeridos do processo {}: ".format(i+1))
			linha.append(quantidade)
		Requeridos.append(linha)
	print("\n-----------------------------------------------------------------------------\n")

	print("Recurso existentes                  {}".format(Existentes))
	print("Recurso disponiveis                 {}".format(Disponiveis))
	for i in range(len(Alocados)):
		print("Recurso alocados do processo {}      {}".format(i+1,Alocados[i]))
	for i in range(len(Requeridos)):
		print("Recurso Requeridos do processo {}    {}".format(i+1,Requeridos[i]))
	print("\n-----------------------------------------------------------------------------\n")
	
def algoritmo_circular():
	print("\n---------------------------------------\n")
	processos = []

	quantidade = input("\nQuantidade de processos: ")
	quantum = input("\nValor do quantum: ")
	troca_de_contexto = input("\nValor da troca de contexto: ")
	tempo_total = 0
	print("\n---------------------------------------\n")
	for i in range(quantidade):
		tempo = input("Tempo do processo {}: ".format(i+1))
		processos.append(tempo)

	tempo_turnaround = [0]*quantidade
	tempo_espera = []
	copia_processos = processos[:]

	for i in range(quantidade):
		tempo_total += processos[i]

	tamanho = quantidade
	temp = 0
	passes = 0
	while(tempo_total >= 0):
		if(processos[temp] > quantum):
			if(tamanho == 1):
				for i in range(quantidade):
					if(processos[i] > 0):
						if(passes > quantidade):
							tempo_turnaround[i] += processos[i]
						else:
							tempo_turnaround[i] += processos[i]
				break
			else:
				for i in range(quantidade):
					if(processos[i] > 0):
						tempo_turnaround[i] += (quantum + troca_de_contexto)
				tempo_total -= quantum
				processos[temp] -= quantum
		else:
			if(tamanho == 1):
				for i in range(quantidade):
					if(processos[i] > 0):
						tempo_turnaround[i] += processos[i]
				break
			else:
				for i in range(quantidade):
					if(processos[i] > 0):
						if(i != temp):
							tempo_turnaround[i] += (processos[temp] + troca_de_contexto)
						else:
							tempo_turnaround[i] += processos[temp]
				processos[temp] -= processos[temp]
				tempo_total -= processos[temp]
				tamanho -= 1
		if(temp == quantidade-1):
			passes += 1
			temp = 0
		else:
			temp += 1	

	print("\n---------------------------------------\n")
	for i in range(len(tempo_turnaround)):
		print("Tempo de turnaround do processo {} : {} u.t".format(i+1,tempo_turnaround[i]))
	tempo_medio_turnaround = 0
	for i in range(len(tempo_turnaround)):
		tempo_medio_turnaround += tempo_turnaround[i]
	tempo_medio_turnaround = tempo_medio_turnaround / quantidade
	print("\nTempo medio de turnaround : {} u.t".format(tempo_medio_turnaround))
	print("\n---------------------------------------\n")
	for i in range(quantidade):
		tempo = tempo_turnaround[i] - copia_processos[i]
		tempo_espera.append(tempo)
	for i in range(len(tempo_espera)):
		print("Tempo de espera do processo {} : {} u.t".format(i+1,tempo_espera[i]))
	tempo_medio_espera = 0
	for i in range(len(tempo_espera)):
		tempo_medio_espera += tempo_espera[i]
	tempo_medio_espera = tempo_medio_espera / quantidade
	print("\nTempo medio de espera : {} u.t".format(tempo_medio_espera))

def main():
	algoritmo_banqueiro()
if __name__ == '__main__':
	main()