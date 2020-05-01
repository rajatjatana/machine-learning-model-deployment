import pathlib
import regression_model

PACKAGE_ROOT = pathlib.Path(regression_model.__file__).resolve().parent
DATASET_DIR = PACKAGE_ROOT / 'datasets'
