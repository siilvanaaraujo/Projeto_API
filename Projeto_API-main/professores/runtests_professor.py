import requests
import unittest

'''

'''

class TestStringMethods(unittest.TextCase):

    def test_000_professor_retorna_lista(self):
        #Utiliza o método GET para buscar o endpoint
        r = requests.get('http://127.0.0.1:8000/professores')

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)


if __name__ == '__main__':
    runTests()  