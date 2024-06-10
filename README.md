#Alias
## Line Commands

| Alias      | Macro                          |
|------------|--------------------------------|
| L          | '_Line                         |
| SL         | '_Split                        |
| TR         | '_Connect                      |
| TT         | '_Trim                         |

## View Commands

| Alias      | Macro                          |
|------------|--------------------------------|
| H          | '_Hide                         |
| HI         | '_Isolate                      |
| LO         | '_OneLayerOff                  |
| O          | '_Ortho                        |
| objectplane| '_CPlane _Object               |
| WW         | '_CPlane _World _Top           |
| ZS         | '_Zoom _Selected               |

## Transform Commands

| Alias      | Macro                          |
|------------|--------------------------------|
| M          | ! _Move                        |
| E          | PushPull                       |
| EC         | '_ExtrudeCrv                   |
| ESrf       | '_DupBorder _SelLast _PlanarSrf _SelPrev _Delete _SelLast            |
| P          | '_Planar                       |
| PC         | '_ProjectToCPlane _Yes         |
| PS         | '_PlanarSrf '_SelLast '_MergeAllEdges |

#Shortcuts

#Scripts

| Task        | Script Path                                                                                                                |
|-------------|-----------------------------------------------------------------------------------------------------------------------------|
| guide       | ! _-RunPythonScript "J:\\...\\SRF_guide_GuidePlaneFromCrv.py"  |
| wall        | ! _-RunPythonScript "J:\\...\\SRF_wall_LineLoftVertical.py"    |
| floor       | ! _-RunPythonScript "J:\\...\\SRF_floor_LineLoftHorizontal.py"  |
| checkgeo    | ! _-RunPythonScript "J:\\...\\RhinoPythonScripts\\GEO_Check.py"|
| smartslice  | ! _-RunPythonScript "J:\\...\\GEO_SL_CappedSlice.py"           |
| smartunion  | ! _-RunPythonScript "J:\\...\\GEO_JJ_CleanUnion.py"            |
| trash       | ! _-RunPythonScript "J:\\...\\LAYER_Trash.py"                   |


