import openpyxl
import re

# 파일 경로 설정
output_file = 'ELG_GW-C_PCC.xlsx'
src_redirect_file = 'src_redirect.txt'

# output2.xlsx 파일 열기
workbook = openpyxl.load_workbook(output_file)
sheet = workbook['PCC']

# src_redirect.txt 파일 읽기
with open(src_redirect_file, 'r') as file:
    src_redirect_data = file.read()

# traffic-redirection rule 정보 추출하고 필요한 데이터를 저장할 딕셔너리 초기화
redirect_data = {}
pattern = r"traffic-redirection rule\s+([^\n]+)[\s\S]*?destination-nat[\s\S]*?(ipv4-address\s+([^\s]+)|ipv6-address\s+([^\s]+))[\s\S]*?!"
matches = re.findall(pattern, src_redirect_data)

# 추출된 정보를 딕셔너리에 저장
for match in matches:
    rule_name = match[0].strip()
    ipv4_address = match[2].strip() if match[2] else None
    ipv6_address = match[3].strip() if match[3] else None
    address = ipv4_address if ipv4_address else ipv6_address
    redirect_data[rule_name] = address

# output2.xlsx 파일의 L컬럼을 읽어 src_redirect.txt에서 정보를 찾아 M컬럼에 입력
for row in range(2, sheet.max_row + 1):
    rule_value = sheet[f'L{row}'].value

    if rule_value in redirect_data:
        sheet[f'M{row}'] = redirect_data[rule_value]  # ipv4-address 또는 ipv6-address 정보

# 엑셀 파일 저장
workbook.save(output_file)

