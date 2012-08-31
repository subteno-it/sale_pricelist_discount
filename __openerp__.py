# -*- coding: utf-8 -*-
################################################################
#
# sale_pricelist_discount module for OpenERP, Sale pricelist discount
# Copyright (C) 2009-20112 SYLEAM Info Services (<http://www.Syleam.fr/>)
#
# This file is a part of sale_pricelist_discount
#
# sale_pricelist_discount is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sale_pricelist_discount is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################

{
    'name': 'Sale Pricelist Discount',
    'version': '0.2.0',
    'category': 'Custom',
    'description': """Sale Pricelist Discount""",
    'author': 'SYLEAM Info Services',
    'depends': [
            'base',
            'sale',
            'pricelist_discount',
        ],
    'init_xml': [],
    'update_xml': [
        ],
    'demo_xml': [],
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
