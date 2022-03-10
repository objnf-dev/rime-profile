import pykakasi

kakasi = pykakasi.kakasi()
kakasi.setMode("H", "a")
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')

conv = kakasi.getConverter()

with open("basic.txt", "w", encoding="utf-8") as f:
    for i in range(12353, 12543):
            line_content = chr(i)
            line_content = line_content + "\t" + conv.do(line_content)
            f.write(line_content + "\n")