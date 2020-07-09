pizzas = ['napolitana','especial','fugazetta']
pizzas_amigo = pizzas[:]

for pizza in pizzas:
    print(f"Me encanta la pizza {pizza.title()}.\n")

print("Como verán, me encanta la pizza!")

pizzas.append('roquefort')
pizzas_amigo.append('calabresa')

print("Mis pizzas favoritas son:")
print(pizzas)

print("Las pizzas favoritas de mi amigo son:")
print(pizzas_amigo)