# -*- coding: utf-8 -*-
# Copyright (c) 2020 Warpnet B.V.

from saltlint.linter.rule import DeprecationRule


class StateDeprecationVirtRevertedRule(DeprecationRule):
    id = '903'
    state = 'virt.reverted'
    deprecated_since = '2016.3.0'
    version_added = 'develop'
