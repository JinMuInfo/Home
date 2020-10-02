# coding: utf-8
import os
import sys


def format_file(filename, str1, str2):
    """
    文件内容的替换功能
    :return:
    """
    with open(filename, 'r') as f:
        var_object = f.read()
        if "gitalk" not in var_object:
            var_object = var_object.replace(str1, str2)
        # print(var_object)

    f = open(filename, "w")
    f.write(var_object)


if __name__ == "__main__":
    version, u_type = sys.argv[1], sys.argv[2]

    tag = True
    if u_type == "index":
        tag = False

    elif u_type == "book":
        if version == "home":
            filename = "book.json"
            tag = False
                          
    elif u_type == "powered":
        if version == "home":
            filename = "node_modules/gitbook-plugin-tbfed-pagefooter/index.js"
        else:
            filename = "docs/%s/node_modules/gitbook-plugin-tbfed-pagefooter/index.js" % version
        str1 = "powered by Gitbook"
        str2 = "由 MongoDB汉化小组 提供技术支持"

    
    # 状态为 True 就进行替换
    if tag: format_file(filename, str1, str2)
