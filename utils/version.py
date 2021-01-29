import operator  # 首先要导入运算符模块
'''
operator.gt(1,2)      #意思是greater than（大于）
operator.ge(1,2)      #意思是greater and equal（大于等于）
operator.eq(1,2)      #意思是equal（等于）
operator.ne(1,2)      #意思是（不等于）
operator.le(1,2)      #意思是less and equal（小于等于）
operator.lt(1,2)      #意思是less than（小于）
'''


def versionCompare(version1, version2, split_flag="."):
    v1Arr = version1.split(split_flag)
    v2Arr = version2.split(split_flag)
    i = 0
    diff = 0
    diff = len(v1Arr) - len(v2Arr)
    while diff == 0 and i < len(v1Arr):
        # if operator.gt(1,2)
        if operator.gt(int(v1Arr[i]), int(v2Arr[i])):
            print('第一个版本号要比第二个版本号大')
            return 1
        elif operator.lt(int(v1Arr[i]), int(v2Arr[i])):
            print('第二个版本号要比第一个版本号大')
            return -1
        else:
            diff = 0
            # diff = cmp(int(v1Arr[i]), int(v2Arr[i]))
        i += 1
    print('两个版本号一样')
    return 0


# version1----第一个要比较的版本字符串
# version2----第二个要比较的版本字符串
# split_flag----版本分隔符，默认为"."，可自定义
# 返回值----相等返回0，version1比version2大返回1，version2比version1大返回2
# 接受的版本字符形式----空/x/x.y/x.y./x.y.z；两个参数可为前边列出的形式的任一种
def compare_version(version1=None, version2=None, split_flag="."):
    # 如果存在有为空的情况则进入
    if (version1 is None) or (version1 == "") or (version2 is None) or (version2 == ""):
        # version1为空且version2不为空，则返回version2大
        if ((version1 is None) or (version1 == "")) and (version2 is not None) and (version2 != ""):
            return 2
        # version2为空且version1不为空，则返回version1大
        if ((version2 is None) or (version2 == "")) and (version1 is not None) and (version1 != ""):
            return 1

    # 如果版本字符串相等，那么直接返回相等，这句会且只会在第一次比较时才可能进入
    # version1和version2都为空时也会进入这里
    if version1 == version2:
        return 0

    # 对版本字符串从左向右查找"."，第一个"."之前的字符串即为此次要比较的版本
    # 如1.3.5中的1
    try:
        current_section_version1 = version1[:version1.index(split_flag)]
    except:
        current_section_version1 = version1
    try:
        current_section_version2 = version2[:version2.index(split_flag)]
    except:
        current_section_version2 = version2
    # 对本次要比较的版本字符转成整型进行比较
    if int(current_section_version1) > int(current_section_version2):
        return 1
    elif int(current_section_version1) < int(current_section_version2):
        return 2

    # 如果本次传来版本字符串中已没有版本号分隔符，那说明本次比较的版本号已是最后一位版本号，下次比较值赋空
    # 如本次传来的是5，那下次要比较的只能赋空
    try:
        other_section_version1 = version1[version1.index(split_flag)+1:]
    except:
        other_section_version1 = ""
    try:
        other_section_version2 = version2[version2.index(split_flag) + 1:]
    except:
        other_section_version2 = ""

    # 递归调用比较
    return compare_version(other_section_version1, other_section_version2)

# 此函数调用compare_version()，打印比较结果


def pick_up_latest_version(version1, version2):
    flag = compare_version(version1, version2)
    if flag == 0:
        print(
            f"version1 = {version1}, version2 = {version2}, the two version is equal")
    elif flag == 1:
        print(
            f"version1 = {version1}, version2 = {version2}, the latest version is version1 {version1}")
    elif flag == 2:
        print(
            f"version1 = {version1}, version2 = {version2}, the latest version is version2 {version2}")


if __name__ == '__main__':
    print(versionCompare('0.4.6.1', '0.4.6'))
    pick_up_latest_version('0.4.11.1', '0.4.6')
