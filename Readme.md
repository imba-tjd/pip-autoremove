# pip-autoremove-2 (unfinished)

For personal use, this is a fork of https://github.com/invl/pip-autoremove, and it also absorbs some commits from other forks.

Install: `pip install git+https://github.com/imba-tjd/pip-autoremove`

```
Usage: pip-autoremove [OPTION]... [NAME]...

Options:
    -l    list unused dependencies, but don't uninstall them.
    -L  list leaves (packages which are not used by any others).
    -y     don't ask for confirmation of uninstall deletions.
```