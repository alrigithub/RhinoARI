import Rhino
import rhinoscriptsyntax as rs
import scriptcontext

def recursive_boolean_union_and_merge_faces():
    # Select solids for Boolean union
    solid_ids = rs.GetObjects("Select solids for Boolean union", rs.filter.polysurface, preselect=True)
    if not solid_ids:
        print("No solids selected.")
        return

    # Convert GUIDs to Brep objects
    breps = [rs.coercebrep(id) for id in solid_ids if rs.coercebrep(id)]

    # Attempt to union all breps
    union_results = Rhino.Geometry.Brep.CreateBooleanUnion(breps, scriptcontext.doc.ModelAbsoluteTolerance)
    
    if not union_results:
        print("Boolean union operation failed or no changes were made.")
        return
    
    # Assuming successful union, process each result (though typically expecting one)
    for brep in union_results:
        # In Rhino 7 and above, try merging coplanar faces of the resulting brep
        if Rhino.RhinoApp.Version.Major >= 7:
            brep.MergeCoplanarFaces(scriptcontext.doc.ModelAbsoluteTolerance)
        
        # Add the final brep to the document
        final_brep_id = scriptcontext.doc.Objects.AddBrep(brep)
        rs.ObjectColor(final_brep_id, rs.ObjectColor(solid_ids[0]))
    
    # Delete the original solids
    rs.DeleteObjects(solid_ids)

    scriptcontext.doc.Views.Redraw()
    print("Operation completed successfully.")

if __name__ == "__main__":
    recursive_boolean_union_and_merge_faces()
