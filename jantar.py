#Faculdade de Juazeiro do Norte (FJN)
#Curso: Sistemas de Informação
#Disciplina: Sistemas Operacionais
#Professor: Isydório Alves Donato
#Aluno: Leonardo Freitas de Souza

# -*- coding: ISO-8859-1 -*-
import _thread
import time, random
import threading

garfo = list()
for i in range(5):
   garfo.append(threading.Semaphore(1)) #Retorna um novo objeto do semaphore

def filosofo(f):
   f = int(f)
   while True:
      # garfo da esquerda
      garfo[f].acquire() #Chama um elemento da lista e ocupa os outros
      # garfo da direita
      garfo[(f + 1) % 5].acquire()
      print ("Filosofo %i comendo..." %f)
      time.sleep(random.randint(10,15))
      garfo[f].release() #Substitui a release ocupada e ocupa as outras do semaphore liberando o bloqueio
      garfo[(f + 1) % 5].release()
      print ("Filosofo %i pensando..." %f)
      time.sleep(random.randint(10,15))

for i in range(5):
   #print ("Filosofo", i)
   _thread.start_new_thread(filosofo, tuple([i]))

while 1: pass
