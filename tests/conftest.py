import sys
from pathlib import Path
path = Path(__file__).parent.parent  # i.e. the folder above the tests folder, which has app
sys.path.append(path)
