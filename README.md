<h1 align="center">⚙️ LabVIEW ↔ Python Predictive Maintenance Bridge</h1>

<p align="center">
  A hybrid architecture demonstrating how to process high-speed LabVIEW DAQ data through a Python Machine Learning backend for real-time Predictive Maintenance and Anomaly Detection.
</p>

## 🚀 Overview

Modern Test & Measurement systems require advanced data analytics (Machine Learning, FFTs, Neural Networks). Instead of rewriting complex Python AI models in LabVIEW, this project demonstrates how to use LabVIEW's native **Python Node** to stream sensor data (Vibration, Acoustic Emission) directly into Python, process it, and return the Machine Health status to the LabVIEW Front Panel.

## 📁 Repository Contents

- `predictive_ai.py` - The Python backend that processes 1D arrays of sensor data, calculates RMS/Peak-to-Peak features, and returns an anomaly score.
- `Main.vi` - *(You will build this following the instructions below!)* The LabVIEW UI that simulates or reads DAQ data and calls the Python script.

## 🛠️ How to Build the LabVIEW VI (`Main.vi`)

Because LabVIEW `.vi` files are binary and tied to specific LabVIEW versions, I have provided the exact architecture so you can wire it up in 2 minutes:

### 1. The Block Diagram
Drop these 3 nodes onto your Block Diagram (found in **Connectivity -> Python**):
1. **Open Python Session**: Set the version string to `"3.9"` (or your installed Python version).
2. **Python Node**: 
   - **Module Path**: Wire a path constant pointing to `predictive_ai.py`.
   - **Function Name**: Wire a string constant `"analyze_vibration"`.
   - **Input Terminal**: Wire a `1D Array of DBL` (your simulated vibration data).
   - **Return Type**: Wire a Cluster containing: `(Numeric DBL, String, Boolean)`.
3. **Close Python Session**: Wire the session out from the Python Node into this.

### 2. The Front Panel
Add the following indicators to show the results returned from Python:
- **Anomaly Score** (Numeric Indicator)
- **Machine Health Status** (String Indicator)
- **Warning LED** (Boolean Indicator)

## 💡 Why This Architecture is Powerful

By keeping Hardware I/O (DAQmx, Modbus, RS-485) in **LabVIEW**, and heavy Data Science / AI in **Python**, you get the best of both worlds. This exact architecture is currently being adopted by major aerospace and manufacturing companies for Industry 4.0 upgrades.

---
*Created by Kiran Shivakumar*
