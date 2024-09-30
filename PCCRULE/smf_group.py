import openpyxl

# 파일 경로 설정
output_file = 'ELG_GW-C_PCC.xlsx'
src_group_file = 'src_group.txt'

# output2.xlsx 파일 열기
workbook = openpyxl.load_workbook(output_file)
sheet = workbook['PCC']

# src_group.txt 파일 읽기
with open(src_group_file, 'r') as file:
    src_group_lines = file.readlines()

# 필요한 변수 초기화
group_data = {}
current_group = {}
pcc_rule_group = ""
description = ""
rules = []

# src_group.txt 파일에서 데이터를 추출해 group_data에 저장
for line in src_group_lines:
    line = line.strip()

    if line.startswith("pcc-rule-group"):
        pcc_rule_group = line.split("pcc-rule-group", 1)[1].strip()

    elif line.startswith("description"):
        description = line.split("description", 1)[1].strip()

    elif line.startswith("pcc-rule"):
        rules = line.split("[", 1)[1].split("]", 1)[0].split()

    elif line.startswith("!"):
        # group_data에 각 rule을 키로 하고, pcc_rule_group과 description을 값으로 저장
        for rule in rules:
            group_data[rule] = {
                "pcc_rule_group": pcc_rule_group,
                "description": description
            }
        # 다음 세트를 위해 변수 초기화
        pcc_rule_group = ""
        description = ""
        rules = []

# output2.xlsx 파일의 C컬럼을 읽어 src_group.txt에서 정보를 찾아 A, B컬럼에 입력
for row in range(2, sheet.max_row + 1):
    pcc_rule_value = sheet[f'C{row}'].value

    if pcc_rule_value in group_data:
        sheet[f'A{row}'] = group_data[pcc_rule_value]["pcc_rule_group"]  # pcc-rule-group 정보
        sheet[f'B{row}'] = group_data[pcc_rule_value]["description"]    # description 정보

# 엑셀 파일 저장
workbook.save(output_file)

