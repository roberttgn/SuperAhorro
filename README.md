# SuperAhorro 🇪🇸

Prototipo de un comparador de precios de supermercados en España, pensado primero para móvil.

> **Aviso:** los productos y precios incluidos son ficticios y sirven únicamente para probar el funcionamiento. No son precios reales ni ofertas de ningún supermercado.

## Qué incluye

- Interfaz web responsive con Next.js y TypeScript.
- Búsqueda de productos y filtros por categoría.
- Precios de demostración comparados entre Mercadona, Carrefour y Lidl.
- Cesta con cantidades y suma estimada por supermercado.
- API REST con FastAPI: estado, tiendas, productos y comparación de cesta.
- PostgreSQL configurado en Docker Compose para la siguiente iteración.
- Pruebas básicas para la API.

## Arranque local

Necesitas Docker Engine y Docker Compose. En la carpeta del proyecto:

```bash
docker compose up --build -d
```

- Web: http://localhost:3000
- API: http://localhost:8000
- Documentación interactiva: http://localhost:8000/docs
- Estado: http://localhost:8000/health

Para detener los contenedores: `docker compose down`.

## Estructura

- `src/app`: interfaz Next.js.
- `api/main.py`: endpoints de FastAPI y catálogo de muestra.
- `api/test_main.py`: pruebas de la API.
- `docker-compose.yml`: web, API y PostgreSQL.
- `docs/DEPLOYMENT.md`: guía de despliegue y lista de comprobaciones.

## Próximos pasos

1. Probar el arranque y ejecutar las pruebas en un entorno con Docker/Python.
2. Conectar catálogo y precios a PostgreSQL.
3. Incorporar fuentes autorizadas de precios reales, fecha de actualización, tienda/zona y formato exacto del producto.
4. Preparar despliegue público con HTTPS, secretos seguros y CORS limitado al dominio de producción.

No se presentan datos inventados como precios reales. Antes de publicar precios reales hay que comprobar las condiciones de uso y autorización de las fuentes de datos.
