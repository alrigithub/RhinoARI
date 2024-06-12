import rhinoscriptsyntax as rs

# Line Commands
rs.AddAlias("L", "'_Line")
rs.AddAlias("SL", "'_Split")
rs.AddAlias("TR", "'_Connect")
rs.AddAlias("TT", "'_Trim")

# View Commands
rs.AddAlias("H", "'_Hide")
rs.AddAlias("HI", "'_Isolate")
rs.AddAlias("LO", "'_OneLayerOff")
rs.AddAlias("WW", "'_CPlane _World _Top")
rs.AddAlias("ZS", "'_Zoom _Selected")

# Transform Commands
rs.AddAlias("M", "'_Move")
rs.AddAlias("E", "'_PushPull")
rs.AddAlias("EC", "'_ExtrudeCrv")
rs.AddAlias("ES", "'_ExtrudeSrf")
rs.AddAlias("E", "'_Explode")
rs.AddAlias("ESrf", "'_DupBorder _SelLast _PlanarSrf _SelPrev _Delete _SelLast")
rs.AddAlias("P", "'_Planar")
rs.AddAlias("PC", "'_ProjectToCPlane _Yes")
rs.AddAlias("PS", "'_PlanarSrf _SelLast _MergeAllEdges")
rs.AddAlias("J", "'_Join")
rs.AddAlias("JJ", "'_MergeAllCoplanarFaces")
rs.AddAlias("JJJ", "'_MergeAllEdges")


# Boolean Commands
rs.AddAlias("BS", "'_BooleanSplit")
rs.AddAlias("BU", "'_BooleanUnion _MergeAllEdges _MergeAllCoplanarFaces")
rs.AddAlias("BD", "'_BooleanDifference")

# -----

# Add keyboard shortcuts for view commands
# This command might require manual entry if the RhinoScript API does not support direct shortcut bindings.
# Use this as a guide for setting up shortcuts manually.

rs.Command("'_OptionsPage '_Keyboard")
rs.Command("'_OptionsPage '_Keyboard '_NewShortcut Ctrl+D '_Macro ''_CPlane '_Object")
rs.Command("'_OptionsPage '_Keyboard '_NewShortcut Ctrl+1 '_Macro ''_CPlane '_World '_Top")
rs.Command("'_OptionsPage '_Keyboard '_NewShortcut Ctrl+2 '_Macro ''_CPlane '_World '_Front")
rs.Command("'_OptionsPage '_Keyboard '_NewShortcut Ctrl+3 '_Macro ''_CPlane '_World '_Right")
rs.Command("'_OptionsPage '_Keyboard '_NewShortcut Ctrl+4 '_Macro ''_CPlane '_World '_Back")
rs.Command("'_OptionsPage '_Keyboard '_NewShortcut Ctrl+5 '_Macro ''_CPlane '_World '_Left")
