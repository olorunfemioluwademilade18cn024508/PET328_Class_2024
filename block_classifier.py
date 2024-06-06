#TTOWG

# Define the function classify_block
def classify_block(i, j, nx, ny):
    """
    Classify gridblocks in a discretized oil reservoir based on the position
    of the gridblock relative to the reservoir boundaries.

    Parameters:
    i (int): Column index of the gridblock
    j (int): Row index of the gridblock
    nx (int): Total number of columns in the discretized reservoir
    ny (int): Total number of rows in the discretized reservoir

    Returns:
    str: Block category
    """
    if (i == 1 and j == 1) or (i == 1 and j == ny) or (i == nx and j == 1) or (i == nx and j == ny):
        block_cat = 'IV'
    elif j == 1 or j == ny:
        block_cat = 'II'
    elif i == 1 or i == nx:
        block_cat = 'III'
    else:
        block_cat = 'I'
    
    return block_cat
