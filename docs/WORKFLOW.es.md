# Flujo diario de desarrollo

## Empezar un cambio

1. Escribe el problema y los criterios de aceptación.
2. Actualiza `main` y crea una rama breve, por ejemplo `feat/export-json`.
3. Implementa un cambio pequeño con pruebas del comportamiento relevante.
4. Ejecuta las comprobaciones del README.
5. Abre una pull request con resultados, riesgos y documentación.
6. Revisa el diff, espera a que CI termine y fusiona con squash.

## Configuración que cada proyecto debe revisar

- Rama principal protegida; impedir borrados y force pushes.
- Comprobaciones obligatorias de CI antes de fusionar.
- Dependabot, alertas y reportes privados de vulnerabilidades.
- Secretos en GitHub Secrets o un gestor dedicado.
- Permisos mínimos de GitHub Actions.
- Licencia, instrucciones de instalación y soporte.
- Entornos y aprobación de despliegue cuando exista un servicio real.

## Git local

Para evitar exponer el correo personal, usa el correo privado que aparece en los ajustes de GitHub. Después de cambiar de usuario, revisa los remotos de los clones existentes.

Este repositorio proporciona una base. La calidad de producción requiere pruebas y decisiones específicas de cada aplicación.
