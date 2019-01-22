import re

files_list = []
file_ext_list = ['.c', '.h']

try:
  with open ('Jamfile', 'rt') as in_file :
    for line in in_file :
      for file_ext in file_ext_list :
        pattern = "[^ ]*" + file_ext
        flist = re.findall(pattern, line.rstrip('\n'))
        if flist :
          files_list.extend(flist)
except IOError as e :
  errno, strerror = e.args
  print("I/O error({0}): {1}".format(errno, strerror))

print(files_list)

