import os
import sys
os.chdir('/home/Projects/Academic-Collaboration-RS/back-end')  # change working directory to the root of the project
sys.path.append(os.getcwd())  # add the root of the project to the path

# 后台运行 py 脚本
# nohup python -u name.py > log_name.log 2>&1 &
