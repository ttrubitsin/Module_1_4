calls = 0

def count_calls():
    global calls
    calls +=1

def string_info(string):
    global calls
    count_calls()

    t = (len(string),
         string.upper(),
         string.lower())
    return t

def is_contains(string, list_to_search):
    global calls
    count_calls()

    list_to_search = [item.lower() for item in list_to_search]

    if string.lower() in list_to_search:
        return True
    else:
        return False

print(string_info('Barakuda'))
print(string_info('Brandenburg'))
print(is_contains('incomplite',['comlation','complicton','IncOmPlite']))
print(is_contains('Assembler',['assemb','bler','sembler']))
print(string_info('Assembler'))
print(calls)