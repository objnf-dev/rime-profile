# sort -n origin.txt

# uniq
with open("merged.txt", "r", encoding="utf-8") as f_in:
    with open("uniq.txt", "w", encoding="utf-8") as f_out:
        line_current = ""
        for line_num, line_content in enumerate(f_in):
            if line_content.strip() != line_current:
                line_current = line_content.strip()
                f_out.write(line_content)
            else:
                continue

# sort again
with open("uniq.txt", "r", encoding="utf-8") as f_in:
    with open("final.txt", "w", encoding="utf-8") as f_out:
        lines = f_in.readlines()
        lines.sort(key=lambda x: len(x.strip().split("\t")[0]))
        for i in lines:
            f_out.write(i)