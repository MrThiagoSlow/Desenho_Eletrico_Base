import subprocess
import time
import os

# Path to the ODA File Converter
oda_file_converter_path = r"ODAFileConverter"

# Folder of input and output
input_folder = r"C:\Users\21000015\Documents\GitHub\Desenho_Eletrico_Base\drawer2.dxf"
output_folder = r"C:\Users\21000015\Documents\GitHub\Desenho_Eletrico_Base\drawingODA.dwg"

# Working directory
working_directory = r"ODAFileConverter" # Check this path to make sure it's correct

# Versão do arquivo de saída e tipo de arquivo
output_version = "ACAD2018"
output_type = "DWG"

# Change the working directory
os.chdir(working_directory)

# Start the ODA File Converter
process = subprocess.Popen([oda_file_converter_path, input_folder, output_folder, output_version, output_type],
                            stderr=subprocess.PIPE, stdout=subprocess.PIPE)

# Wait for the process to finish
while process.poll() is None:
    time.sleep(1)

# Print the error messages if any
stderr = process.stderr.read().decode('utf-8')
stdout = process.stdout.read().decode('utf-8')
if stderr:
    print(f"Error: {stderr}")
if stdout:
    print(f"Output: {stdout}")