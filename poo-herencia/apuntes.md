Trabajador     -> Es una clase Abstracta 
  - diseñar -> es método asbtracto
  - vender  -> es método asbtracto
  - dormir  -> es método asbtracto
  - comer    -> es método asbtracto
  - programar  -> es método asbtracto
  - cobrar     -> es método asbtracto


Una clase abstracta bastaria con que un solo método de la clase sea abstracto para que la clase sea abstracta.


Que eran los métodos abstractos??
 Un metodo abstracto es un método sin implementación 

 ```python
class Trabajador():
    def trabajar():
      pass

    def diseñar():
      pass

    def vender():
      pass

    def dormir():
      pass

    def comer():
      pass

    def programar():
      pass

    def cobrar():
      pass


```

```python
class IngenieroInformatico(Trabajador):
    def trabajar():
      print("ING.Informatica trabajando en planificacion de software")

    def comer():
      print("Comiendo")

    def dormir():
      print("Dormir")

    def programar():
      print("Programando....")

    def diseñar():
      pass

    def cobrar():
      pass

    def vender():
      pass


```