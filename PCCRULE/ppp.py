import re

source_lines = []
with open('DATA_UPF55_config_240808.txt', 'r') as source_file:
    source_lines = source_file.readlines()

start_line_index = -1
end_line_index = -1
filtered_application_lines = []

for k, line in enumerate(source_lines):
    if 'applications' in line:
        start_line_index = k
    if '!' in line and not ' !'and start_line_index != -1:
       end_line_index = k
       filtered_application_lines.extend(source_lines[start_line_index:end_line_index+1])
       start_line_index = -1

with open('Ssrc_app.txt', 'w') as output_file:
    for line in filtered_application_lines:
        output_file.write(line)
