#---------------------------------------------


def recenter_cloud(cloud):
    centroid = compute_centroid(cloud)
    cloud = compute_centering(cloud, centroid)
    print("[\033[1;32mok\033[0m] Cloud recentered by \033[1;32m%s\033[0m"% str(centroid))

def compute_centroid(cloud):
    x = 0
    y = 0
    z = 0
    for point in cloud["xyz"]:
        x = x + point[0]
        y = y + point[1]
        z = z + point[2]
    x = x / len(cloud["xyz"])
    y = y / len(cloud["xyz"])
    z = z / len(cloud["xyz"])
    centroid = (x, y, z)
    return centroid

def compute_centering(cloud, centroid):
    for point in cloud["xyz"]:
        point[0] = point[0] - centroid[0]
        point[1] = point[1] - centroid[1]
        point[2] = point[2] - centroid[2]
    return cloud
