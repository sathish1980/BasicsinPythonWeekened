

def ticketbooking(person):
    i=5
    while (person <= i):
        if(i>0):
            if person==3:
                i = i - 1
                person = person - 1
                #break
                continue
            print("Ticket booked for person: "+str(person))
            i=i-1
            person=person-1
        if(person<=0):
            break

ticketbooking(4)