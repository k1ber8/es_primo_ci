#!/bin/bash
set -e

echo "Actualizando pip..."
python -m pip install --upgrade pip

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Entorno de liberación listo."