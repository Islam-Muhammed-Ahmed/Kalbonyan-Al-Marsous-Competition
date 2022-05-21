flips = [
    'heads',
    'tails',
    'tails',
    'heads',
    'tails',
]
# this will get the count of element "head"
print(flips.count('heads'))
# this will print only the last element in the list
print(flips.pop())

# the code with the instructor

class Tickets:
    'class for Tickets'

    def __init__(self, name, tickets):
        self.name = name
        self.tickets = tickets

    def displayTicketsOwner(self):
        print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

    def addTicket(self):
        self.tickets += 1
        print('{} tickets increased to {}'.format(self.name, self.tickets))

attendee1 = Tickets('Islam M Ahmed', 2)
attendee2 = Tickets('Mostafa M Ahmed', 1)
attendee1.displayTicketsOwner()
attendee2.displayTicketsOwner()
attendee2.addTicket()
attendee2.addTicket()
