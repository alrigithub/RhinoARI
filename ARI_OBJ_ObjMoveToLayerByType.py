import rhinoscriptsyntax as rs

def main():
    # Define the layer names and fun colors for each type
    layers = {
        "Surface": ("Surfaces", (127, 255, 212)),  # Aquamarine
        "Curve": ("Curves", (46, 139, 87)),  # Sea Green
        "Closed PolySurface": ("ClosedPolySurfaces", (223, 255, 0)),  # Chartreuse
        "Open PolySurface": ("OpenPolySurfaces", (255, 215, 0))  # Gold
    }
    
    # Ensure layers exist, create them if they don't, and set colors
    for layer, (layer_name, color) in layers.items():
        if not rs.IsLayer(layer_name):
            rs.AddLayer(layer_name, color)
        else:
            rs.LayerColor(layer_name, color)
    
    # Get selected objects
    selected_objects = rs.GetObjects("Select objects to move to specific layers", preselect=True)
    if not selected_objects:
        print("No objects selected.")
        return

    # Move objects to the appropriate layer based on type
    for obj in selected_objects:
        if rs.IsSurface(obj):
            rs.ObjectLayer(obj, layers["Surface"][0])
        elif rs.IsCurve(obj):
            rs.ObjectLayer(obj, layers["Curve"][0])
        elif rs.IsPolysurface(obj):
            if rs.IsObjectSolid(obj):
                rs.ObjectLayer(obj, layers["Closed PolySurface"][0])
            else:
                rs.ObjectLayer(obj, layers["Open PolySurface"][0])

    print("Objects moved to respective layers.")

if __name__ == "__main__":
    main()
