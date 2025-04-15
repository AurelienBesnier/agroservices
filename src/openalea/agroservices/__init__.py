from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("openalea.agroservices")
except PackageNotFoundError:
    # package is not installed
    pass