from pypinyin import slug
import opencc
import re

convs2t = opencc.OpenCC("s2t.json")

with open("proc.txt", "r", encoding="utf-8") as f_in:
    with open("proc_out.txt", "w", encoding="utf-8") as f_out:
        for line_num, line_content in enumerate(f_in):
            line_content = re.search("[\t][\u4e00-\u9fa5].*[\t]", line_content, re.U).group().strip()
            result = line_content + "\t" + slug(line_content, separator=" ", heteronym=False).strip() + "\n"
            result = convs2t.convert(result)
            f_out.write(result)
