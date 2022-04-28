
Aaron Saban
### Consigna

1) Listar los títulos de las materias del departamento "Computer Science" 
2) Todas las materias que dicta el profesor de Apellido Roberts 
3) Todas las materias que tienen como correlativas a alguna de las materias que dicta el profesor de Apellido Roberts

### Soluciones con los selectores XPATH

1: ```//Departamento[@Codigo="CS"]/Materia/Titulo/text()```
2: ```//Materia[.//Profesor/Apellido[contains(text(),'Roberts')]]```
3: ```//Correlativas[Corre="CS106A"]/..|//Correlativas[Corre="CS106B"]/..```