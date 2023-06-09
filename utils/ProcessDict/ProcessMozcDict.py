with open("proc.txt", "r", encoding="utf-8") as f_in:
    with open("proc_out.txt", "w", encoding="utf-8") as f_out:
        for line_num, line_content in enumerate(f_in):
            line_content = line_content.strip().split("\t")
            # Remove symbols from results
            # if line_content[1][0] < u"\u0061" or line_content[1][0] > u"\u007a" :
                # continue
            line_content = line_content[0] + "\t" + line_content[4]
            f_out.write(line_content + "\n")