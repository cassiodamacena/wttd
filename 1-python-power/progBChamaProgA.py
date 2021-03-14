print('Begin', __name__)
import progA # Importando progA e já executa o seu código

print('Define fB')
def fA():
    print('Dentro fB')
    progA.fA() # Chamando agora somente a função fA de progA

print('Chama fB')
fA()

print('End', __name__)