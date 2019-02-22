'''
@author:Administrator
@file:Main.py
@note:

'''
from CommonTool.Gen_py_class_files.Config import Config_OBJ
from CommonTool.Gen_py_class_files.Generate_model_class import Generater

if __name__ == '__main__':
    attributionList = ['name', 'deviceid']
    filename = 'Netcard_test.py'
    class_name = 'Netcard_OBJ'
    generated_file_path = '../../HardwareModel/'
    config_obj = Config_OBJ()
    config_obj.attributionList = attributionList
    config_obj.generated_file_path = generated_file_path
    config_obj.file_name = filename
    config_obj.class_name = class_name
    Generater.start_gen(config_obj)
