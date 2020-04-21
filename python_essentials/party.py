'''
Problem:

Create a class Party that only has an attribute called people.
The __init__ method should not accept any parameters.
You will be given names of people (on separate lines) until you receive the command "End".
Use the created class to solve this problem.
After you receive the end command print 2 lines:
Going: {people} - the people should be separated by comma and space
Total: {total_people_going}

Solution:

'''


class Party():

    def __init__(self):
        self.people = []


a = Party()
command = input('name: ').lower()
while not command == 'end':
    a.people.append(command)
    command = input('name: ').lower()

b = ', '.join(a.people)
print('Going: {}'.format(b))
print('Total: {}'.format(len(a.people)))
