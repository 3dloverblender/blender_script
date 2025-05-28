import bpy
import math

# オブジェクトを円形に指定角度でコピーする関数
def copy_on_circle(deg=10):
    # 選択されたオブジェクトを取得
    obj = bpy.context.active_object
    # オブジェクトが選択されていない場合は終了
    if obj is None:
        print("No active object selected.")
        return

    # 円形にコピー
    for deg in range(0, 360, deg):
        # 角度をラジアンに変換
        rad = math.radians(deg)
        # オブジェクトのコピーを作成
        new_obj = obj.copy()
        new_obj.data = obj.data.copy()
        # 新しいオブジェクトをシーンにリンク
        bpy.context.collection.objects.link(new_obj)
        # 新しいオブジェクトを回転して配置
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

copy_on_circle()