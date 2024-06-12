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
rs.AddAlias("ESrf", "'_DupBorder _SelLast _PlanarSrf _SelPrev _Delete _SelLast")
rs.AddAlias("P", "'_Planar")
rs.AddAlias("PC", "'_ProjectToCPlane _Yes")
rs.AddAlias("PS", "'_PlanarSrf _SelLast _MergeAllEdges")
rs.AddAlias("J", "'_Join")
rs.AddAlias("JJ", "'_Join _MergeAllEdges _MergeAllCoplanarFaces")
rs.AddAlias("ES", "'_ExtrudeSrf")
rs.AddAlias("E", "'_Explode")

# Boolean Commands
rs.AddAlias("BS", "'_BooleanSplit")
rs.AddAlias("BU", "'_BooleanUnion _MergeAllEdges _MergeAllCoplanarFaces")
rs.AddAlias("BD", "'_BooleanDifference")

# -----

# Add keyboard shortcuts for view commands
rs.Command("'_OptionsPage _Keyboard")
rs.AddShortcut("Ctrl+D", "'_CPlane '_Object")
rs.AddShortcut("Ctrl+1", "'_CPlane '_World _Top")
rs.AddShortcut("Ctrl+2", "'_CPlane '_World _Front")
rs.AddShortcut("Ctrl+3", "'_CPlane '_World _Right")
rs.AddShortcut("Ctrl+4", "'_CPlane '_World _Back")
rs.AddShortcut("Ctrl+5", "'_CPlane '_World _Left")