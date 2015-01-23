#!/usr/bin/env python
#--*-- coding:utf-8 --*--

import os

class SplitFiles():
    """split file in row"""

    def __init__(self, file_name, line_count=50000):
        self.file_name = file_name
        self.line_count = line_count

    def split_file(self):
        if self.file_name and os.path.exists(self.file_name):
            try:
                with open(self.file_name) as f:
                    temp_count = 0
                    temp_content = []
                    part_num = 1
                    for line in f:
                        if temp_count < self.line_count:
                            temp_count += 1
                        else:
                            self.write_file(part_num, temp_content)
                            part_num += 1
                            temp_count = 1
                            temp_content = []
                        temp_content.append(line)
                    else:
                        self.write_file(part_num, temp_content)

            except IOError as err:
                print(err)
        else:
            print("%s is not a validate file" % self.file_name)

    def get_part_file_name(self, part_num):
        part_file_name = "split_file_" + str(part_num) + ".json"
        return part_file_name

    def write_file(self, part_num, *line_content):
        part_file_name = self.get_part_file_name(part_num)
        try :
            with open(part_file_name, "w") as part_file:
                part_file.writelines(line_content[0])
        except IOError as err:
            print(err)


if __name__ == "__main__":
    sf = SplitFiles('datademo.json')
    sf.split_file()
