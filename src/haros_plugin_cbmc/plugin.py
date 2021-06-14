# -*- coding: utf-8 -*-

# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

###############################################################################
# Imports
###############################################################################

from __future__ import unicode_literals
import os

from jinja2 import Environment, PackageLoader

from .analyzer import model_check
from .cbmc2haros import parse_output, render_result
from .haros2cbmc import node2cbmc, render_cbmc


###############################################################################
# Plugin Entry Point
###############################################################################

PLUGIN = 'haros_plugin_cbmc'

def package_analysis(iface, pkg):
    for node in pkg.nodes:
        if not node.hpl_properties:
            continue
        if not node.source_files:
            continue
        if not node.language == 'cpp':
            continue
        jinja = Jinja()
        try:
            node_data = node2cbmc(node)
            cbmc_src = render_cbmc(jinja, node_data)
            filename = 'node-{}.c'.format(node.node_name.replace('/', '-'))
            with open(filename, 'w') as f:
                f.write(cbmc_src)
                f.write('\n')
            iface.export_file(filename)
            output = model_check(filename) # passo para analisar, aqui é onde corre o cbmc
            result = parse_output(output, node)
            html = render_result(jinja, result)
            iface.report_violation('counterexample', html)
        except Exception as e:
            iface.log_error(str(e))


###############################################################################
# Data Structures
###############################################################################

def Jinja():
    return Environment(
        loader=PackageLoader(PLUGIN, 'templates'),
        line_statement_prefix=None,
        line_comment_prefix=None,
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=False
    )
