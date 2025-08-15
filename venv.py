import sys
    print('Python version')
    print(sys.version)
    print('Version info.')
    print(sys.version_info)

import subprocess

try:
    result = subprocess.run(['pip', '--version'], capture_output=True, text=True, check=True)
   
    pip_version_line = result.stdout.strip()
    pip_version = pip_version_line.split(' ')[1]
    
    print(fPIP Version: {pip_version})

except subprocess.CalledProcessError as e:
    print(fError checking PIP version: {e})
    print(fStderr: {e.stderr})
except FileNotFoundError:
    print(Error: pip command not found. Ensure pip is installed and in your systems PATH.)
