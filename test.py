from classifier import *

setup()

string1 = "Volvió a casarse en 1118 con Agnés de Garlande, hija de Anseau de Garlande, señor de Rochefort-en-Yvelines, y de Beatrice de Rochefort. De esta unión nacieron"
string2 = "Our teacher warned him not to be late again"

print (classifier(string1))
print (classifier(string2))