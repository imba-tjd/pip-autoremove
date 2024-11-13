# pip-autoremove-3

For personal use, this is a fork of https://github.com/invl/pip-autoremove. The main difference is that this removed Python2 support.

Install: `pip install git+https://github.com/imba-tjd/pip-autoremove`

As of 0.10.3, this supports Python 3.13 and does not require *setuptools* to be installed in the environment, by changing *pkg_resources* to *pip._vendor.pkg_resources*.
