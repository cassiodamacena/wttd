print('Begin', __name__)
# __name__ retorna o nome do módulo em questão (no caso o nome do módulo 'proga'), porém, quando é o mesmo arquivo retorna o próprio __name__

print('Define fA')
def fA():
    print('Dentro fA')

print('Chama fA')
fA()

print('End', __name__)