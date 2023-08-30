import sys
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(script_directory, "input.text")

sys.stdin = open(input_file_path, "r")

n = int(sys.stdin.readline())
name = []

for i in range(n):
  name.append(sys.stdin.readline())

current_name = str(name[0])
current_type = []

for i in range(len(current_name)):
   current_type.append(False)

for i in range(len(name)):
    for j in range(len(current_name)-1):
       if current_name[j] != name[i][j]:
          current_type[j] = True

for i in range(len(current_type)):
    if current_type[i] == True:
       current_name = current_name[:i] + "?" + current_name[i+1:]

print(current_name)