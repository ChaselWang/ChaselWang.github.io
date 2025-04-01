import os

def process_file(old_path, new_path):
    with open(old_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if len(lines) < 5:
        print(f"跳过文件 {old_path}，因为它不足5行。")
        return
    
    # 处理前五行
    title = lines[0].strip().lstrip('#').strip()
    date_str = f"{lines[1].strip()} 20:19:32"
    categories = lines[2].strip().strip('[]')
    tags = [tag.strip().lstrip('#') for tag in lines[3].strip().split()]
    tags_str = ', '.join(tags)
    description = lines[4].strip()
    
    frontmatter = f"""---
title: {title}
date: {date_str}
categories: {categories}
tags: [{tags_str}]
description: {description}
---
"""
    
    remaining_content = ''.join(lines[5:])
    
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
        f.write(remaining_content)

def main():
    vault_dir = './obsidian_vault'
    new_dir = './ChaselWang.github.io/source/_posts'
    
    for root, dirs, files in os.walk(vault_dir):
        for file in files:
            if file.endswith('.md'):
                old_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, vault_dir)
                new_root = os.path.join(new_dir, relative_path)
                os.makedirs(new_root, exist_ok=True)
                new_path = os.path.join(new_root, file)
                process_file(old_path, new_path)
                print(f"处理完成：{old_path} -> {new_path}")

if __name__ == '__main__':
    main()