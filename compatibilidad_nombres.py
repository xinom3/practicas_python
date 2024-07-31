name1 = 'Pierre Curie' #input("Cual es el nombre de tu pareja?\n")
name2 = 'Victoria Beckham' #input("Cual es tu nombre?\n")

#Tranformamos las mayusculas a minusculas con la funcion lower()
name1_text = name1.lower()
name2_text = name2.lower()
#estaban mal colocadas las variables hay que tener mas cuidado en ellas
names = name1_text+name2_text

T_count = names.count("t")
R_count = names.count("r")
U_count = names.count("u")
E_count = names.count("e")
count_true = str(T_count+R_count+U_count+E_count)

L_count = names.count("l")
O_count = names.count("o")
V_count = names.count("v")
E_count = names.count("e")
count_love = str(L_count+O_count+V_count+E_count)

compatibility = int(count_true+count_love)

if compatibility < 10 or compatibility > 90:
    print(f"Your score is {compatibility}, you go together like coke and mentos.") 

elif compatibility > 40 and compatibility < 50:
    print(f"Your score is {compatibility}, you are alright together.")

else: 
    print(f"Your score is {compatibility}.")