import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Streamlit App
st.title("Virtual Oscilloscope")

# Sidebar Controls
input_type = st.selectbox("Input", ["Live Input (5 V peak amp)", "Simulated Sine Wave", "Simulated Square Wave"])
freeze_input = st.checkbox("Freeze Live Input")
input_frequency = st.slider("Input Wave Frequency", 1, 500, 250, disabled=(input_type == "Live Input (5 V peak amp)"))
gain = st.number_input("Oscilloscope gain", 0.1, 10.0, 1.0, step=0.1)
time_div = st.selectbox("Seconds / div", ["1 ms", "2 ms", "5 ms", "10 ms"])
volt_div = st.selectbox("Volts / div", ["1 V", "2 V", "5 V", "10 V"])
h_offset = st.slider("Horizontal Offset", -5.0, 5.0, 0.0, step=0.1)
v_offset = st.slider("Vertical Offset", -5.0, 5.0, 0.0, step=0.1)
color_scheme = st.selectbox("Color scheme", ["Default", "Dark Mode", "Light Mode"])

# Time settings
samples = 1000
time_values = np.linspace(0, 1, samples)  # Simulated 1-second window

# Generate Waveform
def generate_waveform(input_type, freq, gain):
    if input_type == "Simulated Sine Wave":
        return gain * np.sin(2 * np.pi * freq * time_values)
    elif input_type == "Simulated Square Wave":
        return gain * np.sign(np.sin(2 * np.pi * freq * time_values))
    else:
        return np.random.normal(0, 0.1, samples)  # Simulated noise for "Live Input"

# Run Live Simulation
if not freeze_input:
    while True:
        waveform = generate_waveform(input_type, input_frequency, gain)
        plt.figure(figsize=(8, 4))
        plt.plot(time_values + h_offset, waveform + v_offset, color='white' if color_scheme == "Dark Mode" else 'black')
        plt.ylim(-5, 5)
        plt.xlim(0, 1)
        plt.grid(True)
        plt.xlabel("Time (s)")
        plt.ylabel("Voltage (V)")
        st.pyplot(plt)
        time.sleep(0.1)
else:
    waveform = generate_waveform(input_type, input_frequency, gain)
    plt.figure(figsize=(8, 4))
    plt.plot(time_values + h_offset, waveform + v_offset, color='white' if color_scheme == "Dark Mode" else 'black')
    plt.ylim(-5, 5)
    plt.xlim(0, 1)
    plt.grid(True)
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    st.pyplot(plt)
