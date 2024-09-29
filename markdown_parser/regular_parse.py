import re

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 正则表达式匹配Markdown标题
    title_regex = r'^(#+)\s*(.*)'
    # 存储标题和对应内容
    content_dict = {}
    current_title = None
    current_level = 0

    for line in lines:
        match = re.match(title_regex, line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            if current_title is None or level <= current_level:
                current_title = title
                current_level = level
                content_dict[current_title] = []
            else:
                content_dict[current_title].append(line)
        elif current_title:
            content_dict[current_title].append(line)

    # 将内容列表转换为字符串
    for title, content in content_dict.items():
        content_dict[title] = ''.join(content).strip()

    return content_dict


def parse_markdown_2(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # 正则表达式匹配Markdown标题
    title_regex = r'^(#+)\s*(.*)'
    # 存储标题和对应内容
    content_dict = {}
    current_title = "None"
    current_title_list = []

    for idx, line in enumerate(lines):
        match = re.match(title_regex, line)
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            if level == 1:
                current_title_list = []
                current_title_list.append(title)
                current_title = title
                content_dict[current_title] = []
            else:
                current_title_list = current_title_list[:level]
                current_title_list.append(title)
                current_title = '-->'.join(current_title_list)
                content_dict[current_title] = []

        else:
            if idx == 0:
                content_dict[current_title] = [line]
            else:
                content_dict[current_title].append(line)

    # # 将内容列表转换为字符串
    # for title, content in content_dict.items():
    #     content_dict[title] = ''.join(content).strip()
    #
    return content_dict

# 使用函数
markdown_path = r'D:\data\code\llm_test\20240820_AI_development\markdown_parser\markdown_files\Ovis.md'
result = parse_markdown_2(markdown_path)
for title, content in result.items():
    print(f"Title: {title}")
    print("Content:")
    print(content)
    print("|----------------------------------------------------")
