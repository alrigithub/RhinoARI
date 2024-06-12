import rhinoscriptsyntax as rs

def select_blocks_with_same_name():
    # Prompt the user to select blocks
    selected_objects = rs.GetObjects("Select one or more blocks", rs.filter.instance)
    if not selected_objects:
        print("No blocks selected.")
        return
    
    # Get the names of the selected blocks
    block_names = set()
    for obj in selected_objects:
        if rs.IsBlockInstance(obj):
            block_name = rs.BlockInstanceName(obj)
            if block_name:
                block_names.add(block_name)
    
    if not block_names:
        print("No valid block names found in the selection.")
        return
    
    # Find all blocks with the same names and select them
    all_objects = rs.AllObjects()
    blocks_to_select = []
    
    for obj in all_objects:
        if rs.IsBlockInstance(obj) and rs.BlockInstanceName(obj) in block_names:
            blocks_to_select.append(obj)
    
    if blocks_to_select:
        rs.SelectObjects(blocks_to_select)
        print("Selected {} blocks with the same names.".format(len(blocks_to_select)))
    else:
        print("No matching blocks found.")

if __name__ == "__main__":
    select_blocks_with_same_name()
