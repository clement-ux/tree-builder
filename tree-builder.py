file_name = "file.txt" # change file name here
dest_name = file_name[:-4] + ".tree"

with open(dest_name, 'w') as dest:
    # Open the file in 'read' mode
    with open(file_name, 'r') as file:
        # Initialize line count
        line_count = 0

        tab_counter = []
        line_memory = []
        # Read each line
        for line in file:
            # Increment line count
            tab_counter.append(line.count('    '))
            line_memory.append(line.replace('    ', ''))

        for i in range(len(tab_counter)):

            # First line is the header
            if (tab_counter[i] == 0) :
                dest.write(line_memory[i])
                continue

            # Handle last line
            if (i == len(tab_counter)-1) :
                dest.write((tab_counter[i] - 1) * ('    ') + ('└── ') + (line_memory[i]))
                continue

            # Need to be indent
            elif (tab_counter[i] >= 1) :
                if ((tab_counter[i] >= min(tab_counter[i+1:])) and (tab_counter[i] <= tab_counter[i+1])) :
                    if (tab_counter[i] >= 2) : 
                        dest.write((min(tab_counter[i:]) - 1) * ('    ') + min(tab_counter[i] - 1,(tab_counter[i] - min(tab_counter[i:])))*('│   ') + ('├── ') + (line_memory[i]))
                    else :
                        dest.write((min(tab_counter[i:]) - 1) * ('    ') + ('├── ') + (line_memory[i]))
                else :
                    if (tab_counter[i] >= 2) : 
                        dest.write((min(tab_counter[i:]) - 1) * ('    ') + min(tab_counter[i] -1,(tab_counter[i] - min(tab_counter[i:])))*('│   ') + ('└── ') + (line_memory[i]))
                    else :
                        dest.write((tab_counter[i] - 1) * ('    ') + ('└── ') + (line_memory[i]))
