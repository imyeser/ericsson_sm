import openpyxl
import re

# 파일 경로 설정
output_file = 'ELG_GW-C_PCC.xlsx'
src_qos_file = 'src_qos.txt'

# output2.xlsx 파일 열기
workbook = openpyxl.load_workbook(output_file)
sheet = workbook['PCC']

# src_qos.txt 파일 읽기
with open(src_qos_file, 'r') as file:
    src_qos_data = file.read()

# service-profile 정보를 추출하고 필요한 데이터를 저장할 딕셔너리 초기화
qos_data = {}
pattern = r"service-profile\s+([^\n]+)[\s\S]*?maximum-bit-rate-uplink\s+(\d+)[\s\S]*?maximum-bit-rate-downlink\s+(\d+)[\s\S]*?!"
matches = re.findall(pattern, src_qos_data)

# 추출된 정보를 딕셔너리에 저장
for match in matches:
    service_profile = match[0].strip()
    uplink = match[1].strip()
    downlink = match[2].strip()
    qos_data[service_profile] = (uplink, downlink)

# output2.xlsx 파일의 H컬럼을 읽어 src_qos.txt에서 정보를 찾아 I, J컬럼에 입력
for row in range(2, sheet.max_row + 1):
    service_profile_value = sheet[f'H{row}'].value

    if service_profile_value in qos_data:
        sheet[f'I{row}'] = qos_data[service_profile_value][0]  # maximum-bit-rate-uplink 정보
        sheet[f'J{row}'] = qos_data[service_profile_value][1]  # maximum-bit-rate-downlink 정보

# 엑셀 파일 저장
workbook.save(output_file)

