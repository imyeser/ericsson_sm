import openpyxl

# 파일 경로 및 워크북 로드
output_file = 'ELG_GW-U_PCC.xlsx'
src_app_file = 'src_app.txt'

workbook = openpyxl.load_workbook(output_file)
sheet = workbook['APPLICATION']

# 기존 데이터 삭제
sheet.delete_rows(2, sheet.max_row)

# 텍스트 파일 읽기
with open(src_app_file, 'r') as file:
    lines = file.readlines()

# 변수 초기화
app_data_list = []
app = enabled = port = proto = rtx = dupl = syn_flood = dft = tcp_setup = tcp_down = fil = ""
filter = []
addrs = []

# 텍스트 파일 처리
for line in lines:
    if 'applications' in line:
        app = line.split()[-1]
    elif 'enabled' in line:
        enabled = line.split()[-1]
    elif 'ip-flow-network-port' in line:
#        port = line.split()[-1]
        port =line[line.index('[')+1:line.index(']')]
    elif 'ip-flow-protocol' in line:
#        proto = line.split()[-1]
        proto = line[line.index('[')+1:line.index(']')]
    elif 'tcp-retransmission' in line:
        rtx = line.split()[-1]
    elif 'tcp-duplicated-ack' in line:
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
#    elif '!' in line:
    elif line.strip() == '':
        # addrs와 filter가 모두 없는 경우도 포함하여 처리
        if not addrs and not filter:
            print(app, enabled, port, proto, rtx, dupl, syn_flood, dft, tcp_setup, tcp_down, "", "")
            sheet.append([app, enabled, port, proto, rtx, dupl, syn_flood, dft, tcp_setup, tcp_down, "", ""])
        else:
            if addrs:
                for addr in addrs:
                    print(app, enabled, port, proto, rtx, dupl, syn_flood, dft, tcp_setup, tcp_down, addr, "")
                    sheet.append([app, enabled, port, proto, rtx, dupl, syn_flood, dft, tcp_setup, tcp_down, addr, ""])
            if filter:
                for fil in filter:
                    print(app, enabled, port, proto, rtx, dupl, syn_flood, dft, tcp_setup, tcp_down, "", fil)
                    sheet.append([app, enabled, port, proto, rtx, dupl, syn_flood, dft, tcp_setup, tcp_down, "", fil])
        
        # 초기화
        app = enabled = port = proto = rtx = dupl = syn_flood = dft = tcp_setup = tcp_down = ""
        filter = []
        addrs = []

# 엑셀 파일 저장
workbook.save(output_file)

