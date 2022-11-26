database = {}

def saveFile():
    formatted = ''
    #print(f'database:{database}') #FOR DEBUGGING
    for i in database:
        formatted += f'{i}'
        for x in database.get(i):
            formatted += f' {x}'
        formatted += '\n'

    formatted = formatted[:-1]
    with open('database.txt', 'w') as f:
        f.write(formatted)

    listData()

def delete(delKey): #delete delKey
    if (database.get(delKey) == None):
        print("Element does not exist.")
        return
    
    try:
        database.pop(delKey)
        saveFile()
        print(f'Element {delKey} sucessfully deleted.')
    except KeyError:
        print(f'Element {delKey} does not exist.')

def create(*args):
    #check if no args
    if len(args) == 0:
        print("No element specified to create.")
        return
    #check if dupe
    if (database.get(args[0]) != None):
        print("Element already exists.")
        return
    
    database.update({args[0]:args[1:]})
    saveFile()
    print("Element sucessfully created.")

def listData():
    print(40*'='+'\nKEY       |    VALUES\n' + 40*'=')
    for i in database:
        spaces = 10 - len(i)
        print(f'{i}' + spaces*' ' + f'|   {database[i]}')
    print(40*'-')


####################################################################


def getHelp():
    print(
'''
>>>\t\tHELP MENU\t\t<<<

>> create ElementName value1 value2... valueX
[Creates a new element with all the assigned values]

>> delete ElementName
[Deletes element "ElementName" with all its values, if it exists]

>> get ElementName
[Displays all the values of the element "ElementName"]

>> list
[Lists all the elements with their assigned values]

>> quit / exit / escape
[Quits the application]

>> help
[Prints this help menu]\n\n
''')

if __name__ == '__main__':
    #intro
    print(
'''
<--:.:.:. *WELCOME TO THE DATABASE INTERFACE* .:.:.:-->>\n
You can use this program to store procedural data in a text file.
Use the command 'help' to get a list of all usable commands.\n\n
''')
    
    #Load existing database
    with open('database.txt', 'r') as f:
        data = f.read().strip()
        dics = data.split('\n')
        for i in dics:
            if (i not in [[''],'']):
                x = i.split(' ')
                database.update({x[0]:x[1:]})
    
    while True:
        inp = input().lower().strip().split(' ')
        if inp != ['']:
            cmd = inp[0]
            if (cmd in ['exit','quit','escape']):
                exit()
            elif (cmd == 'create'):
                try:
                    create(*inp[1:]) #Search diff between [1:] & [1::]
                except IndexError:
                    create('Please enter a name for the element')
            elif (cmd == 'delete'):
                try:
                    delete(inp[1])
                except IndexError:
                    print('Please enter the name of the element to delete.')
            elif (cmd == 'get'):
                try:
                    print(f'[ {inp[1]} ]:  {database[inp[1]]}')
                except KeyError:
                    print(f'Element {inp[1]} does not exist.')
                except IndexError:
                    print(f'Please enter a name for the element to get.')
            elif (cmd == 'list'):
                listData()
            elif (cmd == 'help'):
                getHelp()
            else:
                print(f'Undefined Command {cmd}')
        else:
            getHelp()
