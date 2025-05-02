# CREATE ENV
- conda create -n link_online_rl python=3.13

# PACKAGES
- pip install minari[all]
- pip install gymnasium[mujoco]
- pip install wandb
- pip install torch
- pip install scipy
- pip install config-to-object

or 

-  pip install -r requirements.txt

# _a_config
- config.original.ini --> 동일 폴더에 COPY --> config.ini 
- odt_config.original.ini --> 동일 폴더에 COPY --> odt_config.ini

# .ini file to Type Class
- ini_typefile codes/a_config/common/config.original.ini codes/a_config/common/config.py
- ini_typefile codes/a_config/odt/odt_config.original.ini codes/a_config/odt/odt_config.py