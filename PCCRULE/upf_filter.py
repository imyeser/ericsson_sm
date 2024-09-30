import openpyxl

# src_filter.txt 파일 읽기

output_file = 'ELG_GW-U_PCC.xlsx'
src_filter_file = 'src_filter.txt'

workbook = openpyxl.load_workbook(output_file)
sheet = workbook['FILTER']
sheet.delete_rows(2, sheet.max_row)

with open(src_filter_file, 'r') as file:
    lines = file.readlines()

filter = port = ue = addr = ""

filter_info = []
for line in lines:
    if 'filters' in line:
        filter = line.split()[-1]
    elif 'ip-flow-network-port' in line:
        port = line[line.index('[')+1:line.index(']')].replace(" ", "")
    elif 'ip-flow-ue-address' in line:
        ue = line[line.index('[')+1:line.index(']')].replace(" ", "")
    elif 'ip-flow-network-address' in line:
        addrs = line[line.index('[')+1:line.index(']')].split()
    elif '!' in line:
        for addr in addrs:
            sheet.append([filter, port, addr, ue])
        filter = port = ue = addr = ""

# 변경 내용을 저장
workbook.save(output_file)
