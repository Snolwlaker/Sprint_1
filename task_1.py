time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0

time_blocks = time_string.split(',')

for block in time_blocks:

    if 'h' in block:
        parts = block.replace('h', '').split()
        for part in parts:
            if part.isdigit():
                total_minutes += int(part) * 60
                break

    if 'm' in block:
        parts = block.replace('m', '').split()
        for part in parts:
            if part.isdigit():
                total_minutes += int(part)
                break

    if 's' in block:
        parts = block.replace('s', '').split()
        for part in parts:
            if part.isdigit():
                total_minutes += int(part) // 60
                break

print(total_minutes)
