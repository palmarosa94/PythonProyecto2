# PythonProyecto2 - Gestión de Beneficiarios SR

Este proyecto es una **aplicación web creada con Django** para gestionar beneficiarios que trabajan para la empresa ficticia **SR**. Los beneficiarios pueden ser **abogados** o **peritos**, y cada uno debe estar asociado a una **jurisdicción** (localidad donde desempeña su trabajo).  

La app permite:  
- Registrar nuevos beneficiarios (abogados y peritos).  
- Registrar nuevas jurisdicciones.  
- Buscar abogados en la base de datos.  
- Listar beneficiarios y consultar sus datos.

 Configuraciónn del proyecto:
 1) Crear entorno virtual: python -m venv entorno
 2) Activar el entorno virtual: entorno\Scripts\activate
 3) Instalar Django: pip install django
 4) Configurar el intérprete de Python: En VS Code u otro editor, seleccionar el intérprete del entorno virtual creado (entorno) para que se usen las librerías correctas.

Migraciones y base de datos:
Dentro del directorio del proyecto, ejecutar:
    python manage.py makemigrations
    python manage.py migrate
*Esto creará la base de datos y las tablas correspondientes a los modelos: Abogados, Peritos y Jurisdicciones.

Ejecutar el servidor:
    python manage.py runserver
    Abrir el navegador en: http://127.0.0.1:8000/

Funcionalidades:
-Página principal: Acceso rápido a las distintas secciones: Abogados, Peritos, Jurisdicciones.
-Registro de beneficiarios:
    Abogados: ir a "Abogados → Nuevo", completar el formulario y guardar.
    Peritos: ir a "Peritos → Nuevo", completar el formulario y guardar.
-Registro de jurisdicciones:
    Ir a "Jurisdicciones → Nuevo", completar el formulario y guardar.
-Búsqueda de abogados: En la página http://127.0.0.1:8000/abogados/ se puede buscar por nombre, apellido o número de abogado.