import time
import numpy as np
import pandas as pd

# Project #1: Smart Kidney-Loop Water Quality & Nozzle Clogging Analytics Engine
# Designed for Steel CCM Spray Cages & Universal Industrial Utilities


def generate_sensor_data():
    """Simulates Real-Time IIoT Sensors in a Bypass/Kidney Loop Line"""
    # Baseline normal values with random industrial noise
    dp_bar = np.random.normal(0.4, 0.02)  # Differential Pressure across filter (Bar)
    turbidity_ntu = np.random.normal(15, 2.0)  # Water Turbidity (NTU)
    flow_lpm = np.random.normal(120, 3.0)  # Water Flow Rate (LPM)

    # Randomly introduce a Contamination / Filter Clogging Event
    event_chance = np.random.rand()
    if event_chance > 0.85:  # Filter Clogging/Dirty Water
        dp_bar += np.random.uniform(0.8, 1.5)
        turbidity_ntu += np.random.uniform(50, 120)
        flow_lpm -= np.random.uniform(20, 40)
    elif event_chance < 0.05:  # Filter Mesh Rupture/Damage
        dp_bar = np.random.uniform(0.01, 0.05)
        turbidity_ntu += np.random.uniform(80, 150)

    return round(dp_bar, 2), round(turbidity_ntu, 1), round(flow_lpm, 1)


def process_analytics(dp, turbidity, flow):
    """Predictive Logic Engine based on Physics Rules"""
    risk_score = 0
    status = "NORMAL"
    recommendation = "System Healthy. No action required."

    # Rule 1: High Differential Pressure (Filter Clogged)
    if dp > 1.2:
        risk_score += 40
        status = "WARNING"
        recommendation = "Initiate Automatic Backwash Cycle immediately."

    # Rule 2: High Turbidity (Scale / Mud Contamination)
    if turbidity > 60:
        risk_score += 45
        status = "CRITICAL"
        recommendation = (
            "High Scale Density! Risk of Nozzle Clogging & Billet Bending!"
        )

    # Rule 3: Low DP + High Turbidity (Filter Damaged / Ruptured)
    if dp < 0.1 and turbidity > 50:
        risk_score += 90
        status = "CATASTROPHIIC RISK"
        recommendation = (
            "FILTER RUPTURED! Raw solids entering spray nozzles directly!"
        )

    # Rule 4: Flow Drop
    if flow < 90:
        risk_score += 20

    risk_score = min(risk_score, 100)
    return status, risk_score, recommendation


# Simulation Loop
print("=" * 65)
print("  SMART KIDNEY-LOOP IIOT ANALYTICS ENGINE - CCM SPRAY CAGE")
print("=" * 65)

for i in range(1, 6):
    dp, turbidity, flow = generate_sensor_data()
    status, risk, rec = process_analytics(dp, turbidity, flow)

    print(f"\n[READING #{i}]")
    print(f"|-- Differential Pressure (DP): {dp} Bar")
    print(f"|-- Water Turbidity          : {turbidity} NTU")
    print(f"|-- Spray Flow Rate          : {flow} LPM")
    print(f"|-- Process Health Status    : [{status}]")
    print(f"|-- Nozzle Clogging Risk     : {risk}%")
    print(f"|-- Action Recommendation    : {rec}")
    print("-" * 65)
    time.sleep(1)
