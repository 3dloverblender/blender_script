import bpy
import bmesh
import math

# すべてのメッシュオブジェクトを削除する
def delete_mesh_objects():
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            bpy.data.objects.remove(obj)

#　円のポリゴンを作成する関数　 
def create_spring_polygon():
    # メッシュを作成する
    new_mesh = bpy.data.meshes.new("Spring")
    # オブジェクトを作成する
    new_obj = bpy.data.objects.new("Spring", new_mesh)
    # 現在のシーンにオブジェクトをリンクさせる
    bpy.context.scene.collection.objects.link(new_obj)
    # 作成したオブジェクトをアクティブオブジェクトにする
    bpy.context.view_layer.objects.active = new_obj
    # 作成したオブジェクトを選択状態にする
    new_obj.select_set(True)

    # BMeshを作成する
    bm = bmesh.new()
    verts = []
    # 半径
    r = 1.0
    # 角度
    deg = 10
    # 初期z座標
    z = 0.0
    # z座標の増加量
    dz = 0.01
    # 巻く回数
    times = 10
    # バネの頂点を作成する
    for deg in range(0, 360 * times, deg):
        # 角度をラジアンに変換
        rad = math.radians(deg)
        # x, y座標を計算
        x = r * math.cos(rad)
        y = r * math.sin(rad)
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

delete_mesh_objects()

create_spring_polygon()