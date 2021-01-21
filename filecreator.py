# Data managment functions
configFile = 'configFileCreator.txt'

def write(var):
    file = open(configFile, 'w')
    file.write(str(var))
    file.close()

def read():
    file = open(configFile, 'r')
    var = eval(file.read())
    write(var)
    file.close()
    return var



# Import configuration data
path = read()[0]
name = read()[1]
extension = read()[2]



# File parameters correcting functions
# Config rereader function
def resetParameters():
    global path
    global name
    global extension

    path = read()[0]
    name = read()[1]
    extension = read()[2]

# Current parameters correcting functions
def setPath():
    global path
    path = input()

def setName():
    global name
    name = input()

def setExtension():
    global extension
    extension = input()

# Base parameters correcting functions
def setConfigPath():
    var = read()
    var[0] = input()
    write(var)

def setConfigName():
    var = read()
    var[1] = input()
    write(var)

def setConfigExtension():
    var = read()
    var[0] = input()
    write(var)

# File creating function
def createFile():
    open(path + r'\\' + name + '.' + extension, 'x').close()

# Short functions names
r = resetParameters
c = createFile

p = setPath
n = setName
e = setExtension

cp = setConfigPath
cn = setConfigName
ce = setConfigExtension



# Text interface
command = input()
while command != '':
    exec(command)
    command = input()



# File creating
    createFile()
