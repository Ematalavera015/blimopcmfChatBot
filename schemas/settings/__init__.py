from settings.server import server_manager
from dotenv import load

import os

if server_manager.get_app().debug:
    env_ruta = os.path.abspath(__file__).replace("__init__.py",".env")
    load(env_ruta)
