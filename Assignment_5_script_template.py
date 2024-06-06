# A script to classify and count 'active' and 'inactive'
# gridblocks in a discretized reservoir

#################### Task 1 ############################
# Request for reservoir dimensions and discretization parameters

# Lx: Length in x-direction (not used in this script)
Lx = float(input('Enter the length of the reservoir in the x-direction (Lx): '))

# Ly: Length in y-direction (not used in this script)
Ly = float(input('Enter the length of the reservoir in the y-direction (Ly): '))

# Lz: Length in z-direction (not used in this script)
Lz = float(input('Enter the length of the reservoir in the z-direction (Lz): '))

# nx: Number of columns in the discretized reservoir
nx = int(input('Enter the number of columns (nx): '))

# ny: Number of rows in the discretized reservoir
ny = int(input('Enter the number of rows (ny): '))

# nz: Number of layers in the discretized reservoir
nz = int(input('Enter the number of layers (nz): '))

#################### Task 2 ############################
# Request for the cut-off value
cut_off = float(input('Enter the permeability cut-off value: '))

#################### Task 3 ############################
# Initialize counters

# n_active: Counter for active gridblocks
n_active = 0

# n_inactive: Counter for inactive gridblocks
n_inactive = 0

#################### Task 4 ############################
# Loop through all blocks (nested loop)
for k in range(1, nz + 1):
    # Initialize layer counter
    n_active_layer = 0

    for j in range(1, ny + 1):
        for i in range(1, nx + 1):
            # Request for the permeability value
            perm = float(input(f'Enter the permeability value for block ({i}, {j}, {k}): '))

            # Classify the gridblock
            if perm >= cut_off:
                n_active += 1
                n_active_layer += 1
            else:
                n_inactive += 1

    # Print layer count
    print(f'Number of active gridblocks in layer {k}: {n_active_layer}')

#################### Task 5 ############################
# Print overall counts

# Print 'active'
print(f'Total number of active gridblocks: {n_active}')

# Print 'inactive'
print(f'Total number of inactive gridblocks: {n_inactive}')

# Print the percentage of active gridblocks
total_blocks = nx * ny * nz
percentage_active = (n_active / total_blocks) * 100
print(f'Percentage of active gridblocks: {percentage_active:.2f}%')
