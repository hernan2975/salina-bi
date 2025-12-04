# Política de Seguridad — Salina BI

## 📌 Alcance
Esta política cubre el proyecto `salina-bi` en su configuración típica de **entorno offline** (sin conexión a internet), como se implementa en salinas de La Pampa.

## 🔒 Principios de seguridad

1. **Autonomía técnica**:  
   - Todos los datos permanecen en la red local de la salina  
   - Ningún dato sale del establecimiento sin autorización explícita por asamblea

2. **Minimización de superficie de ataque**:  
   - Sin APIs expuestas a internet  
   - Sin servicios en la nube  
   - Sin dependencias con servidores externos

3. **Protección de datos sensibles**:  
   - Datos productivos y económicos son propiedad exclusiva de la salina  
   - No se almacenan credenciales, contraseñas ni datos personales de operarios

## 🛡️ Medidas implementadas

| Capa | Medida | Estado |
|------|--------|--------|
| **Aplicación** | Validación estricta de esquemas (Pydantic) | ✅ Implementado |
| **Datos** | Sin almacenamiento de información personal identificable (PII) | ✅ Por diseño |
| **Infraestructura** | Ejecución en red aislada (sin salida a internet) | ✅ Configuración recomendada |
| **Hardware** | Soporte para cifrado de disco (LUKS/BitLocker) en netbooks | ✅ Documentado en `docs/security_guide.md` |

## 🚨 Reporte de vulnerabilidades

Debido al carácter **offline y autónomo** del sistema:

- **No hay programa de recompensas** (no hay superficie de ataque pública)  
- **Reportes internos**:  
  Si identifica una vulnerabilidad durante el uso:  
  1. Documente el escenario en `issues` de este repositorio  
  2. Etiquete como `security`  
  3. **No incluya datos sensibles reales** (use ejemplos anonimizados)  

Los reportes se revisan mensualmente por el equipo de la Comunidad Salinera Pampeana.

## ⚠️ Limitaciones conocidas

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Acceso físico no autorizado a netbook | Media | Alto | Cifrado de disco + bloqueo automático |
| Inyección de datos maliciosos vía USB | Baja | Medio | Validación estricta en `ingestion.py` |
| Modificación no autorizada de scripts | Baja | Alto | Control de versiones con Git local |

## 📜 Cumplimiento normativo

- **Ley 25.326 (Protección de Datos Personales)**:  
  El sistema no procesa datos personales según definición legal (solo datos productivos agregados).  
- **Res. SENASA 433/2023**:  
  Los datos de trazabilidad se almacenan exclusivamente para cumplimiento, sin fines comerciales.  
- **Normas ISO 27001**:  
  Se aplican controles selectos del Anexo A (A.7, A.8, A.12) adaptados a PYMEs industriales.

## 📚 Recursos adicionales

- [`docs/security_guide.md`](docs/security_guide.md): Guía práctica para administradores  
- [`deploy/backup_to_usb.sh`](deploy/backup_to_usb.sh): Respaldo seguro a USB cifrado  
- [`config/settings.example.yaml`](config/settings.example.yaml): Configuración de seguridad por defecto

---

> ℹ️ **Nota**: Este sistema está diseñado para entornos industriales con recursos limitados. La seguridad se basa en **aislamiento físico** y **buenas prácticas operativas**, no en soluciones complejas de ciberseguridad.
