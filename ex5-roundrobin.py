# Algoritmo para simulação de escalonamento de processos
# Round Robin

processos = [
  {"nome": "P1", "chegada": 0, "execucao": 5, "resposta": None, "fim": None},
  {"nome": "P2", "chegada": 1, "execucao": 3, "resposta": None, "fim": None},
  {"nome": "P3", "chegada": 2, "execucao": 6, "resposta": None, "fim": None},
]

tempo = 0
quantum = 2
cont_quantum = 0
p_finalizados = 0
ordem_execucao = []
fila = []

# Início do Escalonamento
while True: 
  # Adição na fila
  for p in processos: 
    if p["chegada"] <= tempo and p["execucao"] > 0 and p not in fila:
      fila.append(p)

  # Execução do quantum
  if cont_quantum == quantum:
    troca_de_processo = fila.pop(0)
    fila.append(troca_de_processo)
    cont_quantum = 0

  if len(fila) == 0:
    tempo += 1
    continue 

  # Registro do tempo de resposta
  if fila[0]['resposta'] == None:
    fila[0]['resposta'] = tempo

  fila[0]['execucao'] -= 1

  if len(ordem_execucao)==0 or fila[0]['nome'] != ordem_execucao[-1]:
    ordem_execucao.append(fila[0]['nome'])

  tempo += 1

  # Remove da fila o processo finalizado
  if fila[0]['execucao'] == 0:
    fila[0]['fim'] = tempo
    fila.pop(0)
    p_finalizados += 1
    cont_quantum = 0
  else:
    cont_quantum += 1

  if p_finalizados == len(processos):
    break
      
TMR = sum(p["resposta"] for p in processos) / len(processos)

print(f'\nOrdem de execução: {ordem_execucao}')
for p in processos:
  print(f'Tempo de resposta {p["nome"]}: {p["resposta"]}')
print(f'Tempo médio de resposta: {round(TMR, 2)}\n')