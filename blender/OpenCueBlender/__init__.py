bl_info = {
    "name": "OpenCue Blender Submitter",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "category": "Render",
}

import bpy

class CUSTOM_OT_SubmitToOpenCue(bpy.types.Operator):
    bl_idname = "custom.submit_opencue"
    bl_label = "Submit to OpenCue"

    def execute(self, context):
        self.report({'INFO'}, "This will submit to OpenCue!")
        return {'FINISHED'}

def draw_menu_item(self, context):
    self.layout.separator()
    self.layout.operator(CUSTOM_OT_SubmitToOpenCue.bl_idname)

def register():
    bpy.utils.register_class(CUSTOM_OT_SubmitToOpenCue)
    bpy.types.TOPBAR_MT_render.append(draw_menu_item)

def unregister():
    bpy.types.TOPBAR_MT_render.remove(draw_menu_item)
    bpy.utils.unregister_class(CUSTOM_OT_SubmitToOpenCue)

if __name__ == "__main__":
    register()
