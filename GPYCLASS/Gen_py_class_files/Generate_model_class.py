# coding=utf-8

'''
    @author:pope
    @file:Generate_model_class.py
    @note:用于生成基础新类的python脚本
'''


class Generater(object):
    @staticmethod
    def start_gen(config_obj):
        changeline = '\n'
        if config_obj:
            with open(config_obj.generated_file_path + config_obj.file_name, 'w') as openedfile:
                openedfile.write('# -*- coding=utf-8 -*-' + '\n')
                openedfile.write(
                    '\'\'\'' + changeline + 'this is a auto generated file please check it before using!' + changeline + '\'\'\'' + changeline)
                openedfile.write(changeline)
                openedfile.write(changeline)
                openedfile.write('class ' + config_obj.class_name + '(object):' + changeline)

                openedfile.write('    def __init__(self):' + changeline)
                for attri in config_obj.attributionList:
                    openedfile.write('        self._' + attri + ' = None' + changeline)
                openedfile.write(changeline)
                for attri in config_obj.attributionList:
                    openedfile.write('    @property' + changeline)
                    openedfile.write('    def ' + attri + '(self):' + changeline)
                    openedfile.write('        return self._' + attri + changeline)
                    openedfile.write(changeline)

                for attri in config_obj.attributionList:
                    openedfile.write('    @' + attri + '.setter' + changeline)
                    openedfile.write('    def ' + attri + '(self, ' + attri + '):' + changeline)
                    openedfile.write('        self._' + attri + ' = ' + attri + changeline)
                    openedfile.write(changeline)
                    openedfile.write('    @' + attri + '.getter' + changeline)
                    openedfile.write('    def ' + attri + '(self):' + changeline)
                    openedfile.write('        return self._' + attri + changeline)
                    openedfile.write(changeline)

        else:
            print('')
            print('config obj 为空')
            return 0
