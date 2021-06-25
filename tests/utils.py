import os

from importlib import import_module
def data_file(name):
    return os.path.join(os.path.dirname(__file__), 'data', name)





def is_package_installed(package):
    """return true if all packages in "package" are installed"""
    if isinstance(package, (list, tuple)):
        installed = [p for p in package if is_package_installed(p)]
        if len(installed) != len(package):
            return False
        return True

    try:
        import_module(package)
        return True
    except ImportError:
        return False
