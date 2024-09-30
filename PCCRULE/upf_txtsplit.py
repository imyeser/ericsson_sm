source_lines = []
with open('source_upf.txt', 'r') as source_file:
    source_lines = source_file.readlines()

start_line_index = -1
end_line_index = -1
filtered_prule_lines = []
filtered_pdr_lines = []
filtered_application_lines = []
filtered_filter_lines = []

for i, line in enumerate(source_lines):
    if 'predefined-rules' in line:
        start_line_index = i
    if '!' in line and start_line_index != -1:
        end_line_index = i
        filtered_prule_lines.extend(source_lines[start_line_index:end_line_index+1])
        start_line_index = -1

for j, line in enumerate(source_lines):
    if 'predefined-pdrs' in line and '[' not in line and ']' not in line and 'group' not in line:
        start_line_index = j
    if '!' in line and start_line_index != -1:
        end_line_index = j
        filtered_pdr_lines.extend(source_lines[start_line_index:end_line_index+1])
        start_line_index = -1

for k, line in enumerate(source_lines):
    if 'applications' in line:
        start_line_index = k
#    if '!' in line and start_line_index != -1:
    if line.strip() == '' and start_line_index != -1:
       end_line_index = k
       filtered_application_lines.extend(source_lines[start_line_index:end_line_index+1])
       start_line_index = -1

for l, line in enumerate(source_lines):
    if 'filters' in line:
        start_line_index = l
    if '!' in line and start_line_index != -1:
       end_line_index = l
       filtered_filter_lines.extend(source_lines[start_line_index:end_line_index+1])
       start_line_index = -1

for m, line in enumerate(source_lines):
    if 'epg pgw user-plane predefined-rule profile' in line:
        start_line_index = m
    if '!' in line and start_line_index != -1:
        end_line_index = l
        filtered_urr_lines.extend(source_lines[start_line_index:end_line_index+1])
        start_line_index = -1


with open('src_prule.txt', 'w') as output_file:
    for line in filtered_prule_lines:
        output_file.write(line)

with open('src_pdr.txt', 'w') as output_file:
    for line in filtered_pdr_lines:
        output_file.write(line)

with open('src_app.txt', 'w') as output_file:
    for line in filtered_application_lines:
        output_file.write(line)

with open('src_filter.txt', 'w') as output_file:
    for line in filtered_filter_lines:
        output_file.write(line)
