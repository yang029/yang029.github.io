import os
import sys

def rename_files_in_folder(folder_path):
    # 检查路径是否存在
    if not os.path.isdir(folder_path):
        print(f"错误: {folder_path} 不是一个有效的文件夹路径")
        return

    # 获取文件夹内所有文件（不包含子文件夹）
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # 按文件名排序（可选）
    files.sort()

    # 重命名文件
    for idx, filename in enumerate(files, start=1):
        # 拆分文件名和扩展名
        name, ext = os.path.splitext(filename)
        new_name = f"{idx}{ext}"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)

        # 如果新文件名已存在，加上前缀避免覆盖
        if os.path.exists(new_path):
            new_path = os.path.join(folder_path, f"{idx}_new{ext}")

        os.rename(old_path, new_path)
        print(f"{filename} → {os.path.basename(new_path)}")

    print("重命名完成！")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python rename_files.py <文件夹路径>")
    else:
        folder_path = sys.argv[1]
        rename_files_in_folder(folder_path)
