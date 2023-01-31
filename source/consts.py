import os


# File Path(s)
SHARE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGES_LIST = os.path.join(SHARE_DIR, 'images.yaml')
ROOT_DIR = os.path.abspath(os.path.join(SHARE_DIR, os.pardir))
OUTPUT_DIR = os.path.join(ROOT_DIR, 'target')
JINJA_TEMPLATE = 'template.j2'

# K8S Resources Config(s)
NAMESPACE = 'interop-scale'
