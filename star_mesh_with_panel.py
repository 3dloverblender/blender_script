import bpy
import bmesh
import math

bl_info = {
    "name": "サンプルアドオン: 星形メッシュ",
    "author": "ぬっち",
    "version": (1, 0, 0),
    "blender": (3, 3, 0),
    "location": "3Dビューポート > サイドバー > カスタム",
    "description": "平面の星形メッシュを作成するアドオン",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "category": "Sample"
}


class SAMPLE_OT_CreateStarPolygon(bpy.types.Operator):

    bl_idname = "sample.create_star_polygon"
    bl_label = "星形メッシュを作成"
    bl_description = "星形メッシュを作成します"
    bl_options = {'REGISTER', 'UNDO'}

    num_sides: bpy.props.IntProperty(
        name="角数",
        description="星形メッシュの角数",
        default=10,
        min=4,
        max=20
    )

    radius: bpy.props.FloatProperty(
        name="サイズ",
        description="星形メッシュのサイズ",
        default=100.0,
        min=1.0,
        max=1000.0
    )

    def execute(self, context):
        num_sides = self.num_sides
        radius = self.radius

        new_mesh = bpy.data.meshes.new("Regular N-sided Star Polygon")
        new_obj = bpy.data.objects.new("Regular N-sided Star Polygon", new_mesh)
        bpy.context.scene.collection.objects.link(new_obj)
        bpy.context.view_layer.objects.active = new_obj
        new_obj.select_set(True)

        bm = bmesh.new()
        verts = []
        dtheta = 2 * math.pi / num_sides
        for i in range(num_sides):
            outer_x = radius * math.cos(dtheta * i)
            outer_y = radius * math.sin(dtheta * i)
            outer_vert = bm.verts.new([outer_x, outer_y, 0.0])
            verts.append(outer_vert)
            inner_x = (radius/2) * math.cos(dtheta * (i+0.5))
            inner_y = (radius/2) * math.sin(dtheta * (i+0.5))
            inner_vert = bm.verts.new([inner_x, inner_y, 0.0])
            verts.append(inner_vert)
        bm.faces.new(verts)
        bm.to_mesh(new_mesh)

        print("オペレータを実行しました。")

        return {'FINISHED'}


class SAMPLE_PT_Custom(bpy.types.Panel):

    bl_idname = "SAMPLE_PT_Custom"
    bl_label = "星形メッシュの作成"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "カスタム"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='PLUGIN')

    def draw(self, context):
        layout = self.layout
        layout.operator(SAMPLE_OT_CreateStarPolygon.bl_idname, text="作成")


classes = [
    SAMPLE_OT_CreateStarPolygon,
    SAMPLE_PT_Custom,
]


def register():
    for c in classes:
        bpy.utils.register_class(c)
    print(f"アドオン『{bl_info['name']}』が有効化されました。")


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
    print(f"アドオン『{bl_info['name']}』が無効化されました。")
