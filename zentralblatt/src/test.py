#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# zentralblatt - zentralblatt metadata plugin for calibre
# Copyright 2012 Abdó Roig-Maranges <abdo.roig@gmail.com>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import (unicode_literals, division)


# To run these test use:
# calibre-debug -e test.py

if __name__ == '__main__':
    from calibre.ebooks.metadata.sources.test import (test_identify_plugin,
         title_test, authors_test)

    tests_list = [
        ({'identifiers': {"zbl" : "1140.18005"}},
         [title_test("Moduli of objects in dg-categories"),
          authors_test(['Bertrand Toën', 'Michel Vaquié'])]),

        ({'identifiers': {"zbl" : "0129.15601"}},
         [title_test("The stable homotopy of the classical groups"),
          authors_test(['Raoul Bott'])]),

        ({'title': "Superconnections, Thom classes", 'authors':['Mathai', 'Daniel Quillen']},
         [title_test("Superconnections, Thom classes, and equivariant differential forms"),
          authors_test(['Varghese Mathai', 'Daniel Quillen'])]),

        ({'title': "sur le nombre des points rationnels", 'authors':['serre']},
         [title_test("Sur le nombre des points rationnels d'une courbe algébrique sur un corps fini"),
          authors_test(['Jean-Pierre Serre'])]),

        ]

    test_identify_plugin("Zentralblatt", tests_list)



# vim: expandtab:shiftwidth=4:tabstop=4:softtabstop=4:textwidth=80
