import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Time parameters
time = np.linspace(0, 10, 1000)  # 10 seconds, 1000 data points

# Simulated sensor data
acc_x = 0.5 * np.sin(2 * np.pi * 0.5 * time)  # Accelerometer data (X-axis)
gyro_z = 30 * np.cos(2 * np.pi * 0.2 * time)  # Gyroscope data (Z-axis)

# Add random noise to simulate sensor imperfections
sensor_noise = np.random.normal(0, 0.1, size=time.shape)  # Sensor noise
acc_x_noisy = acc_x + sensor_noise
gyro_z_noisy = gyro_z + sensor_noise

# Add EMI noise to simulate electromagnetic interference
emi_noise = np.random.normal(0, 0.2, size=time.shape)  # EMI noise
acc_x_noisy += emi_noise
gyro_z_noisy += emi_noise

# Function to apply a low-pass filter
def low_pass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return filtfilt(b, a, data)

# Apply the low-pass filter to remove noise
filtered_acc_x = low_pass_filter(acc_x_noisy, cutoff=1, fs=100, order=4)
filtered_gyro_z = low_pass_filter(gyro_z_noisy, cutoff=0.5, fs=100, order=4)

# Plot raw and noisy sensor data
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(time, acc_x, label="True Accelerometer (X)", linestyle="--", color="green")
plt.plot(time, acc_x_noisy, label="Noisy Accelerometer with EMI (X)", color="purple")
plt.title("Accelerometer Data with Noise and EMI")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time, gyro_z, label="True Gyroscope (Z)", linestyle="--", color="green")
plt.plot(time, gyro_z_noisy, label="Noisy Gyroscope with EMI (Z)", color="purple")
plt.title("Gyroscope Data with Noise and EMI")
plt.xlabel("Time (s)")
plt.ylabel("Angular Velocity (deg/s)")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(time, filtered_acc_x, label="Filtered Accelerometer (X)", color="blue")
plt.plot(time, filtered_gyro_z, label="Filtered Gyroscope (Z)", color="orange")
plt.title("Filtered Sensor Data")
plt.xlabel("Time (s)")
plt.ylabel("Filtered Values")
plt.legend()

plt.tight_layout()
plt.show()
