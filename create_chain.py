import bpy
import math

# 鎖状のオブジェクトを作成
def create_chain(offset, count, rot=90):
    active_obj = bpy.context.active_object

    if active_obj is None or active_obj.type != 'MESH':
        print("アクティブなメッシュオブジェクトがありません。")
        return
    
    # 新しいコレクションを作成
    chain_collection = bpy.data.collections.new("Chain")
    bpy.context.scene.collection.children.link(chain_collection)
    # アクティブなオブジェクトをコピー
    for i in range(count):
        new_obj = active_obj.copy()
        new_obj.data = active_obj.data.copy()
        chain_collection.objects.link(new_obj)

    # アクティブなオブジェクトを削除する
    bpy.data.objects.remove(active_obj, do_unlink=True)

    # 親子関係を設定    
    for i in range(len(chain_collection.objects) - 1):
        c1 = chain_collection.objects[i]
        c2 = chain_collection.objects[i + 1]

        c2.parent = c1
        c2.location = (offset, 0, 0)
        # 回転を設定
        c2.rotation_euler = (math.radians(rot), 0, 0)

create_chain(1.5, 15)