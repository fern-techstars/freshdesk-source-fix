from freshdesk.api import API
from time import sleep
from os import environ

a = API(environ['FRESHDESK_URL'], environ['FRESHDESK_KEY'])

# supply updated_since or else it only grabs ticket created in past 30 days
# supply 
tickets = a.tickets.list_tickets(filter_name=None, updated_since='2014-01-01T00:00:00.000Z')

for i, ticket in enumerate(tickets):
    print(f'checking ticket {ticket.id} with current source of {ticket.source}')
    if ticket.source == 'phone':
        try:
            a.tickets.update_ticket(ticket.id, source=1)
            print('updated source')
        except Exception as e:
            print(e)

    if (i+1)%5==0:
        print('taking a breather')
        sleep(5)