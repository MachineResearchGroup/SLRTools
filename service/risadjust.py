

def ris_adjust(filename, base):
    arquivo = open(f"archives/ris/{base}_{filename}.ris", 'w', encoding="utf8")

    with open(f"archives/ris/{base}_init_{filename}.ris", 'r', encoding="utf8") as file:
        for line in file:

            if line.startswith('DO  -'):
                arquivo.write(line)
                arquivo.write('ER  -')
                arquivo.write('\n')
            else:
                arquivo.write(line)

        arquivo.close()



