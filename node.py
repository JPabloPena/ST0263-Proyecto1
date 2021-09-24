#https://tutorialpython.com/listas-en-python/
def node(value):
    hash = {}
    node1 = []
    node2 = []
    node3 = []
    key = 0
    v = value
    
    hash[key] = value
    node1.append(hash)
    key = key + 1

    hash[key] = 'minecraft'
    node1.append(hash)

    for n in node1:
        print(n)

    #key = key + 1

node('file_test.txt')