# -*- coding: utf-8 -*-

# SPDX-License-Identifier: MIT
# Copyright © 2021 André Santos

###############################################################################
# Imports
###############################################################################

from __future__ import unicode_literals
from builtins import str
from collections import namedtuple


###############################################################################
# Module Functions
###############################################################################

def node2cbmc(node):
    cpp_files = node.source_files # haros.metamodel > SourceFile
    hpl_properties = node.hpl_properties # haros.hpl.hpl_ast > HplProperty
    advertised_topics = node.advertise # haros.metamodel > AdvertiseCall
    subscribed_topics = node.subscribe # haros.metamodel > SubscribeCall
    return NodeData()


def render_cbmc(jinja, node_data, strip=True):
    template = jinja.get_template('node.c.jinja')
    cbmc_src = template.render(data=node_data).encode('utf-8')
    if strip:
        cbmc_src = cbmc_src.strip()
    return cbmc_src


###############################################################################
# Data Structures
###############################################################################

NodeData = namedtuple('NodeData', ())


###############################################################################
# Helper Functions
###############################################################################
