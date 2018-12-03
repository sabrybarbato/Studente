class studente:
      def __init__ (self,nome,cognome,classe):
		self.nome=nome
		self.cognome=cognome
		self.classe=classe



alunni = []
S=" "
n=input ("quanti studenti vuoi inserire")
n=int (n)
for a in range(n):
 	nome =  input ("inserisci nome")
	cognome = input ("inserisci cognome")
	classe = input ("inserisci classe ")
	S=studente(nome,cognome,classe)
	alunni.append(S)
for alunno in alunni:
 	print (alunno.nome)
	print (alunno.cognome)
	print (alunno.classe)

