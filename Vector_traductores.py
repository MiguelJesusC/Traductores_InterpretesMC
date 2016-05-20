import msvcrt
print ("***Bienvenido***\n")
print ("***Ingrese 3 numeros***\n")


for i in range(1):
	num=int (input("Ingrese numero:\n"))
	num2=int (input("Ingrese numero:\n"))
	num3=int (input("Ingrese numero:\n"))
	
	lista=[num,num2,num3]

	print ("Datos:",lista)
	if num>num2 and num>num3:
		print ("Este es el mayor\n",num)
		
	elif num2>num and num2>num3:
		print ("Este es el mayor\n",num2)
		
	else:
		print ("Este es el mayor\n",num3)
		
	if num<num2 and num<num3:
		print ("Este es el menor\n",num)
		
	elif num2<num and num2<num3:
		print ("Este es el menor\n",num2)
		
	else:
		print ("Este es el menor\n",num3)
		

    
msvcrt.getch()