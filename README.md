<div align="center">
  <img src="https://github.com/user-attachments/assets/df02cfe1-dd25-41d8-9cc3-2cea31e60d1a" alt="Logo del Proyecto" width="400"/>

# 🤖 Portal de Noticias sobre Robótica
## Etapa 2: Desarrollo Web - Grupo N°4

[![Django](https://img.shields.io/badge/Django-5.2.4-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://html.spec.whatwg.org/)

</div>

## 📋 Descripción del Proyecto

Este proyecto es un **portal web de noticias especializado en robótica** desarrollado como proyecto final del curso de Desarrollo Web - Etapa 2. La aplicación permite gestionar noticias, eventos y categorías relacionadas con el mundo de la robótica, ofreciendo tanto funcionalidades de visualización como de administración de contenido.

### 🎯 Objetivos del Proyecto

- Crear un sistema web completo para la gestión de noticias sobre robótica
- Implementar un CRUD (Create, Read, Update, Delete) funcional usando Django
- Aplicar conceptos de programación orientada a objetos y bases de datos relacionales
- Desarrollar tanto vistas basadas en funciones (FBV) como vistas basadas en clases (CBV)
- Crear un sistema de categorización y filtrado de contenido

## ✨ Características Principales

### 📰 Gestión de Noticias
- **Visualización** de todas las noticias del portal
- **Filtrado** por categorías (Tecnología, Política, Deportes, etc.)
- **Detalle completo** de cada noticia con autor y fecha
- **CRUD completo**: Crear, editar y eliminar noticias
- **Sistema de categorías** múltiples por noticia

### 🎪 Gestión de Eventos
- **Listado** de eventos relacionados con robótica
- **Filtrado** por categorías de eventos
- **Detalles** con organizador, fecha/hora y duración
- **Carga de imágenes** para eventos
- **CRUD completo** para gestión de eventos

### 👥 Sistema de Autores y Organizadores
- **Gestión de autores** con nacionalidad
- **Organizadores** con tipos (Individual, Empresa, Institución)
- **Relaciones** entre contenido y responsables

## 🏗️ Arquitectura del Proyecto

### 📁 Estructura de Directorios
```
Proyecto-Final-Grupo-N-4/
├── apps/
│   ├── noticias/          # App para gestión de noticias
│   │   ├── models.py      # Modelos: Noticia, Autor, Categoria
│   │   ├── views.py       # Vistas FBV y CBV
│   │   ├── urls.py        # URLs de la app
│   │   └── admin.py       # Configuración del admin
│   └── eventos/           # App para gestión de eventos
│       ├── models.py      # Modelos: Evento, Organizador, Categoria
│       ├── views.py       # Vistas FBV y CBV
│       ├── forms.py       # Formularios personalizados
│       └── urls.py        # URLs de la app
├── comsiete/              # Configuración principal del proyecto
│   ├── settings/          # Configuraciones separadas
│   │   ├── base.py        # Configuración base
│   │   ├── local.py       # Desarrollo local
│   │   └── production.py  # Producción
│   ├── urls.py            # URLs principales
│   └── views.py           # Vista principal
├── templates/             # Templates HTML
│   ├── noticias/          # Templates de noticias
│   └── eventos/           # Templates de eventos
├── static/                # Archivos estáticos
├── requirements.txt       # Dependencias del proyecto
└── manage.py             # Comando de gestión de Django
```

### 🗄️ Modelos de Base de Datos

#### Noticias
- **Noticia**: Título, subtítulo, contenido, fecha, autor, categorías
- **Autor**: Nombre, nacionalidad
- **Categoria**: Nombre, descripción

#### Eventos
- **Evento**: Nombre, descripción, fecha/hora, duración, organizador, categorías, imagen
- **Organizador**: Nombre, tipo (Individual/Empresa/Institución)
- **Categoria**: Nombre, descripción

### 🔗 Relaciones de Base de Datos
- **Uno a Muchos**: Autor → Noticias, Organizador → Eventos
- **Muchos a Muchos**: Noticias ↔ Categorías, Eventos ↔ Categorías

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso a paso

1. **Clonar el repositorio**
```bash
git clone https://github.com/JDGA1997/Proyecto-Final-Grupo-N-4.git
cd Proyecto-Final-Grupo-N-4
```

2. **Crear entorno virtual**
```bash
python -m venv venv
venv\Scripts\activate  # En Windows
# source venv/bin/activate  # En Linux/Mac
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**
- Portal principal: http://127.0.0.1:8000/
- Noticias: http://127.0.0.1:8000/noticias/
- Eventos: http://127.0.0.1:8000/eventos/
- Admin: http://127.0.0.1:8000/admin/

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| **Django** | 5.2.4 | Framework web principal |
| **Python** | 3.x | Lenguaje de programación |
| **SQLite** | - | Base de datos |
| **HTML5** | - | Estructura de páginas |
| **CSS3** | - | Estilos (básicos) |

## 📱 Funcionalidades por Módulo

### 📰 Módulo Noticias

#### Vistas Disponibles
- **Lista de noticias** (`/noticias/cbv/` y `/noticias/fbv/`)
- **Detalle de noticia** (`/noticias/cbv/<id>/`)
- **Crear noticia** (`/noticias/cbv/crear/`)
- **Editar noticia** (`/noticias/cbv/actualizar/<id>/`)
- **Eliminar noticia** (`/noticias/cbv/eliminar/<id>/`)

#### Filtros
- Por categoría mediante parámetros GET
- Búsqueda en títulos y contenido

### 🎪 Módulo Eventos

#### Vistas Disponibles
- **Lista de eventos** (`/eventos/`)
- **Detalle de evento** (`/eventos/<id>/`)
- **Crear evento** (`/eventos/crear/`)
- **Editar evento** (`/eventos/editar/<id>/`)
- **Eliminar evento** (`/eventos/eliminar/<id>/`)

#### Características Especiales
- Carga de imágenes para eventos
- Cálculo automático de fecha/hora de finalización
- Formularios personalizados con widgets de fecha/hora

## 🔧 Configuración de Desarrollo

### Configuraciones Separadas
El proyecto utiliza configuraciones separadas para diferentes entornos:

- **`base.py`**: Configuración común
- **`local.py`**: Desarrollo local (DEBUG=True, SQLite)
- **`production.py`**: Producción (DEBUG=False)

### Variables de Entorno
Por defecto, el proyecto usa `comsiete.settings.local` para desarrollo.

## 🧪 Testing

El proyecto incluye estructura básica para testing en cada app:
```bash
python manage.py test apps.noticias
python manage.py test apps.eventos
```

## 👩‍💻👨‍💻 Nuestro Equipo

Este proyecto fue posible gracias al trabajo colaborativo de nuestro equipo:

| Nombre y Apellido | Usuario en GitHub | Perfil de GitHub |
| ----------------- | ----------------- | ---------------- |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
|  | `` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/) |
| Aldo Andrés Acosta | `Andres777777` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Andres777777) |
| Juan Diego González Antoniazzi | `JDGA1997` | [![GitHub Badge](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JDGA1997) |

## 🤝 Contribuciones

Este proyecto es parte del curso de Programación - Etapa 2 del **Informatorio**. Las contribuciones están limitadas a los miembros del equipo durante el período académico.

## 📄 Licencia

Este proyecto es desarrollado con fines educativos como parte del programa Informatorio.

## 🏆 Logros Académicos

- ✅ Implementación completa de CRUD
- ✅ Uso de Django ORM y relaciones de base de datos
- ✅ Desarrollo con vistas basadas en funciones y clases
- ✅ Sistema de filtrado y búsqueda
- ✅ Gestión de archivos multimedia
- ✅ Arquitectura modular con apps separadas

---

<div align="center">

### ⭐ Si este proyecto te fue útil, ¡no olvides darle una estrella!

**Desarrollado con 🤖❤️ por el Grupo N°4 - Informatorio 2025**

[![Informatorio](https://img.shields.io/badge/Informatorio-2025-blue?style=for-the-badge)](https://www.informatorio.org/)

</div>
