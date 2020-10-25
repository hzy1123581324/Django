from django import conf


def storeadmin_auto_discover():
    '''
    动态加载模块
    '''
    for app_name in conf.settings.INSTALLED_APPS:
       # mod = importlib.import_module(app_name, 'storeadmin')
        try:
            mod = __import__('%s.storeadmin' % app_name)
            # print(mod.storeadmin)
        except ImportError:
            pass
