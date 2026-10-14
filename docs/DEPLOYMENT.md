# Despliegue de SuperAhorro

## Ejecutar con Docker Compose

Requisitos: Docker Engine y Docker Compose.

1. Clona el repositorio.
2. En la carpeta del proyecto, ejecuta `docker compose up --build -d`.
3. Web: http://localhost:3000
4. API: http://localhost:8000
5. Documentación interactiva de la API: http://localhost:8000/docs
6. Estado de la API: http://localhost:8000/health

Para detener: `docker compose down`. Para conservar la base de datos, no borres el volumen `superahorro_data`.

## Importante sobre los datos

Los productos y precios que incluye el prototipo son ficticios y sirven únicamente para demostrar la interfaz y la comparación de cestas. No deben publicarse como precios reales ni utilizarse para tomar decisiones de compra. Antes de ofrecer precios reales, hay que incorporar fuentes autorizadas, registrar cuándo se actualizó cada precio y especificar tienda/zona y formato del producto.

## Seguridad antes de producción

- Cambiar las credenciales de PostgreSQL.
- Configurar CORS con los dominios concretos de la web.
- Añadir autenticación y límites de peticiones si se habilitan cuentas.
- Configurar HTTPS, copias de seguridad y monitorización.
- No almacenar secretos en GitHub.
- Revisar licencias y condiciones de uso de cualquier fuente de datos.

## Estado actual del MVP

La web incluye búsqueda local, filtros, cesta y cálculo comparativo con datos de muestra. La API ofrece endpoints de salud, tiendas, productos y comparación. PostgreSQL queda definido en Compose para la siguiente iteración; en esta versión los productos de muestra de la API viven en memoria y no se persisten en la base de datos.