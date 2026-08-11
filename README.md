  
# 🌊 Smart Kidney-Loop IIoT Analytics Engine (CCM Spray Cage)

> **A Physics-driven Edge-AI Predictive Analytics Engine designed to eliminate multi-crore quality rejections in Continuous Casting Machines (CCM) secondary cooling.**

---

## 📌 Problem Statement
Traditional SCADA systems rely on static pressure thresholds. When a cooling filter mesh tears ($\Delta P \to 0$), SCADA assumes normal low pressure, while raw suspended scales enter the spray cage directly—causing catastrophic multi-nozzle blockages, asymmetric cooling, and 12-meter billet warping.

## 💡 The Edge-AI Solution
A non-intrusive modular Bypass / Kidney-Loop Analytics Engine built in Python that utilizes **Multi-Sensor Fusion**:

1. **Differential Pressure ($\Delta P$)**
2. **Turbidity (NTU)**
3. **Flow Rate (LPM)**

### Key Features
* **45-Minute Predictive Lead Time:** Warns operators about nozzle clogging risks before thermal deformation occurs.
* **Filter Rupture Detection:** Instantly flags catastrophic filter mesh tears ($\Delta P < 0.1\text{ bar} + \text{High Turbidity}$).
* **High ROI:** Lightweight Edge-AI setup safeguarding multi-crore production lots.

---

## 🛠️ Architecture & Scalability
While designed for CCM Spray Cages, this core logic natively scales across:
* 🏭 **Power Plants:** Condenser & Boiler Feedwater purity
* 🧪 **Pharma Utilities:** WFI Line Contamination
* 🚗 **Automobile Manufacturing:** Robotic Welding Cooling Lines

---

git clone [https://github.com/brahmanrs-virinchi/Smart-kidney-loop-water-analytics-for-heavy-industries.git](https://github.com/brahmanrs-virinchi/Smart-kidney-loop-water-analytics-for-heavy-industries.git)
python main.py


## 📊 Sample Logic Output
```text
======================================================
======= SMART KIDNEY-LOOP IIOT ANALYTICS ENGINE =======
======================================================

[READING #1]
|-- Differential Pressure (DP): 0.01 Bar
|-- Water Turbidity          : 108.9 NTU
|-- Spray Flow Rate          : 115.9 LPM
|-- Process Health Status    : [CATASTROPHIC RISK]
|-- Nozzle Clogging Risk     : 100%
|-- Action Recommendation    : FILTER RUPTURED! Raw solids entering spray nozzles directly!




The Results.

=================================================================
  SMART KIDNEY-LOOP IIOT ANALYTICS ENGINE - CCM SPRAY CAGE
=================================================================

[READING #1]
|-- Differential Pressure (DP): 0.4 Bar
|-- Water Turbidity          : 15.1 NTU
|-- Spray Flow Rate          : 120.6 LPM
|-- Process Health Status    : [NORMAL]
|-- Nozzle Clogging Risk     : 0%
|-- Action Recommendation    : System Healthy. No action required.
-----------------------------------------------------------------

[READING #2]
|-- Differential Pressure (DP): 0.41 Bar
|-- Water Turbidity          : 17.8 NTU
|-- Spray Flow Rate          : 123.7 LPM
|-- Process Health Status    : [NORMAL]
|-- Nozzle Clogging Risk     : 0%
|-- Action Recommendation    : System Healthy. No action required.
-----------------------------------------------------------------

[READING #3]
|-- Differential Pressure (DP): 1.43 Bar
|-- Water Turbidity          : 112.9 NTU
|-- Spray Flow Rate          : 86.1 LPM
|-- Process Health Status    : [CRITICAL]
|-- Nozzle Clogging Risk     : 100%
|-- Action Recommendation    : High Scale Density! Risk of Nozzle Clogging & Billet Bending!
-----------------------------------------------------------------

[READING #4]
|-- Differential Pressure (DP): 0.38 Bar
|-- Water Turbidity          : 15.8 NTU
|-- Spray Flow Rate          : 119.2 LPM
|-- Process Health Status    : [NORMAL]
|-- Nozzle Clogging Risk     : 0%
|-- Action Recommendation    : System Healthy. No action required.
-----------------------------------------------------------------

[READING #5]
|-- Differential Pressure (DP): 0.39 Bar
|-- Water Turbidity          : 12.0 NTU
|-- Spray Flow Rate          : 116.8 LPM
|-- Process Health Status    : [NORMAL]
|-- Nozzle Clogging Risk     : 0%
|-- Action Recommendation    : System Healthy. No action required.
-----------------------------------------------------------------

[Program finished]



