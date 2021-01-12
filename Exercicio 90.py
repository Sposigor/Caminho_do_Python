aluno = {}
while True:
	aluno["nome"] = str(input("Nome: "))
	aluno["média"] = float(input("Média: "))
	if aluno["média"] < 7.5:
		aluno["situação"] = "está reprovado"
	else:
		aluno["situação"] = "está aprovado"
	break
print("o nome do(a) aluno(a) é",aluno["nome"].title(),"e a média da nota é",aluno["média"],"e ele(a)",aluno["situação"])