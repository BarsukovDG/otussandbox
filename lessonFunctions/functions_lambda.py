friends = ['Monica Geller', 'Chandler Bing', 'Joey Tribbiani','Rachel Greene', 'Phoebe Buffay', 'Ross Geller']

sorted_names = sorted(friends)
sorted_surnames = sorted(friends, key=lambda name: name.split(' ')[1])
print(friends)
print(sorted_names)
print(sorted_surnames)