import sys
import os

print("Current working directory:", os.getcwd())
print("Python path:", sys.path)

try:
    import app
    print("Successfully imported app")
except ImportError as e:
    print("Failed to import app:", str(e))

print("Contents of current directory:", os.listdir())
