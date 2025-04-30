# CREATE ENV
- conda create -n link_offline_rl python=3.13

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
- dt_config.original.ini --> 동일 폴더에 COPY --> dt_config.ini
- cql_config.original.ini --> 동일 폴더에 COPY --> cql_config.ini
- prdc_config.original.ini --> 동일 폴더에 COPY --> prdc_config.ini
- rebrac_config.original.ini --> 동일 폴더에 COPY --> rebrac_config.ini
- td3_bc_config.original.ini --> 동일 폴더에 COPY --> td3_bc_config.ini

# .ini file to Type Class
- ini_typefile codes/a_config/common/config.original.ini codes/a_config/common/config.py
- ini_typefile codes/a_config/dt/dt_config.original.ini codes/a_config/dt/dt_config.py
- ini_typefile codes/a_config/cql/cql_config.original.ini codes/a_config/cql/cql_config.py
- ini_typefile codes/a_config/prdc/prdc_config.original.ini codes/a_config/prdc/prdc_config.py
- ini_typefile codes/a_config/rebrac/rebrac_config.original.ini codes/a_config/rebrac/rebrac_config.py
- ini_typefile codes/a_config/td3_bc/td3_bc_config.original.ini codes/a_config/td3_bc/td3_bc_config.py