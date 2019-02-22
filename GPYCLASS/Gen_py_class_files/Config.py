# coding=utf-8

'''
    @author:pope
    @file:Config.py
    @note:用于配置，并根据该配置文件生成基础的class文件

'''

'''
    @:param attributionList Config_OBJ 对象中的一个属性，用于保存即将生成的class文件的属性 类型：list
    @:param generated_file_path Config_OBJ 对象中的一个属性，用于保存即将生成的class文件的路径 类型： str
    @:param file_name Config_OBJ 对象中的一个属性，用于命名即将生成的py脚本的文件名 类型： str
    @:param class_name Config_OBJ 对象中的一个属性，用于命名即将生成的py脚本中的class名 类型： str
'''


class Config_OBJ(object):
    def __init__(self):
        self._attributionList = None
        self._generated_file_path = None
        self._file_name = None
        self._class_name = None
    @property
    def attributionList(self):
        return self._attributionList

    @property
    def generated_file_path(self):
        return self._generated_file_path

    @property
    def file_name(self):
        return self._file_name

    @property
    def class_name(self):
        return self._class_name

    @attributionList.setter
    def attributionList(self, attributionList):
        if isinstance(attributionList, list):
            self._attributionList = attributionList

    @attributionList.getter
    def attributionList(self):
        return self._attributionList

    @generated_file_path.setter
    def generated_file_path(self, generated_file_path):
        if isinstance(generated_file_path, str):
            self._generated_file_path = generated_file_path

    @generated_file_path.getter
    def generated_file_path(self):
        return self._generated_file_path

    @file_name.setter
    def file_name(self, file_name):
        self._file_name = file_name

    @file_name.getter
    def file_name(self):
        return self._file_name

    @class_name.setter
    def class_name(self, class_name):
        if isinstance(class_name, str):
            self._class_name = class_name

    @class_name.getter
    def class_name(self):
        return self._class_name
