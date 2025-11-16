# PythonProyecto2 - Gestión de Beneficiarios SR

Este proyecto es una **aplicación web creada con Django** para gestionar beneficiarios que trabajan para la empresa ficticia **SR**. Los beneficiarios pueden ser **abogados** o **peritos**.  

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
-Búsqueda de abogados: se puede buscar por nombre, apellido o número de abogado.

Autenticación de Usuarios (Login / Logout / Registro)
El proyecto incorpora un sistema completo de autenticación mediante Django, que permite gestionar el acceso de los usuarios a las funcionalidades internas.

La app incluye:
✔️ Registro de usuarios: Los nuevos usuarios pueden crear su cuenta desde la opción "Registrarse". Durante el registro pueden completar:

Nombre de usuario
Nombre y apellido
Email
Contraseña
Foto de perfil (opcional)
Tras registrarse, el usuario queda autenticado automáticamente y es redirigido a su perfil.

✔️ Login: El acceso al sistema se realiza desde /login/.
Una vez autenticado, el usuario puede navegar por las secciones internas del sistema, como Beneficiarios y Pagos.

✔️ Logout: El cierre de sesión puede hacerse desde el menú superior o la opción "Cerrar sesión". Luego del logout, el usuario es redirigido a la página principal.

✔️ Perfil de usuario: Los usuarios cuentan con una sección "Mi perfil" donde pueden ver su información personal y editar:
Nombre de usuario
Email
Nombre y apellido
Fecha de nacimiento
Dirección
Foto de perfil

App "Pagos": Esta aplicación permite gestionar solicitudes de pago realizadas por los usuarios del sistema. Cada pedido queda asociado al usuario que lo creó y puede ser administrado desde la interfaz web.

La app permite:
✔️ Crear un nuevo pedido de pago
Desde la opción "Nuevo pago", el usuario puede cargar:
Número de siniestro
Número de factura
Fecha de la factura
Importe

✔️ Listar pagos existentes
En la vista principal de Pagos, el usuario puede ver todos los pagos registrados, incluyendo:
Siniestro
Factura
Fecha de solicitud
Importe

✔️ Editar un pago
Cada pago puede modificarse desde el botón "Editar".
Solo el creador del pago tiene permisos para editarlo.

✔️ Eliminar un pago
Los pagos también pueden borrarse desde el botón "Eliminar", siempre respetando los permisos del usuario.
