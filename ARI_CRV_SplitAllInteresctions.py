import rhinoscriptsyntax as rs

def main():
    # Step 1: Get selected objects
    selected_objects = rs.GetObjects("Select curves")
    if not selected_objects:
        print("No objects selected.")
        return
    
    # Step 2: Filter curves
    curves = [obj for obj in selected_objects if rs.IsCurve(obj)]
    if not curves:
        print("No curves found.")
        return
    
    # Step 3: Find intersection points
    intersection_points = []
    for i in range(len(curves)):
        for j in range(i + 1, len(curves)):
            pts = rs.CurveCurveIntersection(curves[i], curves[j])
            if pts:
                for pt in pts:
                    if pt[0] == 1:  # Only consider intersection points
                        intersection_points.append(pt[1])
    
    if not intersection_points:
        print("No intersections found.")
        return
    
    # Step 4: Split curves at intersection points
    for curve in curves:
        curve_intersections = []
        for pt in intersection_points:
            param = rs.CurveClosestPoint(curve, pt)
            if param is not None:
                curve_intersections.append(param)
        if curve_intersections:
            rs.SplitCurve(curve, curve_intersections)
    
    # Step 5: Remove the intersection points
    rs.DeleteObjects(rs.ObjectsByType(1, select=False, state=2))  # 1 = point objects, state=2 = hidden or locked objects

    print("Curves split at intersection points and points removed.")

if __name__ == "__main__":
    main()
