def process_file(file_path):
    flags = []
    current_flags = []
    last_was_and = False
 
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
 
            if 'new VMS("ADD", new List<string>()),' in line:
                current_flags.append("+")
                last_was_and = False
            elif 'new VMS("AND", new List<string>()),' in line:
                current_flags.append("&")
                last_was_and = True
            elif 'new VMS("SUB", new List<string>()),' in line:
                current_flags.append("-")
                last_was_and = False
            elif 'new VMS("PUSH", new List<string>' in line and last_was_and:
                next_line = next(file).strip()
                if '{' in next_line:
                    next_line = next(file).strip()
                    if 'INT' in next_line:
                        next_line = next(file).strip()
                        number = next_line.split('"')[1]
                        current_flags.append(number)
                        last_was_and = False
 
            if current_flags:
                flags.append(''.join(current_flags))
                current_flags = []
 
    return flags
 
file_path = 'C:\\Users\\junus\\Music\\modEntryPoint.cs'  
flags = process_file(file_path)
print("Flags:", flags)

i = 0
while flags:
    print(f"(((s[{i}] {flags.pop(0)} s[{i+1}]) {flags.pop(0)} 255) {flags.pop(0)} s[{i+2}]) {flags.pop(0)} 255 == {flags.pop(0)}")
    i += 1
