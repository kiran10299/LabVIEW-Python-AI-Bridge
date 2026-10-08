import math

def analyze_vibration(sensor_data):
    """
    This function is designed to be called directly from LabVIEW via the Python Node.
    
    Args:
        sensor_data (list of floats): A 1D array of vibration or acoustic data passed from LabVIEW.
        
    Returns:
        tuple: (anomaly_score (float), status_message (str), is_warning (bool))
    """
    if not sensor_data or len(sensor_data) == 0:
        return 0.0, "ERROR: No data received from LabVIEW", True

    # 1. Calculate basic statistical features (Root Mean Square)
    squared_sum = sum(x**2 for x in sensor_data)
    rms = math.sqrt(squared_sum / len(sensor_data))
    
    # 2. Calculate Peak-to-Peak
    peak_to_peak = max(sensor_data) - min(sensor_data)
    
    # 3. Simple Anomaly Detection Algorithm (Simulated AI Model)
    # In a real-world scenario, you would load a TensorFlow/Scikit-Learn model here.
    # For this demo, we assume RMS > 2.5 or Peak > 6.0 indicates bearing wear/cavitation.
    
    anomaly_score = (rms * 0.7) + (peak_to_peak * 0.3)
    
    is_warning = False
    if anomaly_score < 2.0:
        status_message = "Machine Health: OPTIMAL"
    elif anomaly_score < 4.0:
        status_message = "Machine Health: WARNING (Check Bearings)"
        is_warning = True
    else:
        status_message = "Machine Health: CRITICAL (Imminent Failure)"
        is_warning = True
        
    # Return data back to LabVIEW
    return float(anomaly_score), str(status_message), bool(is_warning)

# For testing outside of LabVIEW:
if __name__ == "__main__":
    test_data = [0.1, -0.2, 0.5, -0.1, 0.0, 3.1, -2.5, 0.4]
    score, msg, warn = analyze_vibration(test_data)
    print(f"Score: {score:.2f} | Status: {msg} | Warning: {warn}")
