from environ import Env

env = Env()

environment = env.str('environment', 'local')
if environment == 'local':
    from .local import *
elif environment == 'dev':
    from .dev import *
elif environment == 'prod':
    from .prod import *
else:
    raise Exception()
