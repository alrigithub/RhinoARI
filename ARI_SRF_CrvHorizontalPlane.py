import rhinoscriptsyntax as rs
import scriptcontext
import Rhino

def create_large_surface_centered_on_curve():
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

    # Find the midpoint of the curve
    midpoint = rs.CurveMidPoint(curve_id)

    # Create a plane centered at the curve's midpoint, aligned with the world XY plane
    plane = Rhino.Geometry.Plane(midpoint, Rhino.Geometry.Vector3d.ZAxis)

    # Create a 100,000 by 100,000 mm surface centered on this plane
    size_half = 100000  # Half size to center the surface
    surface = Rhino.Geometry.PlaneSurface(plane, Rhino.Geometry.Interval(-size_half, size_half), Rhino.Geometry.Interval(-size_half, size_half))

    # Ensure the target layer exists or create it
    target_layer = "3D_Guide::3D_Guide-Srf-Floor"
    if not rs.IsLayer(target_layer):
        rs.AddLayer(target_layer)

    # Add the surface to the document and set its layer and color
    surface_id = scriptcontext.doc.Objects.AddSurface(surface)
    rs.ObjectLayer(surface_id, target_layer)
    rs.ObjectColor(surface_id, curve_color)

    scriptcontext.doc.Views.Redraw()

if __name__ == "__main__":
    create_large_surface_centered_on_curve()
