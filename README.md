## Alias and Shortcut Bindings

### Line Commands

| Alias | Macro      |
|-------|------------|
| L     | '_Line     |
| SL    | '_Split    |
| TR    | '_Connect  |
| TT    | '_Trim     |

### View Commands

| Alias       | Macro                      | Shortcut |
|-------------|----------------------------|----------|
| H           | '_Hide                     |          |
| HI          | '_Isolate                  |          |
| LO          | '_OneLayerOff              |          |
| WW          | '_CPlane _World _Top       |          |
| ZS          | '_Zoom _Selected           |          |
|             | '_CPlane _Object           | Ctrl+D   |
|             | '_CPlane _World _Top       | Ctrl+1   |
|             | '_CPlane _World _Front     | Ctrl+2   |
|             | '_CPlane _World _Right     | Ctrl+3   |
|             | '_CPlane _World _Back      | Ctrl+4   |
|             | '_CPlane _World _Left      | Ctrl+5   |

### Transform Commands

| Alias  | Macro                                                      |
|--------|------------------------------------------------------------|
| M      | '_Move                                                     |
| E      | '_PushPull                                                 |
| EC     | '_ExtrudeCrv                                               |
| ES     | '_ExtrudeSrf                                               |
| E      | '_Explode                                                  |
| ESrf   | '_DupBorder _SelLast _PlanarSrf _SelPrev _Delete _SelLast  |
| P      | '_Planar                                                   |
| PC     | '_ProjectToCPlane _Yes                                     |
| PS     | '_PlanarSrf _SelLast _MergeAllEdges                        |
| J      | '_Join                                                     |
| JJ     | '_MergeAllCoplanarFaces                                     |
| JJJ    | '_MergeAllEdges                                            |

### Boolean Commands

| Alias  | Macro                                                      |
|--------|------------------------------------------------------------|
| BS     | '_BooleanSplit                                             |
| BU     | '_BooleanUnion _MergeAllEdges _MergeAllCoplanarFaces       |
| BD     | '_BooleanDifference                                        |


## RunPythonScripts

## Scripts

## Scripts

| Alias | Script Name                               | Command                                                   |
|-------|-------------------------------------------|-----------------------------------------------------------|
|       | ARI_BLOCK_SuperSelectBlocks               | ! _-RunPythonScript "X:\\...\\ARI_BLOCK_SuperSelectBlocks.py"               |
|       | ARI_CRV_SplitAllIntersections             | ! _-RunPythonScript "X:\\...\\ARI_CRV_SplitAllIntersections.py"             |
|       | ARI_GEO_CappedSlice                       | ! _-RunPythonScript "X:\\...\\ARI_GEO_CappedSlice.py"                       |
|       | ARI_GEO_Check                             | ! _-RunPythonScript "X:\\...\\ARI_GEO_Check.py"                             |
|       | ARI_GEO_CleanUnion                        | ! _-RunPythonScript "X:\\...\\ARI_GEO_CleanUnion.py"                        |
|       | ARI_LAYER_IFCandBeamLayers                | ! _-RunPythonScript "X:\\...\\ARI_LAYER_IFCandBeamLayers.py"                |
|       | ARI_OBJ_ObjMoveToLayerByType              | ! _-RunPythonScript "X:\\...\\ARI_OBJ_ObjMoveToLayerByType.py"              |
|       | ARI_SHORTCUTS_Load                        | ! _-RunPythonScript "X:\\...\\ARI_SHORTCUTS_Load.py"                        |
|       | ARI_SRF_CrvHorizontalPlane                | ! _-RunPythonScript "X:\\...\\ARI_SRF_CrvHorizontalPlane.py"                |
|       | ARI_SRF_CrvVerticalPlane                  | ! _-RunPythonScript "X:\\...\\ARI_SRF_CrvVerticalPlane.py"                  |
|       | ARI_SRF_PlanarPlaneFromCrv                | ! _-RunPythonScript "X:\\...\\ARI_SRF_PlanarPlaneFromCrv.py"                |



#Load Shortcuts

```
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


```