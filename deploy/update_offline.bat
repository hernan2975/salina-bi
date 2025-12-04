@echo off
REM Script para actualización diaria en netbook de campo (Windows)
REM Ejecutar cada mañana después de cargar planilla de producción

echo 🌊 Salina BI — Actualización diaria
echo.

REM Verificar Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python no encontrado. Instale Python 3.9+ desde:
    echo    https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Crear carpetas si no existen
if not exist "..\data\processed" mkdir "..\data\processed"
if not exist "..\reports" mkdir "..\reports"

REM Buscar archivo de producción de hoy (nombre fijo para operarios)
set "HOY=%DATE:~6,4%%DATE:~3,2%%DATE:~0,2%"
set "ARCHIVO=..\data\raw\produccion_%HOY%.xlsx"

if not exist "%ARCHIVO%" (
    echo ⚠️  No se encontró %ARCHIVO%
    echo    Cree la planilla diaria con este nombre.
    pause
    exit /b 1
)

echo 📥 Procesando %ARCHIVO%...
python -m salinabi.cli.main update-daily --source "%ARCHIVO%"

if %errorlevel% equ 0 (
    echo ✅ Datos actualizados.
    
    echo 📊 Generando informe diario...
    python -m salinabi.cli.main report diario --output "..\reports\informe_%HOY%.pdf"
    
    if %errorlevel% equ 0 (
        echo ✅ Informe generado: ..\reports\informe_%HOY%.pdf
        echo.
        echo 🖨️  Imprima este archivo y péguelo en el tablero.
    ) else (
        echo ❌ Error al generar informe.
    )
) else (
    echo ❌ Error en la actualización.
)

pause
