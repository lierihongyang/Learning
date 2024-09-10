# -*- coding: UTF-8 -*-
"""统计代码行数"""
import os


def get_file_lines(file) -> int:
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return len(lines)


def get_code_lines(paths: list, suffix: list) -> None:
    count = 0
    for path in paths:
        for dir_path, _, files in os.walk(path):
            for file in files:
                ends = file.split(".")[-1]
                if ends in suffix:
                    file_path = os.path.join(dir_path, file)
                    print(f"正在统计: {file_path}")
                    count += get_file_lines(file_path)
    print(f"总行数: {count}")


if __name__ == '__main__':
    paths = [r"D:\code\python\Learning", r"D:\code\python\appium_pro", r"D:\code\python\interfaceFrame"]
    suffix = ["py", "txt", "yaml", "json", "md"]
    get_code_lines(paths, suffix)
