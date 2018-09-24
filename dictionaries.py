#Exercise 1 - Print, add, delete, update
phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print('Elizabeth\'s phonne: ' + phonebook_dict['Elizabeth'])

phonebook_dict['Kareem'] = '938-489-1234'
# print(phonebook_dict)

del phonebook_dict['Alice']
# print(phonebook_dict)

phonebook_dict['Bob'] = '968-345-2345'

print(phonebook_dict)

print('')


# Exercise 2 - Nested Dictionaries
ramit = {
    'name' : 'Ramit',
    'email' : 'ramit@gmail.com',
    'interests' : ['movies', 'tennis'],
    'friends' : [
        {
            'name' : 'Jasmine',
            'email' : 'jasmine@yahoo.com',
            'interests' : ['photography', 'tennis']
        },
        {
            'name' : 'Jan',
            'email' : 'jan@hotmail.com',
            'interests' : ['movies', 'tv']
        }
    ]
}

print('Ramit\'s email: ' + ramit['email'])
print('Ramit\'s first interest: ' + ramit['interests'][0])
print('Ramit\'s friend Jasmine\'s email: ' + ramit['friends'][0]['email'])
print('Ramit\'s friend Jan\'s second interest: ' + ramit['friends'][1]['interests'][1])

print('')



