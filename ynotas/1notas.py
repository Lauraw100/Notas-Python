nomAlto=""
nomBajo=""
finalAlta=0
finalBaja=100

for i in range (1,3,1):
    nombre = input(f'Ingrese el nombre del candidado #{i}\n')
    examenPractico = float(input(f'Ingrese el valor del examen practico de {nombre}\n'))
    examenTeorico = float(input(f'Ingrese el valor del examen teorico de {nombre}\n'))
    notaFinal = ((examenTeorico*0.15)+(examenPractico*0.85))

    if (notaFinal>finalAlta):
        finalAlta=notaFinal
        nomAlto=nombre

    if (notaFinal<finalBaja):
        finalBaja=notaFinal
        nomBajo=nombre


print(nomAlto, ' ', finalAlta, '\n', nomBajo, ' ', finalBaja)
