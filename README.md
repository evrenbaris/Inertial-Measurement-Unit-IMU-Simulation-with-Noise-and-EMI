# Inertial Measurement Unit (IMU) Simulation with Noise and EMI

This project simulates an Inertial Measurement Unit (IMU) with accelerometer and gyroscope data. It includes realistic noise and electromagnetic interference (EMI) effects and applies signal processing techniques to clean the data.

## Features
- Simulated accelerometer (X-axis) and gyroscope (Z-axis) data.
- Added sensor noise and EMI to simulate real-world conditions.
- Applied low-pass filtering to reduce noise and improve signal quality.
- Visualized raw, noisy, and filtered data in a clear and structured manner.

## Technologies Used
- **Python 3.x**
- **NumPy**: For generating simulated data.
- **Matplotlib**: For data visualization.
- **SciPy**: For signal processing (low-pass filter).

## How to Run
1. Install the required libraries:
   ```bash
   pip install numpy matplotlib scipy
