import bpy

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Cheatkey",
    "author": "ambi",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "Alpha",
    "category": "Generic",
}

# from .cheatsheet import CreateCheatsheetOperator, AMB_PT_CheatsheetPanel
# classes = [CreateCheatsheetOperator, AMB_PT_CheatsheetPanel]

from .cheatsheet import CreateCheatsheetOperator
from .hack_rna_keymap_ui import draw_keymaps

classes = [CreateCheatsheetOperator]


def register():
    bpy.types.Scene.cheatkey_show_ui = bpy.props.BoolProperty("Show Cheatkey UI")
    bpy.types.Scene.cheatkey_search_key = bpy.props.StringProperty("Search Key")
    bpy.types.Scene.cheatkey_search_name = bpy.props.StringProperty("Search Name")
    bpy.types.Scene.cheatkey_search_group = bpy.props.StringProperty("Search Group")

    # HACK out addon to the prefs->keymap panel
    def hack_draw(self, context):
        layout = self.layout
        draw_keymaps(context, layout, True)
    bpy.types.USERPREF_PT_keymap.draw = hack_draw

    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes[::-1]:
        bpy.utils.unregister_class(c)

    def hack_draw(self, context):
        layout = self.layout
        draw_keymaps(context, layout, False)
    bpy.types.USERPREF_PT_keymap.draw = hack_draw

    del bpy.types.Scene.cheatkey_show_ui
    del bpy.types.Scene.cheatkey_search_key
    del bpy.types.Scene.cheatkey_search_name
    del bpy.types.Scene.cheatkey_search_group
