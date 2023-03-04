from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("chaostoolkit-reliably")
except PackageNotFoundError:
    __version__ = "unknown"
