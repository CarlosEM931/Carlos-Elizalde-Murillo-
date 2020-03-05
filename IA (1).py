username = 'Charly'
level = 0
musica = None
rock= None
pop=None
rap= None

print(f'Hello, {username}' )

# Ask user input
print("Te hare algunas preguntas sobre la musica que te gusta, para ver si eres un melomano de verdad (Sino quieres contestar entonces no lo eres)")
print(" ")
print("Comencemos")
print(" ")
musica=input(' ')
if(musica != ''):
	level = level + 1
print(" El ser humano no puede vivir sin musica, asi que si quieres puedes decirme cuanto te gusta,sino solo presiona enter")
rock = input('Ahora dinos que banda de de rock te gusta mas, Metallica, Nirvana o Panda ')
if(rock != ''):
	if rock == 'Metallica':
		level = level + 1
	elif rock == 'Nirvana':
		level = level + 1
	elif rock == 'Panda':
		print(f'Come onb({str_gender})! No sabes de musica amigo')
	else:
		print(f'({rock}) No existe en mi base de datos ')
print(" ")
pop= input('Ahora dinos que banda de pop o cantante te gusta')
if pop != '':
	level = level + 1
print(" ")
rap= input('Por ultimo dinos si te gusta el rap,sino,presiona enter')
if rap != '':
	level = level + 1
print(" ")
# Selection of the response
if level == 0:
	print( f'No sabes nada sobre buena musica ')
elif level <4:
	print( f' Te gusta buena musica pero no eres melomano')
else:
	print( f"Gracias{username}. Vaya que eres un melomano" )