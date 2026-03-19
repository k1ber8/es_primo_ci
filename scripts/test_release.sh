#!/bin/bash
set -e

echo "Ejecutando pruebas..."
export PYTHONPATH=.
pytest -v

echo "Pruebas completadas correctamente."