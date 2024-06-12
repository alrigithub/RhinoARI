import rhinoscriptsyntax as rs

def split_and_cap():
    # Select the object to split
    object_to_split_id = rs.GetObject("Select the object to split", 0, preselect=True)
    if not object_to_split_id:
        print("No object selected to split.")
        return
    
    # Select the cutting object
    cutting_object_id = rs.GetObject("Select the cutting object")
    if not cutting_object_id:
        print("No cutting object selected.")
        return
    
    # Perform the split operation
    split_results = rs.SplitBrep(object_to_split_id, cutting_object_id, delete_input=False)
    if not split_results:
        print("Split operation failed or resulted in no changes.")
        return

    # If split was successful, delete the original object
    rs.DeleteObject(object_to_split_id)

    # Attempt to cap the resulting objects
    for result_id in split_results:
        # Check if the object is not solid, implying it might be an open polysurface
        if rs.IsObjectSolid(result_id) == False:
            capped_id = rs.CapPlanarHoles(result_id)
            if capped_id:
                print("Capped an open polysurface.")
            else:
                print("Failed to cap an open polysurface or no planar holes found.")

if __name__ == "__main__":
    split_and_cap()
