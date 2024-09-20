print("Actividad 9 clase humano")
print("Ernesto Larrondo MAT:220308051281070")
# zon de class
# Zona De Clases
class Humano1070:
    # Zona de atributos
    edad=0
    genero=""
    colorO=""
    colorP=""
    estatura=0
    Sano=""
# Zona de funciones dentro de la clase
    def cantar1070(self, n):
        print(f"{n} esta cantando")
    
    def escuchar1070(self, n):
        print(f"{n} esta escuchando a tito doble P")
        
    def manejar1070(self, n):
        print(f"{n} esta manejando")
        
    def corre1070(self, n):
        print(f"{n} quiere correr")


# Zona de creación de objetos
Alex=Humano1070()
Jose=Humano1070()
# Zona usando objetos

Alex.edad=17
Alex.genero="masculino"
Alex.colorO="cafe"
Alex.colorP="negro"
Alex.estatura=1.72
Alex.Sano="Sano"

print("Resultado para Alex1070")
print(f"Edad: {Alex.edad}")
print(f"Alex es del genero: {Alex.genero}")
print(f"Los ojos de Alex con color: {Alex.colorO}")
print(f"El color de cabello de Alex es: {Alex.colorP}")
print(f"Alex mide: {Alex.estatura}")
print(f"Alex esta : {Alex.Sano}")

print("")

Jose.edad=17
Jose.genero="masculino"
Jose.colorO="cafe"
Jose.colorP="castaño claro"
Jose.estatura=1.70
Jose.Sano="Sano"

print("")

print("")
print("Resultado para Jose")
print(f"Edad: {Jose.edad}")
print(f"Jose es del genero: {Jose.genero}")
print(f"Los ojos de Jose con color: {Jose.colorO}")
print(f"El color de cabello de Jose es: {Jose.colorP}")
print(f"Jose mide: {Jose.estatura}")
print(f"Jose esta : {Jose.Sano}")

print("")

# Zona usando funciones
print("Resultado para Alex1070")
Alex.cantar1070("Alex")
Alex.escuchar1070("Alex")
Alex.manejar1070("Alex")
Alex.corre1070("Alex")

print("")
print("Resultado para Jose")
Jose.cantar1070("Jose")
Jose.escuchar1070("Jose")
Jose.manejar1070("Jose")
Jose.corre1070("Jose")