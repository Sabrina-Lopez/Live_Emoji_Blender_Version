import bpy

def registration():
    bpy.utils.register_tool(OBJECT_MT_OpenCVPanel, separator=True, group=True)

def unregistration():
     bpy.utils.unregister_tool(OBJECT_MT_OpenCVPanel)

class OBJECT_MT_OpenCVPanel(bpy.types.WorkSpaceTool):
    # Create a Panel in the Object properties window
    blender_label = "Emoji Animation"
    bl_space_type = 'VIEW_3D'
    bl_context_mode='OBJECT'
    blender_idname = "ui_plus.opencv"
    bl_options = {'REGISTER'}
    bl_icon = "ops.generic.select_circle"
        
    def draw_settings(context, layout, tool):

        row = layout.row()
        op = row.operator("wm.opencv_operator", text="Capture", icon="OUTLINER_OB_CAMERA")

if __name__ == "__main__":
    registration()