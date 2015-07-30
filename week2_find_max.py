def max(list, current):
    if(len(list)>2):
        current = list[0]
        return current
    if(current < list[0]):
    	current = list[0]
    max(list[1:], current)