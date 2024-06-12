import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino

def create_layer_if_needed(layer_name, color):
    if not rs.IsLayer(layer_name):
        rs.AddLayer(layer_name, color=color)

def is_vertical(plane, tolerance=0.01):
    # A plane is considered vertical if its normal is perpendicular to the World XY plane within a tolerance
    # Tolerance is how close the dot product needs to be to 0 to consider the vectors perpendicular
    return abs(plane.Normal * Rhino.Geometry.Vector3d.ZAxis) < tolerance

def is_aligned_with_world_axes(plane, tolerance=0.01):
    # Check if the plane normal is aligned with any of the world axis directions (X, Y, or Z)
    world_axes = [Rhino.Geometry.Vector3d.XAxis, Rhino.Geometry.Vector3d.YAxis, Rhino.Geometry.Vector3d.ZAxis]
    for axis in world_axes:
        if abs(plane.Normal * axis) > (1 - tolerance):  # Dot product close to 1 or -1
            return True
    return False

def SetObjectDisplayModeToGhosted(object_id):
    mode = Rhino.Display.DisplayModeDescription.FindByName("Ghosted")
    if mode:
        attrs = sc.doc.Objects.Find(object_id).Attributes
        attrs.SetDisplayModeOverride(mode)
        sc.doc.Objects.ModifyAttributes(object_id, attrs, True)
        sc.doc.Views.Redraw()

def CreateOffsetRectangleFromCurvesAndColorByOrientation():
    curve_ids = rs.GetObjects("Select planar curves", rs.filter.curve)
    if not curve_ids:
        print("No curves selected. Operation canceled.")
        return

    if isinstance(curve_ids, str):
        curve_ids = [curve_ids]

    if not all(rs.IsCurvePlanar(curve_id) for curve_id in curve_ids):
        print("Selected curves are not planar. Operation canceled.")
        return

    plane = rs.PlaneFitFromPoints([pt for curve_id in curve_ids for pt in rs.CurvePoints(curve_id)])
    if not plane:
        print("The selected curves are not co-planar.")
        return

    # Determine orientation and set color and layer
    if is_vertical(plane) and not is_aligned_with_world_axes(plane):
        layer_name = "3D_Guide::3D_Guide_Srf-LooseVertical"
        color = (0, 255, 255)  # Cyan
    elif not is_vertical(plane) and not is_aligned_with_world_axes(plane):
        layer_name = "3D_Guide::3D_Guide_Srf-Loose"
        color = (255, 0, 255)  # Magenta
    else:
        # Surface is aligned with one of the world axes, no need to check which one as original logic is not needed
        layer_name = "3D_Guide::3D_Guide_Srf-Aligned"
        color = (255, 255, 0)  # Using Yellow as a placeholder for aligned surfaces

    # Create the layer if needed
    create_layer_if_needed("3D_Guide", (0, 0, 0))  # Black base layer
    create_layer_if_needed(layer_name, color)

    bbox = rs.BoundingBox(curve_ids, plane)
    if not bbox:
        print("Could not calculate the bounding box.")
        return

    bbox_center = rs.PointDivide(rs.PointAdd(bbox[0], bbox[2]), 2)
    offset_distance = 100000.0
    length = rs.Distance(bbox[0], bbox[1]) + (2 * offset_distance)
    width = rs.Distance(bbox[1], bbox[2]) + (2 * offset_distance)

    pt1 = rs.PointAdd(bbox_center, plane.XAxis * (-length / 2) + plane.YAxis * (-width / 2))
    pt2 = rs.PointAdd(bbox_center, plane.XAxis * (length / 2) + plane.YAxis * (-width / 2))
    pt3 = rs.PointAdd(bbox_center, plane.XAxis * (length / 2) + plane.YAxis * (width / 2))
    pt4 = rs.PointAdd(bbox_center, plane.XAxis * (-length / 2) + plane.YAxis * (width / 2))

    expanded_rectangle = rs.AddPolyline([pt1, pt2, pt3, pt4, pt1])
    expanded_Srf_id = rs.AddPlanarSrf(expanded_rectangle)[0]
    rs.DeleteObject(expanded_rectangle)

    if expanded_Srf_id:
        rs.ObjectLayer(expanded_Srf_id, layer_name)
        rs.ObjectColor(expanded_Srf_id, color)
        SetObjectDisplayModeToGhosted(expanded_Srf_id)
        print("Offset rectangle created on '{}' layer with specified color and set to Ghosted display mode.".format(layer_name))
    else:
        print("Failed to create the offset rectangle.")

if __name__ == "__main__":
    CreateOffsetRectangleFromCurvesAndColorByOrientation()
