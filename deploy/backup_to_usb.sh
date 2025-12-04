#!/bin/bash
# Script para respaldo automático a USB (Linux/Raspberry Pi)
# Ejecutar al insertar USB con etiqueta "SALINA_BACKUP"

USB_LABEL="SALINA_BACKUP"
MOUNT_POINT="/media/salina"
BACKUP_DIR="$MOUNT_POINT/salina_backup_$(date +%Y%m%d)"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

# Verificar si hay USB con la etiqueta correcta
USB_DEVICE=$(lsblk -f | grep "$USB_LABEL" | head -1 | awk '{print "/dev/" $1}')

if [ -z "$USB_DEVICE" ]; then
    log "❌ No se encontró USB con etiqueta '$USB_LABEL'"
    exit 1
fi

log "✅ USB detectado: $USB_DEVICE"

# Montar USB (requiere permisos o ejecutar como root)
sudo mkdir -p "$MOUNT_POINT"
sudo mount "$USB_DEVICE" "$MOUNT_POINT" 2>/dev/null

if [ $? -ne 0 ]; then
    log "❌ Error al montar USB"
    exit 1
fi

# Crear carpeta de respaldo
mkdir -p "$BACKUP_DIR"

# Respaldo de datos procesados
if [ -f "../data/processed/produccion.parquet" ]; then
    cp "../data/processed/produccion.parquet" "$BACKUP_DIR/"
    log "✅ Respaldo: produccion.parquet"
fi

# Respaldo de informes
if [ -d "../reports" ]; then
    cp -r "../reports" "$BACKUP_DIR/"
    log "✅ Respaldo: reports/"
fi

# Respaldo de configuración
if [ -f "../config/settings.yaml" ]; then
    cp "../config/settings.yaml" "$BACKUP_DIR/salina_config.yaml"
    log "✅ Respaldo: configuración"
fi

# Generar índice de respaldo
cat > "$BACKUP_DIR/indice.txt" <<EOF
Respaldo automático - Salina BI
Fecha: $(date)
Contenido:
- produccion.parquet: Datos procesados
- reports/: Informes PDF
- salina_config.yaml: Configuración actual
EOF

log "✅ Respaldo completado en $BACKUP_DIR"

# Desmontar
sudo umount "$MOUNT_POINT"
log "💾 USB desmontado. Puede retirarlo."

# Notificación visual (para Raspberry Pi con pantalla)
if command -v zenity >/dev/null; then
    zenity --info --text="✅ Respaldo completado.\nPuede retirar el USB." --title="Salina BI" --width=300
fi
