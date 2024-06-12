import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

def is_face_parallel_to_axis(face_normal, axis_vector):
    """Check if a face normal is parallel to an axis."""
    dot_product = abs(Rhino.Geometry.Vector3d.Multiply(face_normal, axis_vector))
    return dot_product > 0.999

def explode_and_color_polysurface(polysurface_id):
    if not polysurface_id or not rs.IsPolysurface(polysurface_id):
        print("Invalid input or the object is not a polysurface.")
        return

    # Explode the polysurface into individual surfaces
    surface_ids = rs.ExplodePolysurfaces(polysurface_id)
    if not surface_ids:
        print("Failed to explode the polysurface.")
        return

    # Axis vectors
    x_axis = Rhino.Geometry.Vector3d(1, 0, 0)
    y_axis = Rhino.Geometry.Vector3d(0, 1, 0)
    z_axis = Rhino.Geometry.Vector3d(0, 0, 1)

    # Colors
    x_color = (255, 0, 0)  # Red
    y_color = (0, 255, 0)  # Green
    z_color = (0, 0, 255)  # Blue
    planar_non_parallel_color = (255, 255, 0)  # Yellow
    non_planar_color = (128, 0, 128)  # Purple

    # Initialize a list to collect objects to isolate
    objects_to_isolate = []

    for surface_id in surface_ids:
        brep = rs.coercebrep(surface_id)
        if brep:
            for face in brep.Faces:
                if face.IsPlanar():
                    normal = face.NormalAt(face.Domain(0).Mid, face.Domain(1).Mid)
                    normal.Unitize()
                    if is_face_parallel_to_axis(normal, x_axis):
                        rs.ObjectColor(surface_id, x_color)
                    elif is_face_parallel_to_axis(normal, y_axis):
                        rs.ObjectColor(surface_id, y_color)
                    elif is_face_parallel_to_axis(normal, z_axis):
                        rs.ObjectColor(surface_id, z_color)
                    else:
                        rs.ObjectColor(surface_id, planar_non_parallel_color)
                else:
                    rs.ObjectColor(surface_id, non_planar_color)
                objects_to_isolate.append(surface_id)

    # Isolate the resulting objects
    rs.SelectObjects(objects_to_isolate)
    rs.Command("_Isolate")
    return objects_to_isolate

if __name__ == "__main__":
    # Ask the user to select a polysurface
    polysurface_id = rs.GetObject("Select a polysurface to explode", rs.filter.polysurface)
    if not polysurface_id:
        print("No polysurface selected.")
    else:
        # Explode the polysurface and color the resulting surfaces
        colored_surfaces = explode_and_color_polysurface(polysurface_id)
        if colored_surfaces:
            print("Successfully colored {} surfaces.".format(len(colored_surfaces)))
        else:
            print("No surfaces were colored.")
