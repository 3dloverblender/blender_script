import bpy
import bmesh
import math
# アドオンであることを示す
bl_info = {
    "name": "サンプルアドオン: スクリューメッシュ",
    "author": "3dloverblender",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),
    "location": "3Dビューポート > 追加 > メッシュ",
    "description": "スクリュー型のメッシュを作成するアドオン",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "category": "Sample"
}
# オペレータークラスを継承して、メッシュを作成するクラスを定義
class SAMPLE_OT_CreateScrewMesh(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.create_screw_mesh"
    # オペレーターの表示名
    bl_label = "スクリュー型メッシュを作成"
    # オペレーターの説明
    bl_description = "スクリュー形メッシュを作成します"
    bl_options = {'REGISTER', 'UNDO'}
    # 巻き回数
    screw_count: bpy.props.IntProperty(
        name = "巻き回数",
        description = "スクリューの巻き回数",
        default = 1,
        min = 1,
    )
    # 半径
    radius: bpy.props.FloatProperty(
        name = "半径",
        description = "スクリューの半径",
        default = 1.0,
        min = 0.1,
        max = 100.0,
    )
    # オペレータで実行する内容
    def execute(self, context):
        screw_count = self.screw_count
        radius = self.radius

        # メッシュを作成する
        new_mesh = bpy.data.meshes.new("Screw")
        # オブジェクトを作成する
        new_obj = bpy.data.objects.new("Screw", new_mesh)
        # 現在のシーンにオブジェクトをリンクさせる
        bpy.context.scene.collection.objects.link(new_obj)
        # 作成したオブジェクトをアクティブオブジェクトにする
        bpy.context.view_layer.objects.active = new_obj
        # 作成したオブジェクトを選択状態にする
        new_obj.select_set(True)

        # BMeshを作成する
        bm = bmesh.new()
        verts = []
        # 角度
        deg = 10
        # 初期z座標
        z = 0.0
        # z座標の増加量
        dz = 0.01
        # バネの頂点を作成する
        for deg in range(0, 360 * screw_count, deg):
            # 角度をラジアンに変換
            rad = math.radians(deg)
            # x, y座標を計算
            x = radius * math.cos(rad)
            y = radius * math.sin(rad)
            # z座標を計算
            z += dz
            # 頂点を作成
            vert = bm.verts.new((x, y, z))
            # 頂点をリストに追加
            verts.append(vert)
        
        # 頂点と頂点を結ぶ
        for i in range(len(verts) - 1):
            v1 = verts[i]
            v2 = verts[i + 1]
            # エッジを作成
            bm.edges.new((v1, v2))
        
        # BMeshをメッシュオブジェクトに変換する
        bm.to_mesh(new_mesh)
        # カーブに変換する
        bpy.ops.object.convert(target='CURVE')
        # カーブのへベル深度を設定する
        bpy.data.curves["Screw"].bevel_depth = 0.2
        # オブジェクトを選択状態にする
        new_obj.select_set(True)
        # メッシュに変換する
        bpy.ops.object.convert(target='MESH')

        print("オペレータを実行しました。")

        return {'FINISHED'}

def menu_register_func(cls, context):
    cls.layout.separator()
    cls.layout.operator(SAMPLE_OT_CreateScrewMesh.bl_idname, icon='PLUGIN')


classes = [
    SAMPLE_OT_CreateScrewMesh,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_register_func)
    print(f"アドオン『{bl_info['name']}』が有効化されました。")


def unregister():
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_register_func)
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
    print(f"アドオン『{bl_info['name']}』が無効化されました。")
