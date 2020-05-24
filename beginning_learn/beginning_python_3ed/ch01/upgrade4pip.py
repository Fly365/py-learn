# -*- coding:utf-8 -*-
import pip
from subprocess import call
from pip._internal.utils.misc import get_installed_distributions

# pip version 9.0.1
# for dist in pip.get_installed_distributions():
# pip version 10.0.1
for dist in get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)