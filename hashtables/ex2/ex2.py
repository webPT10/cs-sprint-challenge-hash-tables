#  Hint:  You may not need all of these.  Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    
    veritas = {}

    for ticket in tickets:
        source = ticket.source
        dest = ticket.destination

        veritas[source] = dest

    current = veritas["NONE"]
    route = []

    while current is not "NONE":
        route.append(current)
        current = veritas[current]
        
    route.append(current)

    return route
