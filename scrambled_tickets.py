input_cities = [
    ['Chennai', 'Bangalore'], 
    ['Bombay', 'Delhi'], 
    ['Goa', 'Chennai'], 
    ['Delhi', 'Goa'], 
    ['Bangalore', 'Beijing']
]


def sort_tickets(tickets):

	temp_tickets = tickets
	for index, element in enumerate(temp_tickets):
		print('Outer')
		t = tickets.pop(index)
		target = t[1]

		for inner_i, inner_e in enumerate(temp_tickets):
			print('Inner')
			if inner_e[0] == target:
				temp_tickets.insert(inner_i - 1, t)

		# Need else case
		# temp_tickets.insert(len(temp_tickets) - 1, t)

	return temp_tickets

output = sort_tickets(input_cities)
print(output)
