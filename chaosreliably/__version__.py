try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:
    from importlib_metadata import PackageNotFoundError, version  # type: ignore


try:
    __version__ = version("chaostoolkit-reliably")
except PackageNotFoundError:
    __version__ = "unknown"
