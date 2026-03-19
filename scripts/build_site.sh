#!/bin/bash
set -e

echo "Generando carpeta de despliegue..."
rm -rf dist
mkdir -p dist

cp index.html dist/
cp -r src dist/src 2>/dev/null || true

echo "Artefacto de despliegue generado en ./dist"