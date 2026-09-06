# LecturaFácil — Módulo de Inventario

Sistema de gestión para la librería LecturaFácil (Estudio de Caso — Ingeniería de Software).

## Estructura
```
src/inventario.py          Lógica de negocio del módulo de inventario
tests/test_inventario.py   Pruebas automatizadas (pytest)
.github/workflows/ci.yml   Pipeline de integración continua
```

## Cómo correr las pruebas localmente
```bash
pip install pytest
pytest tests/ -v
```

## CI
Cada `push` o `pull request` ejecuta automáticamente las pruebas mediante GitHub Actions.
