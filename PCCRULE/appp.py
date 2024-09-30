import openpyxl

output_file = 'ELG_GW-U_PCC.xlsx'
src_app_file = 'src_app.txt'


workbook = openpyxl.load_workbook(output_file)
sheet = workbook['APPLICATION']
sheet.delete_rows(2, sheet.max_row)

# src_filter.txt 파일 읽기
with open(src_app_file, 'r') as file:
    lines = file.readlines()

app = enabled = port = proto = rtx = dupl = syn_flood = dft = tcp_setup = tcp_down = fil = ""
row = 2
filter = []
app_info = []
for line in lines:
    if 'applications' in line:
        app = line.split()[-1]
    elif 'enabled' in line:
        enabled = line.split()[-1]
    elif 'ip-flow-network-port' in line:
        port = line.split()[-1]
    elif 'ip-flow-protocol' in line:
        proto = line.split()[-1]
    elif 'tcp-retransmission' in line:
        rtx = line.split()[-1]
    elif 'tcpduplicated-ack' in line:
        dupl = line.split()[-1]
    elif 'syn-flood-from-ue' in line:
        syn_flood = line.split()[-1]
    elif 'default' in line:
        dft = line.split()[-1]
    elif 'tcp-signaling-setup' in line:
        tcp_setup = line.split()[-1]
    elif 'tcp-signaling-teardown' in line:
        tcp_down = line.split()[-1]
    elif 'ip-flow-network-address' in line:
        addrs = line[line.index('[')+1:line.index(']')].split()
    elif 'filter' in line:
        filter = line[line.index('[')+1:line.index(']')].split()
    elif '!' in line:    
        sheet[f'A{row}'] = app
        sheet[f'B{row}'] = enabled
        sheet[f'C{row}'] = port
        sheet[f'D{row}'] = proto
        sheet[f'E{row}'] = rtx
        sheet[f'F{row}'] = dupl
        sheet[f'G{row}'] = syn_flood
        sheet[f'H{row}'] = dft
        sheet[f'I{row}'] = tcp_setup
        sheet[f'J{row}'] = tcp_down
        for addr in addrs: 
            sheet[f'K{row}'] = addr
        addr = ""
        for fil in filter: 
            sheet[f'L{row}'] = fil
        fil = ""     
        app = enabled = port = proto = rtx = dupl = syn_flood = dft = tcp_setup = tcp_down = addr = fil = ""
        row += 1
# 변경 내용을 저장
workbook.save(output_file)
