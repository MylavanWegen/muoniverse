import sys
import numpy, pandas, xarray, matplotlib

print("Python:", sys.version.split()[0])
print("Running from:", sys.executable)
print("numpy", numpy.__version__, "| pandas", pandas.__version__,
      "| xarray", xarray.__version__)