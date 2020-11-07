#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    table = {}
    for i in range(length):
        # set the destination to the index
        table[tickets[i].source] = tickets[i].destination

    route = []
    current = table["NONE"]

    while current != "NONE":
        route.append(current)
        current = table[current]
    route.append(current)
    # Your code here

    return route
