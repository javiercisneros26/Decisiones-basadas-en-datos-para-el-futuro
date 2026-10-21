```python
"""
Simulación de pago de deuda
---------------------------
Proyecto de portafolio que demuestra:
- Análisis de escenarios financieros
- Simulación de Monte Carlo
- Análisis de sensibilidad

Todos los valores son sintéticos e ilustrativos.
Este modelo tiene fines educativos y no constituye
asesoramiento financiero.
"""

import random
from statistics import mean

# Supuestos del ejemplo con datos sintéticos
DEUDA_INICIAL = 5500.0
ANIOS_PROYECCION = 5
MESES_POR_ANIO = 12
NUMERO_SIMULACIONES = 1000
SEMILLA_ALEATORIA = 42

# Ahorro mensual fijo para cada escenario
ESCENARIOS = {
    "Conservador": 0,
    "Moderado": 75,
    "Objetivo": 125,
    "Agresivo": 200,
}

# Niveles de ahorro para el análisis de sensibilidad
NIVELES_AHORRO = [0, 50, 100, 150, 200, 250, 300]


def calcular_saldo_final(ahorro_mensual):
    """Calcula el saldo neto al finalizar el periodo proyectado."""
    ahorro_acumulado = (
        ahorro_mensual
        * MESES_POR_ANIO
        * ANIOS_PROYECCION
    )
    return DEUDA_INICIAL - ahorro_acumulado


def mostrar_escenarios():
    """Compara los escenarios de ahorro mensual fijo."""
    print("\n=== ANALISIS DE ESCENARIOS ===")

    for nombre, ahorro_mensual in ESCENARIOS.items():
        saldo_final = calcular_saldo_final(ahorro_mensual)

        if saldo_final > 0:
            estado = "Deuda pendiente"
        else:
            estado = "Deuda cubierta"

        print(
            f"{nombre:12} | "
            f"Ahorro mensual: {ahorro_mensual:6.2f} | "
            f"Saldo neto final: {saldo_final:8.2f} | "
            f"{estado}"
        )


def ejecutar_monte_carlo():
    """Simula distintos niveles de ahorro mensual."""
    print("\n=== SIMULACION DE MONTE CARLO ===")

    random.seed(SEMILLA_ALEATORIA)
    saldos_finales = []

    for _ in range(NUMERO_SIMULACIONES):
        ahorro_mensual = random.uniform(0, 250)
        saldo_final = calcular_saldo_final(ahorro_mensual)
        saldos_finales.append(saldo_final)

    deudas_cubiertas = sum(
        saldo <= 0 for saldo in saldos_finales
    )
    porcentaje_cubierto = (
        deudas_cubiertas / NUMERO_SIMULACIONES * 100
    )

    print(f"Numero de simulaciones: {NUMERO_SIMULACIONES}")
    print(f"Casos con deuda cubierta: {deudas_cubiertas}")
    print(
        f"Porcentaje de casos con deuda cubierta: "
        f"{porcentaje_cubierto:.1f}%"
    )
    print(
        f"Saldo neto final promedio: "
        f"{mean(saldos_finales):.2f}"
    )
    print(
        f"Saldo neto final minimo: "
        f"{min(saldos_finales):.2f}"
    )
    print(
        f"Saldo neto final maximo: "
        f"{max(saldos_finales):.2f}"
    )

    return saldos_finales


def mostrar_sensibilidad():
    """Evalúa cómo el ahorro afecta el saldo neto final."""
    print("\n=== ANALISIS DE SENSIBILIDAD ===")
    print("Ahorro mensual | Saldo neto final")

    for ahorro_mensual in NIVELES_AHORRO:
        saldo_final = calcular_saldo_final(ahorro_mensual)
        print(
            f"{ahorro_mensual:15.2f} | "
            f"{saldo_final:18.2f}"
        )


def principal():
    """Ejecuta todos los análisis del proyecto."""
    print("SIMULACION FINANCIERA CON DATOS SINTETICOS")
    print(f"Horizonte de proyeccion: {ANIOS_PROYECCION} años")
    print(f"Deuda inicial ilustrativa: {DEUDA_INICIAL:.2f}")

    mostrar_escenarios()
    ejecutar_monte_carlo()
    mostrar_sensibilidad()


if __name__ == "__main__":
    principal()
```
