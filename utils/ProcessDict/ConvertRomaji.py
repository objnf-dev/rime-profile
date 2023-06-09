import pykakasi

kakasi = pykakasi.kakasi()
kakasi.setMode("H", "a")
kakasi.setMode("s", True)

conv = kakasi.getConverter()

with open("proc_uniq.txt", "r", encoding="utf-8") as f_in:
    with open("proc_final.txt", "w", encoding="utf-8") as f_out:
        for line_num, line_content in enumerate(f_in):
            line_content = line_content.strip().split("\t")
            romaji = conv.do(line_content[0])
            result = line_content[1] + "\t" + romaji + "\n"
            f_out.write(result)
