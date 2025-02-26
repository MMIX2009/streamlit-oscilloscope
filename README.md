# Virtual Oscilloscope - Streamlit App

## Overview
This project is a **Virtual Oscilloscope** implemented using **Streamlit**. It allows users to visualize waveforms with adjustable settings such as **input type, gain, time division, voltage division, offsets, and color scheme**.

## Features
- **Simulated Signals**: Supports live input (simulated noise), sine wave, and square wave.
- **Adjustable Parameters**:
  - Input wave frequency (1 - 500 Hz)
  - Oscilloscope gain (0.1x to 10x)
  - Time division settings (1ms to 10ms per division)
  - Voltage division settings (1V to 10V per division)
  - Horizontal and vertical offsets
  - Color scheme customization (Default, Dark Mode, Light Mode)
- **Live Updates**: The waveform continuously updates unless frozen.

## Installation
### Prerequisites
- Python 3.7+
- Streamlit
- NumPy
- Matplotlib

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/streamlit-oscilloscope.git
   cd streamlit-oscilloscope
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Usage
- Select the desired **input type** (Live, Sine Wave, Square Wave)
- Adjust settings such as **gain, time per division, voltage per division, offsets**
- Click the **Freeze Live Input** checkbox to stop waveform updates
- Observe the **real-time oscilloscope** simulation

## Contributing
If you want to enhance this project:
1. Fork the repository
2. Create a new branch
3. Implement your changes
4. Submit a pull request

## License
This project is licensed under the **MIT License**.

---

🚀 **Enjoy your virtual oscilloscope experience!**

