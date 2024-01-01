import sys
import cutlet

katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = False
f_out = open(sys.argv[1] + '_conv.yaml', 'w', encoding='utf-8')
f_in = open(sys.argv[1], 'r', encoding='utf-8')

while True:
    line = f_in.readline()
    if not line:
        break
    line = line.split('|')
    romaji = katsu.romaji(line[1], capitalize=False)
    romaji = romaji.replace(" ", "")
    f_out.write(line[0] + '\t' + romaji + '\n')

f_in.close()
f_out.close()
