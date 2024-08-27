#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Armor
# Copyright (c) 2008-2024 Hive Solutions Lda.
#
# This file is part of Hive Armor.
#
# Hive Armor is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Armor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Armor. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """


class NodeAPI(object):

    def list_nodes(self, *args, **kwargs):
        url = self.base_url + "admin/models/node"
        contents = self.get(url, **kwargs)
        return contents

    def get_node(self, name):
        url = self.base_url + "admin/models/node/" + name
        contents = self.get(url)
        return contents
