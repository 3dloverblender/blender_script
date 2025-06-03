import bpy
import math

bl_info = {
    "name": "サンプルアドオン: 自分用カスタムパネル",
    "author": "3dloverblender",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),
    "location": "3Dビューポート > サイドバー > カスタム",
    "description": "自分なりによく使う機能をまとめたパネルアドオン",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "category": "Sample"
}

# 選択したオブジェクトの重複頂点をすべてマージするオペレーター
class SAMPLE_OT_MergeDoubles(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.merge_doubles"
    # オペレーターの表示名
    bl_label = "重複頂点をマージ"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトの重複頂点をすべてマージします"
    bl_options = {'REGISTER', 'UNDO'}

    # オペレータで実行する内容
    def execute(self, context):
        # 編集モードに切り替え
        bpy.ops.object.mode_set(mode='EDIT')
        # すべての頂点を選択
        bpy.ops.mesh.select_all(action='SELECT')
        # すべての頂点をマージ
        bpy.ops.mesh.remove_doubles()
        # オブジェクトモードに戻る
        bpy.ops.object.mode_set(mode='OBJECT')

        print("重複頂点をマージしました。")
        return {'FINISHED'}

# 選択されたオブジェクトを円状にコピーして結合するオペレーター
class SAMPLE_OT_CopyOnCircleJoin(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.copy_on_cirlce_join"
    # オペレーターの表示名
    bl_label = "円状コピー結合"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトを円状にコピーして結合します"
    bl_options = {'REGISTER', 'UNDO'}
    # 分割角度
    div_deg: bpy.props.IntProperty(
        name = "分割角度",
        description = "円状にコピーする際の分割角度",
        default = 10,
        min = 1,
        max = 360,
    )
    # 座標軸
    axis: bpy.props.EnumProperty(
        name = "座標軸",
        description = "円状にコピーする際の座標軸",
        items = [
            ('X', "X軸", "X軸を中心に円上にコピー"),
            ('Y', "Y軸", "Y軸を中心に円上にコピー"),
            ('Z', "Z軸", "Z軸を中心に円上にコピー"),
        ],
        default = 'Z',
    )
    # オペレータで実行する内容
    def execute(self, context):
        div_deg = self.div_deg
        axis = self.axis

        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        # オブジェクトが選択されていない場合は終了
        if obj is None:
            print("No active object selected.")
            return

        # 分割角度のスパンでオブジェクトを円形にコピー
        for deg in range(0, 360, div_deg):
            # 角度をラジアンに変換
            rad = math.radians(deg)
            # オブジェクトのコピーを作成
            new_obj = obj.copy()
            new_obj.data = obj.data.copy()
            # 新しいオブジェクトをシーンにリンク
            bpy.context.collection.objects.link(new_obj)
            # axisの値に応じて新しいオブジェクトを回転して配置
            if axis == 'X':
                new_obj.rotation_euler = (rad, 0, 0)
            elif axis == 'Y':
                new_obj.rotation_euler = (0, rad, 0)
            else:
                new_obj.rotation_euler = (0, 0, rad) 

        # オブジェクトを結合
        bpy.ops.object.join()
        # 編集モードに切り替え
        bpy.ops.object.mode_set(mode='EDIT')
        # すべての頂点を選択
        bpy.ops.mesh.select_all(action='SELECT')
        # すべての頂点をマージ
        bpy.ops.mesh.remove_doubles()
        # オブジェクトモードに戻る
        bpy.ops.object.mode_set(mode='OBJECT') 

        print("オペレータを実行しました。")

        return {'FINISHED'}

class SAMPLE_PT_Custom(bpy.types.Panel):

    bl_idname = "SAMPLE_PT_Custom"
    bl_label = "カスタム"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "カスタム"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon='PLUGIN')

    def draw(self, context):
        layout = self.layout
        layout.operator(SAMPLE_OT_MergeDoubles.bl_idname, text="重複頂点をマージ", icon='MOD_MESHDEFORM')
        layout.separator()
        layout.operator(SAMPLE_OT_CopyOnCircleJoin.bl_idname, text="円状コピー結合", icon='MOD_ARRAY')


classes = [
    SAMPLE_OT_MergeDoubles,
    SAMPLE_OT_CopyOnCircleJoin,
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
