"""For production, we'll automatically generate settings from prod.py via ci/cd script"""
import os

env_name = os.getenv('env_name', 'local')

if env_name == "prod":
    from .prod import *
elif env_name == "stage":
    from .stage import *
else:
    from .local import *
