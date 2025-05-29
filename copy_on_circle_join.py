import bpy
import math
# アドオンであることを示す
bl_info = {
    "name": "サンプルアドオン: 円上にコピーして結合",
    "author": "3dloverblender",
    "version": (1, 0, 0),
    "blender": (4, 4, 0),
    "location": "3Dビューポート > 追加 > メッシュ",
    "description": "選択されたオブジェクトを円上にコピーして結合するアドオン",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "category": "Sample"
}
# オペレータークラスを継承
class SAMPLE_OT_CopyOnCircleJoin(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.copy_on_cirlce_join"
    # オペレーターの表示名
    bl_label = "円状にコピーし結合"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトを円上にコピーして結合します"
    bl_options = {'REGISTER', 'UNDO'}
    # 分割角度
    div_deg: bpy.props.IntProperty(
        name = "分割角度",
        description = "円上にコピーする際の分割角度",
        default = 10,
        min = 1,
        max = 360,
    )
    # 座標軸
    axis: bpy.props.EnumProperty(
        name = "座標軸",
        description = "円上にコピーする際の座標軸",
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

classes = [
    SAMPLE_OT_CopyOnCircleJoin,
]

def register():
    for c in classes:
        bpy.utils.register_class(c)
    
    print(f"アドオン『{bl_info['name']}』が有効化されました。")


def unregister():
    for c in reversed(classes):
        bpy.utils.unregister_class(c)
    print(f"アドオン『{bl_info['name']}』が無効化されました。")
