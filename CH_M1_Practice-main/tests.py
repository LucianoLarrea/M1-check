import unittest
import os
import checkpointM1 as ch
import Lista as lis

class DataScience_Modulo1_Checkpoint(unittest.TestCase):
    
    def test_Pregunta01(self):
      valor_test = ch.Ret_Pregunta01()
      valor_esperado = 5190
      self.assertEqual(valor_test, valor_esperado)

    def test_Pregunta02(self):
      valor_test = ch.Ret_Pregunta02()
      valor_esperado = 10
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Pregunta03(self):
      valor_test = ch.Ret_Pregunta03()
      valor_esperado = 5109
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Pregunta04(self):
      valor_test = ch.Ret_Pregunta04()
      valor_esperado = 147237.11
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Pregunta05(self):
      valor_test = ch.Ret_Pregunta05()
      valor_esperado = 2019
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Pregunta06(self):
      import numpy as np
      n1 = np.array([[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5]])
      n2 = np.array([[6,7],[8,6],[7,8]])
      valor_test = ch.Ret_Pregunta06(n1,n2)
      valor_esperado = True
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Pregunta07(self):
      valor_test = ch.Ret_Pregunta07()
      valor_esperado = 'Mexico'
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Pregunta08(self):
      valor_test = ch.Ret_Pregunta08()
      valor_esperado = 99
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Pregunta09(self):
      valor_test = ch.Ret_Pregunta09()
      valor_esperado = 21.15
      self.assertEqual(valor_test, valor_esperado)
      
    def test_Pregunta10(self):
      lista = lis.Lista()
      for i in range(1, 6):
        lista.agregarElemento(i)
      valor_test = ch.Ret_Pregunta10(lista)
      valor_esperado = 5
      self.assertEqual(valor_test, valor_esperado)

resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write(str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))