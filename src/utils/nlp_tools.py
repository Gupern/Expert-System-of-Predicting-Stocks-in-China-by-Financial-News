#encoding: utf-8


def strip_title(title):
    """
    去除掉标题中不合适的首尾，如空格，\t，:等字符
    :param title:
    :return:
    """
    title = title.strip()
    while title.endswith(":"):
        title = title[:-1]
    while title.endswith("："):
        title = title[:-1]
    return title