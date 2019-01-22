from random import randint, randrange
from pprint import pprint
from decimal import Decimal

class event:
    def __init__(self,x,y,i):
        self.x = x
        self.y = y
        self.ID = i
        self.tickets = [randint(1,100000)/100 for x in range(randint(0, 20))]
        self.tickets.sort()

def generate_world():
    world = [[None for x in range(20)] for y in range(20)]

    events = set()

    i = 1
    while(len(events)<randint(0,400)):

        x = randint(0,19)
        y = randint(0,19)

        if (x,y) not in events:
            rand_event = event(x,y,i)
            events.add(rand_event)
            world[rand_event.x][rand_event.y] = rand_event
            i+=1

    return world

def check(world, x, y, eventsF, seen, priQ):
    if (x, y) not in seen and x<20 and y<20 and x>=0 and y>=0:
        seen.add((x,y))
        priQ.append((x,y))
        if world[x][y] != None:
            eventsF.append(world[x][y])


def search(world, priQ, eventsF, seen, last_coord, origin):
    x,y = priQ.pop(0)

    check(world, (x+1), y, eventsF, seen, priQ)
    check(world, x, (y+1), eventsF, seen, priQ)
    check(world, (x-1), y, eventsF, seen, priQ)
    check(world, x, (y-1), eventsF, seen, priQ)


    if ((origin[0]-x)+(origin[1]-y)) != ((origin[0]-last_coord[0])+(origin[1]-last_coord[1])):
        return False

    last_coord = x,y

    return True


def get_top_5(world,x,y):
    eventsFound = []
    priQueue    = []
    seen        = set()
    origin      = (x,y)
    last_coord  = (0,0)
    delta_dist  = True

    priQueue.append((x,y))

    while(len(priQueue) > 0 and (delta_dist or len(eventsFound) < 5)):
        delta_dist = search(world, priQueue, eventsFound, seen, last_coord, origin)
        
    return eventsFound







if __name__ == "__main__":

    world = generate_world()

    # x = int(input('x: '))
    # y = int(input('y: '))

    x=0
    y=0

    eventsFound = get_top_5(world,x+10,y+10)

    eventsFound.sort(key=lambda x: x.tickets[0])

    for x in eventsFound[:5]:
        print(str(x.ID)+": "+str(x.tickets[0]))