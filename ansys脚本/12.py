# ----------------------------------------------
# Script Recorded by Ansys Electronics Desktop Version 2022.1.0
# 15:29:02  10月 13, 2022
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("CeShi")
oDesign = oProject.SetActiveDesign("Maxwell2DDesign1")
oModule = oDesign.GetModule("FieldsReporter")
oModule.SetPlotsSolutionContext(["Har_Edge_Force_Density1"], "Setup1 : Transient", "Time=\'0.0050000000000000027s\'")
oModule.DeleteFieldPlot(["Har_Edge_Force_Density1"])
oModule.CreateFieldPlot(
	[
		"NAME:Har_Edge_Force_Density1",
		"SolutionName:="	, "Setup1 : Transient",
		"UserSpecifyName:="	, 0,
		"UserSpecifyFolder:="	, 0,
		"QuantityName:="	, "Har_Edge_Force_Density",
		"PlotFolder:="		, "Har-Edge-Force",
		"StreamlinePlot:="	, False,
		"AdjacentSidePlot:="	, False,
		"FullModelPlot:="	, False,
		"IntrinsicVar:="	, "Freq=\'0Hz\' Phase=\'0deg\'",
		"PlotGeomInfo:="	, [1,"Edge",4,"50","61","72","38"],
		"FilterBoxes:="		, [0],
		[
			"NAME:PlotOnLineSettings",
			[
				"NAME:LineSettingsID",
				"Width:="		, 4,
				"Style:="		, "Cylinder"
			],
			"IsoValType:="		, "Tone",
			"ArrowUniform:="	, False,
			"NumofArrow:="		, 100,
			"Refinement:="		, 0
		],
		"EnableGaussianSmoothing:=", False,
		"SurfaceOnly:="		, True
	], "Field")
oModule.SetPlotsSolutionContext(["Har_Edge_Force_Density1"], "Setup1 : Transient", "Time=\'0.0050000000000000027s\'")
oModule.SetPlotsSolutionContext(["Har_Edge_Force_Density1"], "Setup1 : Transient", "Time=\'0.0050000000000000027s\'")
oModule.DeleteFieldPlot(["Har_Edge_Force_Density1"])
oModule.CreateFieldPlot(
	[
		"NAME:Har_Edge_Force_Density1",
		"SolutionName:="	, "Setup1 : Transient",
		"UserSpecifyName:="	, 0,
		"UserSpecifyFolder:="	, 0,
		"QuantityName:="	, "Har_Edge_Force_Density",
		"PlotFolder:="		, "Har-Edge-Force",
		"StreamlinePlot:="	, False,
		"AdjacentSidePlot:="	, False,
		"FullModelPlot:="	, False,
		"IntrinsicVar:="	, "Freq=\'0Hz\' Phase=\'0deg\'",
		"PlotGeomInfo:="	, [1,"Edge",4,"50","61","72","38"],
		"FilterBoxes:="		, [0],
		[
			"NAME:PlotOnLineSettings",
			[
				"NAME:LineSettingsID",
				"Width:="		, 4,
				"Style:="		, "Cylinder"
			],
			"IsoValType:="		, "Tone",
			"ArrowUniform:="	, False,
			"NumofArrow:="		, 100,
			"Refinement:="		, 0
		],
		"EnableGaussianSmoothing:=", False,
		"SurfaceOnly:="		, True
	], "Field")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            oModule.DeleteFieldPlot(["Har_Edge_Force_Density1"])
  oModule.CreateFieldPlot(
	[
		"NAME:Har_Edge_Force_Density1",
		"SolutionName:="	, "Setup1 : Transient",
		"UserSpecifyName:="	, 0,
		"UserSpecifyFolder:="	, 0,
		"QuantityName:="	, "Har_Edge_Force_Density",
		"PlotFolder:="		, "Har-Edge-Force",
		"StreamlinePlot:="	, False,
		"AdjacentSidePlot:="	, False,
		"FullModelPlot:="	, False,
		"IntrinsicVar:="	, "Freq=\'0Hz\' Phase=\'0deg\'",
		"PlotGeomInfo:="	, [1,"Edge",4,"50","61","72","38"],
		"FilterBoxes:="		, [0],
		[
			"NAME:PlotOnLineSettings",
			[
				"NAME:LineSettingsID",
				"Width:="		, 4,
				"Style:="		, "Cylinder"
			],
			"IsoValType:="		, "Tone",
			"ArrowUniform:="	, False,
			"NumofArrow:="		, 100,
			"Refinement:="		, 0
		],
		"EnableGaussianSmoothing:=", False,
		"SurfaceOnly:="		, True
	], "Field")
oModule.SetPlotsSolutionContext(["Har_Edge_Force_Density1"], "Setup1 : Transient", "Time=\'0.0050000000000000027s\'")
oModule.ExportFieldPlot("Har_Edge_Force_Density1", False, "E:\\Desktop\\11.png")
oModule.ExportFieldPlot("Har_Edge_Force_Density1", False, "E:\\Desktop\\11.case")
oModule.SetPlotsSolutionContext(["Har_Edge_Force_Density1"], "Setup1 : Transient", "Time=\'0.0050000000000000027s\'")
 oModule.CreateFieldPlot(
	[
		"NAME:Har_Edge_Force_Density1",
		"SolutionName:="	, "Setup1 : Transient",
		"UserSpecifyName:="	, 0,
		"UserSpecifyFolder:="	, 0,
		"QuantityName:="	, "Har_Edge_Force_Density",
		"PlotFolder:="		, "Har-Edge-Force",
		"StreamlinePlot:="	, False,
		"AdjacentSidePlot:="	, False,
		"FullModelPlot:="	, False,
		"IntrinsicVar:="	, "Freq=\'0Hz\' Phase=\'0deg\'",
		"PlotGeomInfo:="	, [1,"Edge",4,"50","61","72","38"],
		"FilterBoxes:="		, [0],
		[
			"NAME:PlotOnLineSettings",
			[
				"NAME:LineSettingsID",
				"Width:="		, 4,
				"Style:="		, "Cylinder"
			],
			"IsoValType:="		, "Tone",
			"ArrowUniform:="	, False,
			"NumofArrow:="		, 100,
			"Refinement:="		, 0
		],
		"EnableGaussianSmoothing:=", False,
		"SurfaceOnly:="		, True
	], "Field")
oModule.SetPlotsSolutionContext(["Har_Edge_Force_Density1"], "Setup1 : Transient", "Time=\'0.0050000000000000027s\'")
oModule.SetPlotsSolutionContext(["Har_Edge_Force_Density1"], "Setup1 : Transient", "Time=\'0.0050000000000000027s\'")
