# =====================================
# generator=datazen
# version=3.1.4
# hash=6bb2aba70c4b665b99c01cc2458623b5
# =====================================

"""
instagram-emoji-bucketizer - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from instagram_emoji_bucketizer_bootstrap.setup import setup  # type: ignore

# internal
from instagram_emoji_bucketizer import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Dylan Fromm",
    "email": "dylanfromm@hotmail.com",
    "username": "dylanfromm",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.8",
        "3.9",
        "3.10",
        "3.11",
    ],
}
setup(
    pkg_info,
    author_info,
)
