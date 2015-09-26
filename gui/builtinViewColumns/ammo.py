#===============================================================================
# Copyright (C) 2010 Diego Duclos
#
# This file is part of pyfa.
#
# pyfa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfa.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

from gui import builtinViewColumns
from gui.viewColumn import ViewColumn
from gui import bitmapLoader
import wx

class Ammo(ViewColumn):
    name = "Ammo"
    def __init__(self, fittingView, params):
        ViewColumn.__init__(self, fittingView)
        self.mask = wx.LIST_MASK_IMAGE
        self.imageId = fittingView.imageList.GetImageIndex("damagePattern_small", "icons")
        self.bitmap = bitmapLoader.getBitmap("damagePattern_small", "icons")

    def getText(self, stuff):
        if getattr(stuff, "charge", None) is not None:
            charges = stuff.numCharges
            if charges > 0:
                cycles = stuff.numShots
                if charges != cycles:
                    return "%s (%d, %d cycles)" % (stuff.charge.name, charges, cycles)
                else:
                    return "%s (%d)" % (stuff.charge.name, charges)
            else:
                return stuff.charge.name
        return ""

    def getImageId(self, mod):
        return -1

Ammo.register()
