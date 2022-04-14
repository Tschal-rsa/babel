def upper():
    with open('command.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
        command_list = [item.split()[1] for item in data]
    command_list.append('combination')
    for cmd in command_list:
        lines = []
        with open(f'{cmd}.txt', 'r', encoding='utf-8') as f:
            data = f.readlines()
            for line in data:
                line = line.strip() + '\n'
                # Corner case: German eszett; Turkish I/i
                lines.extend([line.upper(), line])
        print(lines)
        with open(f'{cmd}.txt', 'w', encoding='utf-8') as f:
            f.writelines(lines)
        # break

if __name__ == '__main__':
    upper()