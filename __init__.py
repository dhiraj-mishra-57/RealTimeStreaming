import subprocess

# Specify the path to your .bat file
bat_file_path = r'C:\Users\dhira\PycharmProjects\real-time-streaming\RealTimeStreaming\src\utils\docker\start_services.bat'

# Run the .bat file using subprocess
try:
    subprocess.run([bat_file_path], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running the script: {e}")
