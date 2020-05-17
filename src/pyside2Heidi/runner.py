from main_application import MainApplication
import os


if __name__ == '__main__':
    # 设置统一工作目录，Icon引入路径基于此
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    mainApplication = MainApplication()