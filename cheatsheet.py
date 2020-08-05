import bpy


class CreateCheatsheetOperator(bpy.types.Operator):
    bl_idname = "object.create_key_cheatsheet"
    bl_label = "Create Cheatsheet"

    def execute(self, context):
        # USERPREF_PT_keymap
        print("creating cheatsheet")
        return {"FINISHED"}


class AMB_PT_CheatsheetPanel(bpy.types.Panel):
    bl_space_type = 'PREFERENCES'
    bl_label = "Cheatsheet"
    bl_region_type = 'WINDOW'
    bl_options = {'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):
        prefs = context.preferences
        return (prefs.active_section == 'KEYMAP')

    def draw(self, context):
        r = self.layout.box().row()
        r.label(text="Test")
