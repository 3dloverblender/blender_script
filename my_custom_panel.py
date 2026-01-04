import bpy
import math

bl_info = {
    "name": "サンプルアドオン: 自分用カスタムパネル",
    "author": "3dloverblender",
    "version": (1, 0, 0),
    "blender": (4, 5, 0),
    "location": "3Dビューポート > サイドバー > カスタム",
    "description": "自分なりによく使う機能をまとめたパネルアドオン",
    "warning": "",
    "support": "COMMUNITY",
    "doc_url": "",
    "tracker_url": "",
    "category": "Sample"
}

# 3Dカーソルをワールド原点へ移動するオペレーター
class SAMPLE_OT_CursorToWorldOrigin(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.cursor_to_world_origin"
    # オペレーターの表示名
    bl_label = "3Dカーソル→ワールド原点"
    # オペレーターの説明
    bl_description = "3Dカーソルをワールド原点へ移動します"
    bl_options = {'REGISTER', 'UNDO'}

    # オペレータで実行する内容
    def execute(self, context):
        # 3Dカーソルの位置をワールド原点に設定
        bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
        print("3Dカーソルをワールド原点へ移動しました。")
        return {'FINISHED'}

# 3Dカーソルを選択物にスナップするオペレーター
class SAMPLE_OT_CursorToSelected(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.cursor_to_selected"
    # オペレーターの表示名
    bl_label = "3Dカーソル→選択物"
    # オペレーターの説明
    bl_description = "3Dカーソルを選択物にスナップします"
    bl_options = {'REGISTER', 'UNDO'}

    # オペレータで実行する内容
    def execute(self, context):
        # 3Dカーソルを選択物にスナップする
        bpy.ops.view3d.snap_cursor_to_selected()
        print("3Dカーソルを選択物の中心へ移動しました。")
        return {'FINISHED'}

# オブジェクトの原点を3Dカーソルの位置に移動するオペレーター
class SAMPLE_OT_OriginToCursor(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.origin_to_cursor"
    # オペレーターの表示名
    bl_label = "オブジェクト原点→3Dカーソル"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトの原点を3Dカーソルの位置に移動します"
    bl_options = {'REGISTER', 'UNDO'}

    # オペレータで実行する内容
    def execute(self, context):
        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        if obj is None:
            print("No active object selected.")
            return {'CANCELLED'}
        
        # オブジェクトの原点を3Dカーソルの位置に移動
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
        print("オブジェクトの原点を3Dカーソルへ移動しました。")
        return {'FINISHED'}

# 選択したオブジェクトを3Dカーソルの位置に移動するオペレーター
class SAMPLE_OT_MoveToCursor(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.move_to_cursor"
    # オペレーターの表示名
    bl_label = "選択物→3Dカーソル"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトを3Dカーソルの位置に移動します"
    bl_options = {'REGISTER', 'UNDO'}

    # オペレータで実行する内容
    def execute(self, context):
        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        if obj is None:
            print("No active object selected.")
            return {'CANCELLED'}

        # オブジェクトを3Dカーソルの位置に移動
        cursor_location = bpy.context.scene.cursor.location
        obj.location = cursor_location
        print("オブジェクトを3Dカーソルの位置に移動しました。")
        return {'FINISHED'}

# 選択したオブジェクトをx軸に90度回転するオペレーター
class SAMPLE_OT_RotateX90(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.rotate_x_90"
    # オペレーターの表示名
    bl_label = "X軸に90度回転"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトをX軸に90度回転します"
    bl_options = {'REGISTER', 'UNDO'}

    # オペレータで実行する内容
    def execute(self, context):
        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        if obj is None:
            print("No active object selected.")
            return {'CANCELLED'}

        # X軸に90度回転
        obj.rotation_euler[0] += math.radians(90)
        print("オブジェクトをX軸に90度回転しました。")
        return {'FINISHED'}

# 選択したオブジェクトをY軸に90度回転するオペレーター
class SAMPLE_OT_RotateY90(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.rotate_y_90"
    # オペレーターの表示名
    bl_label = "Y軸に90度回転"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトをY軸に90度回転します"
    bl_options = {'REGISTER', 'UNDO'}
    
    # オペレータで実行する内容
    def execute(self, context):
        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        if obj is None:
            print("No active object selected.")
            return {'CANCELLED'}

        # Y軸に90度回転
        obj.rotation_euler[1] += math.radians(90)
        print("オブジェクトをY軸に90度回転しました。")
        return {'FINISHED'}

# 選択したオブジェクトをZ軸に90度回転するオペレーター
class SAMPLE_OT_RotateZ90(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.rotate_z_90"
    # オペレーターの表示名
    bl_label = "Z軸に90度回転"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトをZ軸に90度回転します"
    bl_options = {'REGISTER', 'UNDO'}
    
    # オペレータで実行する内容
    def execute(self, context):
        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        if obj is None:
            print("No active object selected.")
            return {'CANCELLED'}

        # Z軸に90度回転
        obj.rotation_euler[2] += math.radians(90)
        print("オブジェクトをZ軸に90度回転しました。")
        return {'FINISHED'} 

# 選択したオブジェクトの回転とスケールを適用するオペレーター
class SAMPLE_OT_ApplyRotationScale(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.apply_rotation_scale"
    # オペレーターの表示名
    bl_label = "回転スケール適用"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトの回転とスケールを適用します"
    bl_options = {'REGISTER', 'UNDO'}

    # オペレータで実行する内容
    def execute(self, context):
        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        if obj is None:
            print("No active object selected.")
            return {'CANCELLED'}

        # 回転とスケールを適用
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        print("回転とスケールを適用しました。")
        return {'FINISHED'}

# 選択したオブジェクトの重複頂点をすべてマージするオペレーター
class SAMPLE_OT_MergeDoubles(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.merge_doubles"
    # オペレーターの表示名
    bl_label = "重複頂点マージ"
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

# トランスフォームピボットポイントをアクティブ要素に設定して指定された軸を0倍にスケールするオペレーター
class SAMPLE_OT_ScaleToZero(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.scale_to_zero"
    # オペレーターの表示名
    bl_label = "アクティブ要素を基準に指定軸で揃える"
    # オペレーターの説明
    bl_description = "アクティブ要素を基準に指定軸で座標を揃えます"
    bl_options = {'REGISTER', 'UNDO'}
    
    # 座標軸
    axis: bpy.props.EnumProperty(
        name = "座標軸",
        description = "揃える座標軸",
        items = [
            ('X', "X軸", "X座標で揃える"),
            ('Y', "Y軸", "Y座標で揃える"),
            ('Z', "Z軸", "Z座標で揃える"),
        ],
        default = 'Z',
    )

    # オペレータで実行する内容
    def execute(self, context):
        axis = self.axis

        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        if obj is None:
            print("No active object selected.")
            return {'CANCELLED'}

        # トランスフォームピボットポイントをアクティブ要素に設定
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'

        # 指定された軸を0倍にスケール
        if axis == 'X':
            # X座標のスケールを0にする
            bpy.ops.transform.resize(value=(0.0, 1.0, 1.0))
        elif axis == 'Y':
            # Y座標のスケールを0にする
            bpy.ops.transform.resize(value=(1.0, 0.0, 1.0))
        elif axis == 'Z':
            # Z座標のスケールを0にする
            bpy.ops.transform.resize(value=(1.0, 1.0, 0.0))

        print(f"{axis}軸を0倍にスケールしました。")
        return {'FINISHED'}

# 選択されたオブジェクトにスピンを適用するオペレーター
class SAMPLE_OT_SpinObjects(bpy.types.Operator):
    # オペレーターID
    bl_idname = "sample.spin_objects"
    # オペレーターの表示名
    bl_label = "スピン適用"
    # オペレーターの説明
    bl_description = "選択されたオブジェクトにスピンを適用します"
    bl_options = {'REGISTER', 'UNDO'}

    # オペレータで実行する内容
    def execute(self, context):
        # 選択されたオブジェクトを取得
        obj = bpy.context.active_object
        if obj is None:
            print("No active object selected.")
            return {'CANCELLED'}

        # スピンを適用（例: 360度、36ステップ）
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.spin(steps=36, angle=math.radians(360), center=(0,0,0), axis=(0,0,1))
        bpy.ops.object.mode_set(mode='OBJECT')

        print("スピンを適用しました。")
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

# カスタムパネルの定義
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
        layout.operator(SAMPLE_OT_CursorToWorldOrigin.bl_idname, text="3Dカーソル → ワールド原点", icon='CURSOR')
        layout.operator(SAMPLE_OT_CursorToSelected.bl_idname, text="3Dカーソル → 選択物", icon='CURSOR')
        layout.operator(SAMPLE_OT_OriginToCursor.bl_idname, text="オブジェクト原点 → 3Dカーソル", icon='CURSOR')
        layout.operator(SAMPLE_OT_MoveToCursor.bl_idname, text="選択物 → 3Dカーソル", icon='CURSOR')
        layout.separator()
        layout.operator(SAMPLE_OT_RotateX90.bl_idname, text="X軸に90度回転", icon='DRIVER_ROTATIONAL_DIFFERENCE')
        layout.operator(SAMPLE_OT_RotateY90.bl_idname, text="Y軸に90度回転", icon='DRIVER_ROTATIONAL_DIFFERENCE')
        layout.operator(SAMPLE_OT_RotateZ90.bl_idname, text="Z軸に90度回転", icon='DRIVER_ROTATIONAL_DIFFERENCE')
        layout.separator()
        layout.operator(SAMPLE_OT_ApplyRotationScale.bl_idname, text="回転スケール適用", icon='FILE_TICK')
        layout.separator()
        layout.operator(SAMPLE_OT_MergeDoubles.bl_idname, text="重複頂点マージ", icon='MESH_CUBE')
        layout.separator()
        layout.operator(SAMPLE_OT_ScaleToZero.bl_idname, text="アクティブ要素基準 → 座標統一", icon='SNAP_PEEL_OBJECT')
        layout.separator()
        layout.operator(SAMPLE_OT_SpinObjects.bl_idname, text="スピン適用", icon='MOD_ARRAY')
        layout.separator()
        layout.operator(SAMPLE_OT_CopyOnCircleJoin.bl_idname, text="円状コピー結合", icon='MOD_ARRAY')

# 登録するクラスのリスト
classes = [
    SAMPLE_OT_CursorToWorldOrigin,
    SAMPLE_OT_CursorToSelected,
    SAMPLE_OT_OriginToCursor,
    SAMPLE_OT_MoveToCursor,
    SAMPLE_OT_RotateX90,
    SAMPLE_OT_RotateY90,
    SAMPLE_OT_RotateZ90,
    SAMPLE_OT_ApplyRotationScale,
    SAMPLE_OT_MergeDoubles,
    SAMPLE_OT_ScaleToZero,
    SAMPLE_OT_SpinObjects,
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
