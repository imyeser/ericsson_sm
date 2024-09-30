source_lines = []
with open('source.txt', 'r') as source_file:
    source_lines = source_file.readlines()

start_line_index = -1
end_line_index = -1
filtered_group_lines = []
filtered_rule_lines = []
filtered_qos_lines = []
filtered_redirect_lines = []
filtered_urr_lines = []

for i, line in enumerate(source_lines):
    if 'pcc-rule-group' in line:
        start_line_index = i
    if '!' in line and start_line_index != -1:
        end_line_index = i
        filtered_group_lines.extend(source_lines[start_line_index:end_line_index+1])
        start_line_index = -1

for j, line in enumerate(source_lines):
    if 'pcc-rule' in line and '[' not in line and ']' not in line and 'group' not in line:
        start_line_index = j
    if '!' in line and start_line_index != -1:
        end_line_index = j
        filtered_rule_lines.extend(source_lines[start_line_index:end_line_index+1])
        start_line_index = -1

for k, line in enumerate(source_lines):
    if 'qos-control service-profile' in line:
        start_line_index = k
    if '!' in line and start_line_index != -1:
       end_line_index = k
       filtered_qos_lines.extend(source_lines[start_line_index:end_line_index+1])
       start_line_index = -1

for l, line in enumerate(source_lines):
    if 'packet-enforcement traffic-redirection rule' in line:
        start_line_index = l
    if '!' in line and start_line_index != -1:
       end_line_index = l
       filtered_redirect_lines.extend(source_lines[start_line_index:end_line_index+1])
       start_line_index = -1

for m, line in enumerate(source_lines):
    if 'epg pgw user-plane predefined-rule profile' in line:
        start_line_index = m
    if '!' in line and start_line_index != -1:
        end_line_index = l
        filtered_urr_lines.extend(source_lines[start_line_index:end_line_index+1])
        start_line_index = -1


with open('src_group.txt', 'w') as output_file:
    for line in filtered_group_lines:
        output_file.write(line)

with open('src_rule.txt', 'w') as output_file:
    for line in filtered_rule_lines:
        output_file.write(line)

with open('src_qos.txt', 'w') as output_file:
    for line in filtered_qos_lines:
        output_file.write(line)

with open('src_redirect.txt', 'w') as output_file:
    for line in filtered_redirect_lines:
        output_file.write(line)

with open('src_urr.txt', 'w') as output_file:
    for line in filtered_urr_lines:
        output_file.write(line)
