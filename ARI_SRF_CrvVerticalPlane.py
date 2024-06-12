import rhinoscriptsyntax as rs
import scriptcontext
import Rhino

def copy_curve_and_create_loft_on_specific_layer():
    # Select a curve
    curve_id = rs.GetObject("Select a curve", rs.filter.curve)
    if not curve_id:
        print("No curve selected.")
        return

    # Check if the curve is planar
    if not rs.IsCurvePlanar(curve_id):
        print("The curve is not planar.")
        return

    # Get the curve color
    curve_color = rs.ObjectColor(curve_id)

    # Copy the curve 120,000 mm upwards
    translation_vector = Rhino.Geometry.Vector3d(0, 0, 120000)
    copied_curve_id = rs.CopyObject(curve_id, translation_vector)

    # Create a loft surface between the original curve and its copy
    loft_surface_ids = rs.AddLoftSrf([curve_id, copied_curve_id])

    if loft_surface_ids:
        loft_surface_id = loft_surface_ids[0]
        # Assign the loft surface the same color as the original curve
        rs.ObjectColor(loft_surface_id, curve_color)

        # Ensure the target layer exists or create it
        target_layer = "3D_Guide::3D_Guide-Srf-Wall"
        if not rs.IsLayer(target_layer):
            rs.AddLayer(target_layer)
        
        # Move the loft surface to the target layer
        rs.ObjectLayer(loft_surface_id, target_layer)

    # Delete the temporary offset curve
    rs.DeleteObject(copied_curve_id)

if __name__ == "__main__":
    copy_curve_and_create_loft_on_specific_layer()
