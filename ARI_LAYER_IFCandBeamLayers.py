import rhinoscriptsyntax as rs
import Rhino

def create_layers_with_subcategories_and_distinct_colors():
    parent_layer = "BEAM"
    categories = [
        "Ceilings", "Columns", "Doors", "Floors", "Furniture", "Railings", "Roofs",
        "Mullions", "Windows", "Walls", "Stairs", "Curtain Panels", "Generic Model",
        "Entourage", "Lighting Features", "Mass", "Structural Framing"
    ]
    
    subcategories = ["Subcategory1", "Subcategory2", "Subcategory3"]
    
    # Define distinct colors for parent layers
    distinct_colors = [
        (255, 0, 0),      # Red
        (0, 255, 0),      # Green
        (0, 0, 255),      # Blue
        (255, 255, 0),    # Yellow
        (255, 165, 0),    # Orange
        (128, 0, 128),    # Purple
        (0, 255, 255),    # Cyan
        (255, 192, 203),  # Pink
        (0, 128, 0),      # Dark Green
        (128, 0, 0),      # Maroon
        (0, 128, 128),    # Teal
        (128, 128, 0),    # Olive
        (75, 0, 130),     # Indigo
        (255, 20, 147),   # Deep Pink
        (139, 69, 19),    # Brown
        (255, 215, 0),    # Gold
        (173, 216, 230)   # Light Blue
    ]
    
    options = ('Create Subcategories', 'Do Not Create Subcategories')
    result = rs.ListBox(options, "Choose the subcategory creation option")
    if result is None:
        return  # User cancelled the operation
    
    create_subcategories = (result == 'Create Subcategories')
    
    rs.AddLayer(parent_layer)
    
    for index, category in enumerate(categories):
        # Choose a distinct color for the parent layer
        parent_color = distinct_colors[index % len(distinct_colors)]
        
        # Create parent layer for the category
        parent_category_layer = "{}::{}".format(parent_layer, category)
        if not rs.IsLayer(parent_category_layer):
            rs.AddLayer(parent_category_layer, parent_color)
        
        if create_subcategories:
            # Create subcategory layers with different tones of the parent color
            for sub_index, subcategory in enumerate(subcategories):
                # Modify color tone for subcategories
                tone_factor = 1 - (sub_index + 1) * 0.2
                sub_color = tuple(min(255, max(0, int(c * tone_factor))) for c in parent_color)
                
                subcategory_layer = "{}::{}::{}".format(parent_layer, category, subcategory)
                if not rs.IsLayer(subcategory_layer):
                    rs.AddLayer(subcategory_layer, sub_color)
    
    print("Layers created successfully with distinct colors.")

if __name__ == "__main__":
    create_layers_with_subcategories_and_distinct_colors()
