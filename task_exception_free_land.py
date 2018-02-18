def get_free_land(area, bed):
    area_square = area[0] * 100
    bed_square = bed[0] * bed[1]
    area_lenth_k = int(area[1].split(":")[0])
    area_width_k = int(area[1].split(":")[1])
    k = area_square / (area_lenth_k * area_width_k)
    area_lenth = area_lenth_k * k
    area_width = area_width_k * k
    if area[0] <= 0:
        raise ValueError("Не задана площадь участка")
    elif (bed[0] <=0) or (bed[1] <= 0):
        raise ValueError("Не задана площадь грядки")
    elif (bed[0] > area_lenth) or (bed[0] > area_width) or (bed[1] > area_width) or (bed[1] > area_lenth) or (bed_square > area_square):
        raise ValueError("Размер грядки больше размера участка")
    else:
        return area_square % bed_square


# area1 = (6, "3:2")
# bed1 = (40,28)
# get_free_land(area1, bed1)
