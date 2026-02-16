import sys
import importlib.util

print(f"Python Executable: {sys.executable}")
print(f"Python Version: {sys.version}")

modules_to_check = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'jupyter', 'notebook', 'ipykernel']

print("\nModule Status:")
for module in modules_to_check:
    spec = importlib.util.find_spec(module)
    found = "✅ Found" if spec else "❌ Missing"
    print(f"{module}: {found}")
