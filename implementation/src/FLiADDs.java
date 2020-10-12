import java.io.File;
import java.io.IOException;
import java.time.Duration;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.concurrent.TimeUnit;

import org.apache.commons.io.FileUtils;

import soot.Body;
import soot.Local;
import soot.PackManager;
import soot.PatchingChain;
import soot.Scene;
import soot.SootClass;
import soot.SootMethod;
import soot.Unit;
import soot.UnitBox;
import soot.Value;
import soot.ValueBox;
import soot.jimple.AbstractStmtSwitch;
import soot.jimple.AssignStmt;
import soot.jimple.Constant;
import soot.jimple.IdentityStmt;
import soot.jimple.InvokeExpr;
import soot.jimple.InvokeStmt;
import soot.jimple.SpecialInvokeExpr;
import soot.jimple.StaticInvokeExpr;
import soot.jimple.Stmt;
import soot.jimple.VirtualInvokeExpr;
import soot.jimple.infoflow.android.InfoflowAndroidConfiguration;
import soot.jimple.infoflow.android.SetupApplication;
import soot.jimple.infoflow.solver.cfg.InfoflowCFG;
import soot.jimple.internal.ImmediateBox;
import soot.jimple.internal.InvokeExprBox;
import soot.jimple.toolkits.callgraph.CallGraph;
import soot.jimple.toolkits.callgraph.Edge;
import soot.options.Options;
import soot.toolkits.graph.Block;
import soot.toolkits.graph.BlockGraph;
import soot.toolkits.graph.DirectedGraph;
import soot.toolkits.graph.ExceptionalBlockGraph;
import soot.util.Chain;
import soot.toolkits.graph.ExceptionalUnitGraph;
import soot.toolkits.scalar.SimpleLiveLocals;
import soot.toolkits.scalar.SimpleLocalDefs;
import soot.toolkits.scalar.SimpleLocalUses;
import soot.toolkits.scalar.SmartLocalDefs;
import soot.toolkits.scalar.UnitValueBoxPair;

public class FLiADDs {	
	public static String SourcesSinks;
	public static String platformPath;
	
	//domain
	static String domainName;
	//Intra-Procedural Data
	static List<List<UnitValueBoxPair>> IaData=new ArrayList<List<UnitValueBoxPair>>();
	static List<ConDe> IaDataConDe=new ArrayList<ConDe>();
	static String oldString;//to remove single L character
	static String newString;//to remove single L character
	//for backward dynamic slicing	
	Map<String, InstructionUnits> resultMapBW = new LinkedHashMap<String, InstructionUnits>();
	static ConDe currentBWCD;
	static int currentBWP=0;	
	//for forward dynamic slicing
	Map<String, InstructionUnits> resultMapFW = new LinkedHashMap<String, InstructionUnits>();
	static ConDe currentFWCD;
	static int currentFWP=0;	
	static int endP=0;
	
	
	
	public FLiADDs(String apkPath, String platFormDir,String androidJar) {
		InfoflowAndroidConfiguration config = new InfoflowAndroidConfiguration();
		config.getAnalysisFileConfig().setAndroidPlatformDir(platFormDir+androidJar);
		config.getAnalysisFileConfig().setTargetAPKFile(apkPath);
		config.setMergeDexFiles(true);
		config.setIgnoreFlowsInSystemPackages(false);
        
		/*
		Options.v().set_no_bodies_for_excluded(true);
		Options.v().set_allow_phantom_refs(true);
        Options.v().set_output_format(12);
        Options.v().set_src_prec(6);
        Options.v().set_keep_offset(false);
		config.getCallbackConfig().setEnableCallbacks(true);
		config.getAnalysisFileConfig().setSourceSinkFile("C:\\Users\\ \\eclipse-workspace\\AndroidSlicer-master\\AndroidSlicer-master\\tool\\SourcesAndSinks.txt");
		Options.v().set_src_prec(Options.src_prec_apk);
		Options.v().set_force_android_jar(platFormDir+androidJar);
		Options.v().set_android_api_version(26);
		Options.v().set_keep_line_number(true);
		Options.v().set_src_prec(Options.src_prec_apk);
		Options.v().set_process_dir(Collections.singletonList(apkPath));
		Options.v().set_android_jars(platformPath);
		Options.v().set_whole_program(true);
		Options.v().set_allow_phantom_refs(true);
		Options.v().set_output_format(Options.output_format_none);
		Options.v().setPhaseOption("cg.cha", "on");
		Scene.v().loadNecessaryClasses();*/

		
		SetupApplication analyzer = new SetupApplication(config);
		Options.v().set_src_prec(Options.src_prec_apk);
		Options.v().set_keep_line_number(true);
		Options.v().set_allow_phantom_refs(true);
		Options.v().set_process_dir(Collections.singletonList(apkPath));
		
		analyzer.constructCallgraph();
		try {
			TimeUnit.SECONDS.sleep(20);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		/*CallGraph appCallGraph = Scene.v().getCallGraph();
		for(Iterator<Edge> edgeIt = appCallGraph.iterator();edgeIt.hasNext();){
			Edge edge = edgeIt.next();
			Unit uSrc_Stmt=edge.srcStmt();
			SootMethod src_Mtd = edge.src();
			SootMethod dest_Mtd = edge.tgt();
			if(src_Mtd.getName().contains("onOptionsItemSelected")) System.out.println("Statement=" +uSrc_Stmt + "...source="+src_Mtd.getName()+"...destination=" + dest_Mtd.getName());
			}*/
	}
	
	public static void main(String args[]) {		
		try {
			LocalTime previousT = LocalTime.now();
			String apkLocation="C:\\Users\\ \\eclipse-workspace\\FLiAD\\apk\\";
			String apk="net.phunehehe.foocam_2.apk";
			String androidJar="android-26\\android.jar";
			String location="C:\\Users\\ \\eclipse-workspace\\FLiAD\\DS\\";
			boolean justTrace = false;
			String option = "final";//"test" or "final";//args[0];
			String fileToParse = location+apk+".logcat.txt";
			String pathApk = apkLocation+apk+"";
			String outFile = location+apk+".logcat.processed.txt";
			platformPath = ("C:\\Users\\ \\AppData\\Local\\Android\\Sdk\\platforms\\");//args[4];
			domainName="net.phunehehe";//"org.liberty.android.fantastischmemo";
			oldString="Lnet/phunehehe/";//"Lorg/liberty/android/fantastischmemo/";
			newString=oldString.replace("Lnet/", "net/");//bytecode - reference single L - removing
			//SourcesSinks = args[5];
			
			//backward slicing
			int posToSliceBW = 908;//10297;//9850;//-1;
			endP = posToSliceBW;
			
			//forward slicing
			int posToSliceFW = 0;//-1;
			
			//gathering info:
			if (option.equals("test")) {
				justTrace = true;
				//pathApk = args[1];
				//fileToParse = args[2];
				//outFile = args[3];
			} else {
				//pathApk = args[1];
				//fileToParse = args[2];
				//posToSlice = Integer.parseInt(args[3]);

			}
			List<Traces> trs = Parser.readFile(fileToParse);
			// HashMap<String, HashMap<String, ArrayList<String>>> map
			// =Parser.doFilePreparation(trs);

			FLiADDs FLiADDs = new FLiADDs(pathApk, platformPath,androidJar);
			// HashMap<Integer, ArrayList<InstructionUnits>> mp2 =
			// FLiADDs.getUnitMethodByLineNumberMethodNameClassName(map);
			// Input input =Parser.transformInput(mp2);
			Input input = FLiADDs.loadInputfromTraces(trs);
			List<String> callbackExecuted = new ArrayList<String>();
			if (justTrace) {
				System.out.println("Printing trace...");
				List<String> listTOPrint = new ArrayList<String>();
				Iterator entries = input.mapKeyNo.entrySet().iterator();
				while (entries.hasNext()) {
					Entry thisEntry = (Entry) entries.next();
					String key = (String) thisEntry.getKey();
					Integer value = (Integer) thisEntry.getValue();
					if (input.mapKeyUnits.get(key).getMethod().getName().startsWith("on")) {
						callbackExecuted.add(key);
						callbackExecuted.add("\n");
					}
					listTOPrint.add(key);
					// ...
				}

				FLiADDs.printList(listTOPrint, outFile);
				FLiADDs.printList(callbackExecuted, location+apk+  ".callbacks.txt");
				// FileUtils.writeLines(new File(outFile), input.mapKeyNo.keySet());
				
				listTOPrint = new ArrayList<String>();
				listTOPrint.add("start size="+IaData.size()+" \n");
				for(int i=0;i<IaData.size();i++) {
					for(int j=0;j<IaData.get(i).size();j++) {
						UnitValueBoxPair uvp=IaData.get(i).get(j);
						listTOPrint.add(uvp.getUnit().toString());
					}
					listTOPrint.add("\n");
				}
				listTOPrint.add("end");
				FLiADDs.printList(listTOPrint, location+apk+ ".IaData.txt");
				
				//IaDataBWDConDe
				listTOPrint = new ArrayList<String>();
				listTOPrint.add("start size="+IaDataConDe.size()+" \n");
				for(int i=0;i<IaDataConDe.size();i++) {
					ConDe cd= IaDataConDe.get(i);
					listTOPrint.add(cd.getControler().toString()+"<=>"+cd.getControlerMethod().toString()+"<=>"+cd.getFollower()+"<=>"+cd.getFound());
					listTOPrint.add("\n");
				}
				listTOPrint.add("end");
				FLiADDs.printList(listTOPrint, location+apk+ ".IaDataConDe.txt");
				System.out.println("Printing Complete.");
				
				LocalTime now = LocalTime.now();
				Duration duration = Duration.between(previousT, now);
				System.out.println(duration.getSeconds() + " seconds");
				
				System.exit(0);

			}

			System.out.println("size of the trace after loading:" + input.mapKeyNo.keySet().size());
			
			//*****start backward dynamic slicing
			System.out.println("Backward Testing for input:" + input.mapNoKey.get(posToSliceBW));
			List<MethodResult> results = FLiADDs.loadPDGBW(input, posToSliceBW);
			System.out.println("Printing backward static program dependence from point of interest:");
			List<String> staticPrint = new ArrayList<String>();
			List<String> dynamicPrint = new ArrayList<String>();
			for (MethodResult me : results) {
				Map<String, InstructionUnits> mapp = me.getMap();
				for (String key : mapp.keySet()) {
					InstructionUnits insUnit = mapp.get(key);
					//what is that? Hsu
					//System.out.println(key);
					staticPrint.add(key);
				}
			}
			System.out.println("Printing backward dynamic dependence:");
			//remove duplicated (?) Hsu
			Map<Unit,String> tmpD=new LinkedHashMap<Unit,String>();
			for(String key: FLiADDs.resultMapBW.keySet()) {
				if(tmpD.get(FLiADDs.resultMapBW.get(key).getUnit())==null)
					tmpD.put(FLiADDs.resultMapBW.get(key).getUnit(),FLiADDs.resultMapBW.get(key).getUnitId());
			}
			/*if (FLiADDs.resultMapBW.size() > 0) {
				for (String key : FLiADDs.resultMapBW.keySet()) {
					dynamicPrint.add(FLiADDs.resultMapBW.get(key).getUnitId());
				}
			}*/
				for (Unit key : tmpD.keySet()) {
					dynamicPrint.add(tmpD.get(key));
				}
			FLiADDs.printList(staticPrint, location+apk + "_bw_static.dat");
			FLiADDs.printList(dynamicPrint, location+apk + "_bw_dynamic.dat");		
			LocalTime now = LocalTime.now();
			Duration duration = Duration.between(previousT, now);
			System.out.println(duration.getSeconds() + " seconds");

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	Input loadInputfromTraces(List<Traces> tr) {
		int len = tr.size();
		System.out.println("length:" + len);

		Map<String, Map<Integer, String>> mapTrace = new LinkedHashMap();
		int i = 0;
		int jj = 0;
		for (Traces t : tr) {
//			if(i==853)
//			{
//				System.out.println("gotcha");
//			}
			//if(t._class.contains("QuizActivity")) System.out.println("checking............");
			if (!mapTrace.containsKey(t._method + t._class)) {
				Map<Integer, String> temp = new LinkedHashMap<Integer, String>();
				temp.put(i, t._ins);
				mapTrace.put(t._method + t._class, temp);
				//System.out.println(t._ins);
				//if(t._class.contains("QuizActivity"))  System.out.println(t._ins);
				//System.out.println("hihih1111");
				jj++;
			} else {
				Map<Integer, String> temp = mapTrace.get(t._method + t._class);
				temp.put(i, t._ins);
				mapTrace.put(t._method + t._class, temp);
				//System.out.println(t._ins);
				//if(t._class.contains("QuizActivity")) System.out.println(t._ins);
				//if(t._class.contains("QuizActivity")) System.out.println("hihih2222>>>"+t._method+","+t._class);
				jj++;
			}
			i++;
		}

		System.out.println("Processed:" + jj);
		System.out.println("mapTrace size="+mapTrace.size());
		//SootClass sflr = Scene.v().getSootClass("org.liberty.android.fantastischmemo.ui.StudyActivity");
		//System.out.println("hello1="+sflr.getPackageName());
		//System.out.println("hello2="+sflr.getMethods());
		//System.out.println("hello0>>>"+Scene.v().getApplicationClasses().getSuccOf(sflr));	
		//System.out.println("hello2>>>"+Scene.v().loadClassAndSupport("org.liberty.android.fantastischmemo.ui.StudyActivity").moduleName);
		//System.out.println("hello2>>>"+Scene.v().loadClassAndSupport("org.liberty.android.fantastischmemo.ui.StudyActivity").getPackageName());
		//System.out.println("hello1>>>"+Scene.v().containsClass("org.liberty.android.fantastischmemo.ui.StudyActivity"));
		//System.out.println("hello3>>>"+Scene.v().getCallGraph().findEdge(u, callee));
		//System.out.println("hello2>>>"+sflr.isAbstract());
		//System.out.println("hello3>>>"+sflr.isJavaLibraryClass());
		//System.out.println("hello4>>>"+sflr.isLibraryClass());
		//System.out.println("hello5>>>"+sflr.isInnerClass());
		//System.out.println("hello3>>>"+sflr.getMethodByName("onCreate"));
		InstructionUnits[] ins = new InstructionUnits[len];
		List<InstructionUnits> listUnis = new ArrayList<InstructionUnits>();
		Chain<SootClass> chain = Scene.v().getApplicationClasses();
		Iterator<SootClass> iterator = chain.snapshotIterator();
		i = 0;
		while (iterator.hasNext()) {
			SootClass sc = iterator.next();
			List<SootMethod> methods = sc.getMethods();
			for (SootMethod mt : methods) {
				String key = mt.getName() + sc.getName();				
				try {
					if (mt.getActiveBody() == null) {
						System.out.println("hello");
						continue;}
				} catch (Exception ex) {
					//if(sc.getName().contains("QuizActivity")) {
						//System.out.println("No body:" + Scene.v().loadClass(sc.getName(), sc.BODIES).isSynchronized());
					//}
					System.out.println("No body:");//+ mt.getName() +","+sc.getName()
					continue;
				}
			try {
			if (sc.getName().contains(domainName) && 
						mt.getActiveBody().toString().contains("new android.content.Intent") && 
						mt.getActiveBody().toString().contains("startActivity")) {	//bug: if there are more than one calling startActivity in a method, this condition make duplicated info with same callee class				
						PatchingChain<Unit> units1 = mt.getActiveBody().getUnits();
						//Map<String, Unit> unitString1 = new LinkedHashMap<String, Unit>();
						for (Unit u1 : units1) {
							//System.out.println("::::::::::::::::::::::::::::::" + u1.toString() + "::::::::::::::::");
							if(u1.toString().contains("startActivity")) {
								//System.out.println(u1.getUseAndDefBoxes());
								List<ValueBox> useBoxes = u1.getUseBoxes();
								for (ValueBox vb : useBoxes) {
									if(vb instanceof InvokeExprBox) {
										Value intentLocal = vb.getValue();									
										useBoxes = intentLocal.getUseBoxes();
										//System.out.println(useBoxes);//[ImmediateBox($r2), JimpleLocalBox($r0)]
										for(ValueBox vbb:useBoxes) {										
											if(vbb instanceof ImmediateBox) {
												//System.out.println(vbb.getValue());
												ExceptionalUnitGraph ex = new ExceptionalUnitGraph(mt.getActiveBody());	
												SimpleLocalDefs simpleLocalDefs = new SimpleLocalDefs(ex);
												SimpleLocalUses simpleLocalUses = new SimpleLocalUses(ex,simpleLocalDefs);
												//System.out.println(simpleLocalUses.getUsedVariables());
												if(vbb.getValue() instanceof Local)
													{
													List<UnitValueBoxPair> tmpUVBP=simpleLocalUses.getUsesOf(simpleLocalDefs.getDefsOf((Local) vbb.getValue()).get(0));
													IaData.add(tmpUVBP);
													for(UnitValueBoxPair uvb : tmpUVBP) {
														if(uvb.getUnit()!=null && uvb.getUnit().toString().contains("specialinvoke")
															&& uvb.getUnit().toString().split("class")!=null
															&& (uvb.getUnit().toString().split("class")).length>1){
														//System.out.println("hello222>>>>"+(uvb.getUnit().toString().split("class"))[1]);	
														String tmpC=(uvb.getUnit().toString().split("class"))[1];
														tmpC = tmpC.substring(3,tmpC.length()-3);
														tmpC = tmpC.replace("/", ".");
														//System.out.println("hello="+tmpC);
														IaDataConDe.add(new ConDe(sc,mt,Scene.v().getSootClass(tmpC),false));
														}
														}
													
													}
													
											}
										}
									}
								}
							}
							/*if(u1.toString().contains("startActivity")) {
								//try to build graph start
								//System.out.println(u1.getUseAndDefBoxes());
								List<ValueBox> useBoxes = u1.getUseBoxes();
								for (ValueBox vb : useBoxes) {
									if(vb instanceof InvokeExprBox) {
										Value intentLocal = vb.getValue();
										
										useBoxes = intentLocal.getUseBoxes();
										//System.out.println(useBoxes	);//[ImmediateBox($r2), JimpleLocalBox($r0)]
										for(ValueBox vbb:useBoxes) {
											
											if(vbb instanceof ImmediateBox) {
												//System.out.println((Local) vbb.getValue());
												//(Local) vbb.getValue()											
												ExceptionalUnitGraph ex = new ExceptionalUnitGraph(mt.getActiveBody());	
												//SimpleLiveLocals simpleLiveLocals = new SimpleLiveLocals(ex);
												//List<Local> locals = simpleLiveLocals.getLiveLocalsBefore(u1);
												//for(Local l:locals) {
													//System.out.println(l);
													//System.out.println(l.get);
												//}
												//SmartLocalDefs smartLocalDefs = new SmartLocalDefs(ex,simpleLiveLocals);
												//System.out.println(smartLocalDefs.getGraph());
												SimpleLocalDefs simpleLocalDefs = new SimpleLocalDefs(ex);
												//System.out.println(simpleLocalDefs.getDefsOf((Local) vbb.getValue()));//$r2 = new android.content.Intent										
												//System.out.println(simpleLocalDefs.getDefsOf((Local) vbb.getValue()).get(0));
												SimpleLocalUses simpleLocalUses = new SimpleLocalUses(ex,simpleLocalDefs);
												//System.out.println(simpleLocalUses.getUsedVariables());
												System.out.println(simpleLocalUses.getUsesOf(simpleLocalDefs.getDefsOf((Local) vbb.getValue()).get(0)));
											}
										}
									}
								}
								InfoflowCFG icfg = new InfoflowCFG();
						        DirectedGraph<Unit> ug = icfg.getOrCreateUnitGraph(mt);
						        Iterator<Unit> uit = ug.iterator();
						        while (uit.hasNext()) {
						            Unit u = uit.next();
						            if (u.branches()) {
						                List<Unit> list = icfg.getSuccsOf(u);
						                System.out.println(list);
						            }else if(icfg.isCallStmt(u)) {
						            	 System.out.println("call Statement="+u);
						            }else if(icfg.isReturnSite(u)) {
						            	System.out.println("call ReturnSite="+u);
						            }else if(icfg.isReachable(u)) {
						            	System.out.println("call Reachable="+u);
						            }else if(icfg.isStartPoint(u)) {
						            	
						            }
						        }
							}*/
						}
						
					}
				}catch(Exception e) {
					System.out.println("e=>"+e);
				}
				PatchingChain<Unit> units = mt.getActiveBody().getUnits();
				Map<String, Unit> unitString = new LinkedHashMap<String, Unit>();
				for (Unit u : units) {
					//unitString.put(u.toString().replace(oldString, newString).replace(";\"", "\""), u);//why ; there and needed to replace?
					unitString.put(u.toString(), u);//why ; there and needed to replace?
					//System.out.println(unitString);
					if(mt.getName().equals("onPictureTaken")) {// && mt.getDeclaringClass().getName().equals("org.liberty.android.fantastischmemo.ui.QuizActivity")) {
						//System.out.println("hello...u="+u.toString());
						//System.out.println("hello...u="+unitString.get(u.toString().replace(oldString, newString).replace(";\"", "\"")));
					}
				}
				if (!mapTrace.keySet().contains(key))
					{
					    // System.out.println("hello---"+key);
						continue;
					}
				
				
				Map<Integer, String> temp = mapTrace.get(key);
				//System.out.println("Entering:"+mt.getName()+",class "+mt.getDeclaringClass().getName());
				if(mt.getName().equals("onOptionsItemSelected") && mt.getDeclaringClass().getName().equals("org.liberty.android.fantastischmemo.ui.QuizActivity")) {
				//System.out.println("hello...temp="+temp.size()+","+temp);
				//System.out.println("hello...unitString="+unitString.size()+","+unitString);
				}
				for (Integer key1 : temp.keySet()) {
					if(temp.get(key1).contains("onPictureTaken") || key1==499) {
						//System.out.println(">>>>"+unitString.keySet().contains(temp.get(key1)));
						//System.out.println(temp.get(key1));
					}
					if (unitString.keySet().contains(temp.get(key1))) {
						Unit unit = unitString.get(temp.get(key1));
						if(mt.getName().equals("onOptionsItemSelected") && mt.getDeclaringClass().getName().equals("org.liberty.android.fantastischmemo.ui.QuizActivity")) {
							//System.out.println("hello...unit="+unit);
							}
						i++;
						InstructionUnits iu = new InstructionUnits();
						iu.setMethod(mt);
						iu.setUnit(unit);
						iu.setLineNo(key1);
						iu.setSootUnitId();
						try {
							// System.out.println("This is filled up! "+ins[key1].getUnitId());
						} catch (Exception ex) {

						}
						ins[key1] = iu;
						listUnis.add(iu);
					}
				}

			}

		}
		System.out.println("i:" + i + "size:" + listUnis.size());
		// Map <String, InstructionUnits> mapIns = new LinkedHashMap<>();
		Input input = new Input();
		i = 0;

		while (i < ins.length) {
			// mapIns.put(ins[i].getUnitId(), ins[i]);
			if (ins[i] != null) {

				input.mapKeyNo.put(ins[i].getUnitId(), ins[i].getLineNo());
				input.mapKeyUnits.put(ins[i].getUnitId(), ins[i]);
				input.mapNoKey.put(ins[i].getLineNo(), ins[i].getUnitId());
			}

			i++;
		}

		// for(map)
		//update found or not
		try {
		if(IaDataConDe!=null)
		{
			for(int l=0; l<IaDataConDe.size();l++ ) {
				ConDe cd = IaDataConDe.get(l);
				//if(mapTrace.get(cd.getFollower().getMethodByName("onCreate").getName()+cd.getFollower().getName())!=null)//key = mt.getName() + sc.getName();
				if(mapTrace.get("onCreate"+cd.getFollower().getName())!=null && mapTrace.get(cd.getControlerMethod().getName()+cd.getControler().getName())!=null)//key = mt.getName() + sc.getName();
					{
						cd.setFound(true);//later we can use??? Hsu
						IaDataConDe.set(l, cd);
					}
			}
		}
		}catch(Exception e) {
			System.out.println("e=>"+e);
		}
		
		return input;

	}

	void printList(List<String> list, String outFile) throws IOException {
		System.out.println("Saving:" + list.size());
		FileUtils.writeLines(new File(outFile), list);
	}

	List<InstructionUnits> getInstructionUnits(List<Unit> listUnits, SootMethod sootMethod) {
		List<InstructionUnits> listIUs = new ArrayList<InstructionUnits>();
		for (Unit u : listUnits) {
			//System.out.println("u="+u.toString());
			InstructionUnits iu = new InstructionUnits();
			iu.setMethod(sootMethod);
			iu.setUnit(u);
			iu.setLineNo(-1);
			iu.setSootUnitId();
			listIUs.add(iu);
		}
		return listIUs;
	}
	/*
	 * backward dynamic slicing start
	 * */
	boolean getConDeBW(SootClass sc) {
		ConDe ret=null;
		for(ConDe cd: IaDataConDe) {
			if(cd.getFollower().equals(sc)) {
				ret=cd;
				currentBWCD = cd;
			}
		}
		return ret==null?true:false;
	}	
	
	boolean isLocalEndBW(InstructionUnits iu) {		
		MethodResult mer = new MethodResult(iu.getMethod().getName());
		mer.addIns(iu);
		ExceptionalUnitGraph ex = new ExceptionalUnitGraph(iu.getMethod().getActiveBody());
		//SimpleLocalDefs simpleLocalDefs = new SimpleLocalDefs(ex);
		List<Unit> units = new ArrayList<Unit>();
		List<ValueBox> useBoxes;
		useBoxes = iu.getUnit().getUseBoxes();
		List<ValueBox> tempUseBoxes = new ArrayList<ValueBox>();
		for (ValueBox vb : useBoxes) {
			tempUseBoxes.add(vb);
		}
		while (!tempUseBoxes.isEmpty()) {
			ValueBox vb = tempUseBoxes.remove(0);
			if (vb.getValue() instanceof Local) {
				Local local = (Local) vb.getValue();
				if (local instanceof Constant) {
					continue;
				}
				if (iu.getMethod().getActiveBody().getParameterLocals().contains(local)) {
					//System.out.println("ParamLocal="+iu.getMethod()+","+iu.getMethod().getDeclaringClass());
					//System.out.println("unit="+iu.getUnit());
					//System.out.println("local="+local);
					//System.out.println("def:"+simpleLocalDefs.getDefsOf(local));
					return false;
				}			
				
			}
		}
		return true;
	}
	
	MethodResult graphInMethodBW(InstructionUnits currentUI) {
		MethodResult mer = new MethodResult(currentUI.getMethod().getName());
			mer.addIns(currentUI);
			if(IaDataConDe!=null && IaDataConDe.size()>0 && currentBWCD ==null)	getConDeBW(currentUI.getMethod().getDeclaringClass());
			//System.out.println("currentBWCD="+currentBWCD);
				List<Unit> units = new ArrayList<Unit>();
				InfoflowCFG icfg = new InfoflowCFG();
				DirectedGraph<Unit> ug = icfg.getOrCreateUnitGraph(currentUI.getMethod());
		        Iterator<Unit> uit = ug.iterator();
		         while (uit.hasNext()) {
		        	 Unit u = uit.next();
		            units.add(u);
		            //System.out.println("---7-----");
		           // System.out.println("-----"+u);
		            /*if (u.branches()) {                
		                List<Unit> list = icfg.getSuccsOf(u);
		                System.out.println("list="+list);
		            }else if(icfg.isCallStmt(u)) {
		            	System.out.println("isCallStmt");
		            }else if(icfg.isReturnSite(u)) {
		            	System.out.println("isReturnSite");
		            }else if(icfg.isStartPoint(u)) {
		            	System.out.println("isStartPoint");
		            }*/
		        	}
		        mer.addInsList(getInstructionUnits(units, currentUI.getMethod()));	
		        
		      //test only started
		         ExceptionalUnitGraph ex = new ExceptionalUnitGraph(currentUI.getMethod().getActiveBody());
		 		SimpleLocalDefs simpleLocalDefs = new SimpleLocalDefs(ex);
		 		units = new ArrayList<Unit>();

		 		List<ValueBox> useBoxes;
		 		useBoxes = currentUI.getUnit().getUseBoxes();
		 		List<ValueBox> tempUseBoxes = new ArrayList<ValueBox>();
		 		for (ValueBox vb : useBoxes) {
		 			tempUseBoxes.add(vb);
		 		}

		 		// now for each usebox
		 		while (!tempUseBoxes.isEmpty()) {
		 			ValueBox vb = tempUseBoxes.remove(0);
		 			if (vb.getValue() instanceof Local) {
		 				Local local = (Local) vb.getValue();
		 				if (local instanceof Constant) {
		 					continue;
		 				}
		 				if (currentUI.getMethod().getActiveBody().getParameterLocals().contains(local)) {
		 					mer.setResult(false);
		 				}
		 				List<Unit> defUnits = simpleLocalDefs.getDefsOf(local);
		 				for (Unit u : defUnits) {
		 					if (!units.contains(u)) {
		 						units.add(u);
		 						for (ValueBox innerVb : u.getUseBoxes()) {
		 							tempUseBoxes.add(innerVb);
		 						}
		 					}

		 				}
		 			}
		 		}
				//test only ended
		 return mer;
	}

	void buildSliceBW(MethodResult mer, Map<String, InstructionUnits> dynamicSlice) {
		Map<String, InstructionUnits> staticSlice = new LinkedHashMap<String, InstructionUnits>();
		for (String key : mer.getMap().keySet()) {
			staticSlice.put(key, mer.getMap().get(key));
		}

		for (String key : dynamicSlice.keySet()) {
			try {
				if (staticSlice.containsKey("-1ZZZ" + key.split("ZZZ")[1])) {
					resultMapBW.put(key, dynamicSlice.get(key));
				}
			} catch (ArrayIndexOutOfBoundsException ax) {
				System.out.println("Array:" + key);
			}

		}

	}

	Map<String, InstructionUnits> getChunkBW(int pos, Input input) {
		InstructionUnits iu = input.mapKeyUnits.get(input.mapNoKey.get(pos));
		String currentMethod = iu.getMethod().getName();
		String currentClass = iu.getMethod().getDeclaringClass().toString();
		Map<String, InstructionUnits> chunk = new LinkedHashMap<String, InstructionUnits>();
		chunk.put(iu.getUnitId(), iu);//first unit
		int p = pos - 1;
		while (p >= 0) {
			iu = input.mapKeyUnits.get(input.mapNoKey.get(p));
			//System.out.println("iu="+iu);
			if (iu == null) {
				p--;
				continue;
			}
			//if (p > 4055 && p < 4061) {
				//iu = input.mapKeyUnits.get(input.mapNoKey.get(p));
			//}
			//System.out.println(currentClass);
			//System.out.println(iu.getUnit());
			if (iu != null && iu.getMethod().getName().equals(currentMethod)) {
				chunk.put(iu.getUnitId(), iu);
				currentBWP=p;
			} //else if(iu != null && iu.getUnit().toString().contains(currentMethod) && 
					//iu.getUnit().toString().contains(currentClass.split("\\$")[0])) {
				//System.out.println("here>>>>>>>>>>>>>"+iu.getUnit().toString());
				//chunk.put(iu.getUnitId(), iu);
				//currentBWP=p;
			//}			
			else {
				currentBWP=p;
				break;
			}
			p--;
		}
		//System.out.println(chunk);
		return chunk;
	}

	List<MethodResult> loadPDGBW(Input input, int previousP) {
		// Input input =loadTraces();
		List<MethodResult> listMer = new ArrayList<MethodResult>();
		String unitId=input.mapNoKey.get(previousP);
		InstructionUnits previousIU = input.mapKeyUnits.get(unitId);
		SootMethod methodNameToBring=previousIU.getMethod();		
		InstructionUnits currentIU = previousIU;
		//int position = input.mapKeyNo.get(previousIU);
		MethodResult mer = graphInMethodBW(currentIU);//getMethodResult(iu);	
		//System.out.println(mer.getMap());
		buildSliceBW(mer, getChunkBW(previousP, input));	
		listMer.add(mer);
		//currentP
	do {
		//System.out.println("currentBWP="+currentBWP);	
		unitId = input.mapNoKey.get(currentBWP);
		currentIU = input.mapKeyUnits.get(unitId);
		if(unitId==null || currentIU==null) {System.out.println("no line found!!!");currentBWP=currentBWP-1;continue;}
		//System.out.println("--1------------");
		if(previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0].equals(currentIU.getMethod().getDeclaringClass().getName().split("\\$")[0])){
			if(currentIU.getMethod().toString().contains(previousIU.getMethod().toString())) {methodNameToBring=currentIU.getMethod();}
			//System.out.println("methodNameToBring="+methodNameToBring);
			int tmpC=currentBWP;
			//System.out.println("--2------------"+currentBWP);
			//System.out.println("equal class"+previousIU.getMethod().getDeclaringClass()+","+currentIU.getMethod().getDeclaringClass());
			previousIU=currentIU;
			mer = graphInMethodBW(currentIU);
			buildSliceBW(mer, getChunkBW(currentBWP, input));	
			listMer.add(mer);
			//if(!isLocalEnd(currentIU))
			//{
				//mer = checkLocalLink(input,currentIU);
				//buildSlice(mer, getChunk(currentP, input));	
				//listMer.add(mer);
			//}
			if(currentBWP==tmpC) currentBWP=currentBWP-1;
			
			
		}
		else if(currentBWCD!=null)
		{
			//System.out.println("--3------------"+currentBWP);
			//System.out.println("controller="+currentBWCD.getControler().getName());
			//System.out.println("follwer="+currentBWCD.getFollower().getName());
			if(currentIU.getMethod().equals(currentBWCD.getControlerMethod()) && currentIU.getMethod().getDeclaringClass().equals(currentBWCD.getControler()))
			{
				//System.out.println("found controller="+currentBWCD.getControler().getName());
				int tmpC=currentBWP;
				currentBWCD=null;
				previousIU=currentIU;
				mer = graphInMethodBW(currentIU);
				buildSliceBW(mer, getChunkBW(currentBWP, input));	
				listMer.add(mer);
				//if(!isLocalEnd(currentIU))
				//{
					//mer = checkLocalLink(input,currentIU);
					//buildSlice(mer, getChunk(currentP, input));	
					//listMer.add(mer);
				//}
				if(currentBWP==tmpC) currentBWP=currentBWP-1;
			}else {
				currentBWP=currentBWP-1;
			}
		 }
		else if(currentIU.getUnit().toString().contains(previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0])) {
			//System.out.println("--4------------"+currentBWP);
			previousIU=currentIU;
			mer = graphInMethodBW(currentIU);
			buildSliceBW(mer, getChunkBW(currentBWP, input));	
			listMer.add(mer);
		}
		//System.out.println(currentIU.getMethod().toString());
		//System.out.println(methodNameToBring.toString());
		
		
		if (mer!=null && !mer.getResult()) {
			//System.out.println("-backward---5-----"+currentBWP);
			int tmpC=currentBWP;
			previousIU=currentIU;
			mer = checkLocalLinkBW(input,currentIU);
			if(mer!=null) buildSliceBW(mer, getChunkBW(currentBWP, input));	
			if(currentBWP==tmpC) currentBWP=currentBWP-1; 
			if(mer!=null) mer.setResult(true);
		}else if(currentIU.getMethod().toString().equals(methodNameToBring.toString())) {
			if(currentBWP<0) break;
			//System.out.println("--4.5------------"+currentBWP);
			previousIU=currentIU;
			mer = graphInMethodBW(currentIU);
			buildSliceBW(mer, getChunkBW(currentBWP, input));	
			listMer.add(mer);
		}
		else {
			//System.out.println("-backward---6-----"+currentBWP);
			int tmpC=currentBWP;
			previousIU=currentIU;
			mer = checkLocalLinkBW(input,currentIU);
			if(mer!=null) buildSliceBW(mer, getChunkBW(currentBWP, input));	
			if(currentBWP==tmpC) 
				currentBWP=currentBWP-1; 
		}
		//System.out.println("--5------------"+currentBWP);
		//if(currentBWP==21) break;
		/*{
			//System.out.println(currentIU.getUnit().getUseBoxes());
			/*List<ValueBox> useBoxes = currentIU.getUnit().getUseBoxes();
			boolean done=false;
			for (ValueBox vb : useBoxes) {
				if(vb instanceof InvokeExprBox && (vb.getValue() instanceof SpecialInvokeExpr)
				   && vb.getValue().toString().contains(previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0])) {
					System.out.println("currentIU>>>"+currentIU);
					System.out.println("previousIU>>>"+previousIU);
					previousIU=currentIU;
					mer = graphInMethod(currentIU);
					buildSlice(mer, getChunk(currentP, input));	
					listMer.add(mer);
					//vb.getValue().getUseBoxes()
					//System.out.println("her test..1.."+currentIU.getUnit());
					//System.out.println("her test..2.."+vb);
					//System.out.println("her test..3.."+vb.getValue().toString().contains(previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0]));
					//System.out.println("her test..4.."+(vb.getValue() instanceof SpecialInvokeExpr));
					//System.out.println("her test..5.."+vb.getValue().getUseBoxes());
					//System.out.println("her test..6.."+vb.getValue());
					//System.out.println("her test..7.."+vb.getTags());
					//System.out.println("her test..8.."+vb.getValue().toString());
					//System.out.println("her test..9.."+previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0]);
					//System.out.println("test"+"aa".split("\\$")[0]);
					done=true;
					break;
				}
			}
			//if(currentIU.getUnit() instanceof AssignStmt && ((AssignStmt)currentIU.getUnit()).getRightOp()!=null && ((Value)((AssignStmt)currentIU.getUnit()).getRightOp()) instanceof StaticInvokeExpr){
				//System.out.println("here>>>"+currentP+","+currentIU.getUnit());
			//}
			
		}	*/
		}while(currentBWP>=0);
		System.out.println("Done");
		return listMer;
	}
	
	MethodResult checkLocalLinkBW(Input input,InstructionUnits iu) {
		//System.out.println("checkLocalLink---");
		//System.out.println("In checkLocalLink currentP---"+currentBWP);
		//System.out.println("iu---"+iu.getUnit());
		MethodResult mer2=null;
		int position=currentBWP;
		String currentMethod = iu.getMethod().getName();
		String lastMethod = iu.getMethod().getName();
		position--;
		while (position >= 0) {
			if (position == 1683) {
				int kkr = 0;
			}
			String nextKey = input.mapNoKey.get(position);
			InstructionUnits nextUnit = input.mapKeyUnits.get(nextKey);
			if (nextUnit == null || nextUnit.getUnit() == null) {
				position--;
				continue;
			}
			Unit unit = nextUnit.getUnit();
			String invokedMethod = "";
			if (unit instanceof AssignStmt) {
				AssignStmt assighStmt = (AssignStmt) unit;
				Value v = assighStmt.getRightOp();

				if (v instanceof VirtualInvokeExpr) {
					invokedMethod = ((VirtualInvokeExpr) v).getMethod().getName();
				}
				if (v instanceof StaticInvokeExpr) {
					invokedMethod = ((StaticInvokeExpr) v).getMethod().getName();
				}

				else if (v instanceof SpecialInvokeExpr) {
					invokedMethod = ((SpecialInvokeExpr) v).getMethod().getName();
				}

				else if (v instanceof InvokeExpr) {
					invokedMethod = ((InvokeExpr) v).getMethod().getName();
				}
			}

			if (unit instanceof InvokeStmt || unit instanceof VirtualInvokeExpr || unit instanceof SpecialInvokeExpr
					|| unit instanceof StaticInvokeExpr || unit instanceof InvokeExpr) {
				currentMethod = nextUnit.getMethod().getName();

				if (unit instanceof InvokeStmt) {
					InvokeExpr iex = ((InvokeStmt) unit).getInvokeExpr();
					invokedMethod = iex.getMethod().getName();
				}

				if (unit instanceof VirtualInvokeExpr) {
					invokedMethod = ((VirtualInvokeExpr) unit).getMethod().getName();
				}

				if (unit instanceof StaticInvokeExpr) {
					invokedMethod = ((VirtualInvokeExpr) unit).getMethod().getName();
				}

				else if (unit instanceof SpecialInvokeExpr) {
					invokedMethod = ((SpecialInvokeExpr) unit).getMethod().getName();
				}

				else if (unit instanceof InvokeExpr) {
					invokedMethod = ((SpecialInvokeExpr) unit).getMethod().getName();
				}
			}

			if (!invokedMethod.equals("")) {

				if (invokedMethod.equals(lastMethod)) {
					mer2 = graphInMethodBW(nextUnit);
					//System.out.println("here>>>"+nextUnit.getUnit());
					currentBWP = position;
					return mer2;
				}
			}
			lastMethod = currentMethod;
			position--;
		}
		return mer2;
	
	}
	
	/*
	 * forward dynamic slicing start
	 * */
	
	boolean getConDeFW(SootClass sc, SootMethod mt) {
		//System.out.println("name="+sc.getName());
		//System.out.println("mt="+mt.getName());
		ConDe ret=null;
		for(ConDe cd: IaDataConDe) {
			//System.out.println(cd.getControler().getName());
			//System.out.println(cd.getControlerMethod().getName());
			if(cd.getControler().equals(sc) && cd.getControlerMethod().equals(mt)) {
				ret=cd;
				currentFWCD = cd;
			}
		}
		return ret==null?true:false;
	}
	boolean isLocalEndFW(InstructionUnits iu) {		
		MethodResult mer = new MethodResult(iu.getMethod().getName());
		mer.addIns(iu);
		ExceptionalUnitGraph ex = new ExceptionalUnitGraph(iu.getMethod().getActiveBody());
		//SimpleLocalDefs simpleLocalDefs = new SimpleLocalDefs(ex);
		List<Unit> units = new ArrayList<Unit>();
		List<ValueBox> useBoxes;
		useBoxes = iu.getUnit().getUseBoxes();
		List<ValueBox> tempUseBoxes = new ArrayList<ValueBox>();
		for (ValueBox vb : useBoxes) {
			tempUseBoxes.add(vb);
		}
		while (!tempUseBoxes.isEmpty()) {
			ValueBox vb = tempUseBoxes.remove(0);
			if (vb.getValue() instanceof Local) {
				Local local = (Local) vb.getValue();
				if (local instanceof Constant) {
					continue;
				}
				if (iu.getMethod().getActiveBody().getParameterLocals().contains(local)) {
					//System.out.println("ParamLocal="+iu.getMethod()+","+iu.getMethod().getDeclaringClass());
					//System.out.println("unit="+iu.getUnit());
					//System.out.println("local="+local);
					//System.out.println("def:"+simpleLocalDefs.getDefsOf(local));
					return false;
				}			
				
			}
		}
		return true;
	}
	
	MethodResult graphInMethodFW(InstructionUnits currentUI) {		
		MethodResult mer = new MethodResult(currentUI.getMethod().getName());
			mer.addIns(currentUI);
			if(currentFWCD ==null)	getConDeFW(currentUI.getMethod().getDeclaringClass(),currentUI.getMethod());
			//System.out.println("currentFWCD="+currentFWCD);
				List<Unit> units = new ArrayList<Unit>();
				InfoflowCFG icfg = new InfoflowCFG();
				DirectedGraph<Unit> ug = icfg.getOrCreateUnitGraph(currentUI.getMethod());
				Iterator<Unit> uit = ug.iterator();
		         while (uit.hasNext()) {
		        	 Unit u = uit.next();
		            units.add(u);
		            //System.out.println("---7-----");
		           // System.out.println("-----"+u);
		            /*if (u.branches()) {                
		                List<Unit> list = icfg.getSuccsOf(u);
		                System.out.println("list="+list);
		            }else if(icfg.isCallStmt(u)) {
		            	System.out.println("isCallStmt");
		            }else if(icfg.isReturnSite(u)) {
		            	System.out.println("isReturnSite");
		            }else if(icfg.isStartPoint(u)) {
		            	System.out.println("isStartPoint");
		            }*/
		        	}
		         mer.addInsList(getInstructionUnits(units, currentUI.getMethod()));	
				//test only started
		         ExceptionalUnitGraph ex = new ExceptionalUnitGraph(currentUI.getMethod().getActiveBody());
		 		SimpleLocalDefs simpleLocalDefs = new SimpleLocalDefs(ex);
		 		units = new ArrayList<Unit>();

		 		List<ValueBox> useBoxes;
		 		useBoxes = currentUI.getUnit().getUseBoxes();
		 		List<ValueBox> tempUseBoxes = new ArrayList<ValueBox>();
		 		for (ValueBox vb : useBoxes) {
		 			tempUseBoxes.add(vb);
		 		}

		 		// now for each usebox
		 		while (!tempUseBoxes.isEmpty()) {
		 			ValueBox vb = tempUseBoxes.remove(0);
		 			if (vb.getValue() instanceof Local) {
		 				Local local = (Local) vb.getValue();
		 				if (local instanceof Constant) {
		 					continue;
		 				}
		 				if (currentUI.getMethod().getActiveBody().getParameterLocals().contains(local)) {
		 					mer.setResult(false);
		 				}
		 				List<Unit> defUnits = simpleLocalDefs.getDefsOf(local);
		 				for (Unit u : defUnits) {
		 					if (!units.contains(u)) {
		 						units.add(u);
		 						for (ValueBox innerVb : u.getUseBoxes()) {
		 							tempUseBoxes.add(innerVb);
		 						}
		 					}

		 				}
		 			}
		 		}
				//test only ended
		        		        
		 return mer;
	}

	void buildSliceFW(MethodResult mer, Map<String, InstructionUnits> dynamicSlice) {
		Map<String, InstructionUnits> staticSlice = new LinkedHashMap<String, InstructionUnits>();
		for (String key : mer.getMap().keySet()) {
			staticSlice.put(key, mer.getMap().get(key));
		}

		for (String key : dynamicSlice.keySet()) {
			try {
				if (staticSlice.containsKey("-1ZZZ" + key.split("ZZZ")[1])) {
					resultMapFW.put(key, dynamicSlice.get(key));
				}
			} catch (ArrayIndexOutOfBoundsException ax) {
				System.out.println("Array:" + key);
			}

		}

	}

	Map<String, InstructionUnits> getChunkFW(int pos, Input input) {
		InstructionUnits iu = input.mapKeyUnits.get(input.mapNoKey.get(pos));
		String currentMethod = iu.getMethod().getName();
		Map<String, InstructionUnits> chunk = new LinkedHashMap<String, InstructionUnits>();
		chunk.put(iu.getUnitId(), iu);//first unit
		int p = pos + 1;
		while (p <= endP) {
			iu = input.mapKeyUnits.get(input.mapNoKey.get(p));
			if (iu == null) {
				p++;
				continue;
			}
			//if (p > 4055 && p < 4061) {
				//iu = input.mapKeyUnits.get(input.mapNoKey.get(p));
			//}

			if (iu != null && iu.getMethod().getName().equals(currentMethod)) {
				chunk.put(iu.getUnitId(), iu);
				currentFWP=p;
			} else {	
				//currentFWP=p;
				break;
			}
			p++;
		}
		
		return chunk;
	}

	List<MethodResult> loadPDGFW(Input input, int previousP) {
		// Input input =loadTraces();
		List<MethodResult> listMer = new ArrayList<MethodResult>();
		String unitId=input.mapNoKey.get(previousP);
		InstructionUnits previousIU = input.mapKeyUnits.get(unitId);
		InstructionUnits currentIU = previousIU;
		//int position = input.mapKeyNo.get(previousIU);
		MethodResult mer = graphInMethodFW(currentIU);//getMethodResult(iu);		
		buildSliceFW(mer, getChunkFW(previousP, input));	
		listMer.add(mer);
		//currentP
	do {
		//System.out.println("currentFWP="+currentFWP);	
		//System.out.println("previousIU="+previousIU.getUnit());
		System.out.println("currentFWP="+currentFWP);
		unitId = input.mapNoKey.get(currentFWP);
		currentIU = input.mapKeyUnits.get(unitId);
		System.out.println(currentIU!=null && currentIU.getUnit()!=null ? "currentIU==>"+currentIU.getUnit() : currentIU);
		System.out.println(previousIU!=null && previousIU.getUnit()!=null ? "previousIU==>"+previousIU.getUnit() : previousIU);
		//if(currentIU!=null) System.out.println("currentIU="+currentIU.getUnit());
		if(unitId==null || currentIU==null) {System.out.println("no line found!!!");currentFWP=currentFWP+1;continue;}
		if(previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0].equals(currentIU.getMethod().getDeclaringClass().getName().split("\\$")[0])){
			System.out.println("--1-----");
			//System.out.println("equal class"+previousIU.getMethod().getDeclaringClass()+","+currentIU.getMethod().getDeclaringClass());
			previousIU=currentIU;
			mer = graphInMethodFW(currentIU);
			int tmpC=currentFWP;
			buildSliceFW(mer, getChunkFW(currentFWP, input));	
			listMer.add(mer);
			//if(!isLocalEnd(currentIU))
			//{
				//mer = checkLocalLink(input,currentIU);
				//buildSlice(mer, getChunk(currentP, input));	
				//listMer.add(mer);
			//}
			if(currentFWP==tmpC) currentFWP=currentFWP+1;
		}
		else if(currentFWCD!=null)
		{
			
			System.out.println("controller="+currentFWCD.getControler().getName());
			System.out.println("follwer="+currentFWCD.getFollower().getName());
			if(currentIU.getMethod().getDeclaringClass().equals(currentFWCD.getFollower()))
			{
				//System.out.println("found follower="+currentFWCD.getFollower().getName());
				currentFWCD=null;
				previousIU=currentIU;
				mer = graphInMethodFW(currentIU);
				buildSliceFW(mer, getChunkFW(currentFWP, input));	
				listMer.add(mer);
				//if(!isLocalEnd(currentIU))
				//{
					//mer = checkLocalLink(input,currentIU);
					//buildSlice(mer, getChunk(currentP, input));	
					//listMer.add(mer);
				//}
			}else {
				currentFWP=currentFWP+1;
			}
		 }
		else if(previousIU.getUnit().toString().contains(currentIU.getMethod().getDeclaringClass().getName().split("\\$")[0])) {
			System.out.println("--3-----");
			System.out.println(previousIU!=null && previousIU.getUnit()!=null ? "previousIU==>"+previousIU.getUnit() : previousIU);
			System.out.println(currentIU!=null && currentIU.getUnit()!=null ? "currentIU==>"+currentIU.getUnit() : currentIU);
			previousIU=currentIU;
			int tmpC=currentFWP;
			mer = graphInMethodFW(currentIU);
			buildSliceFW(mer, getChunkFW(currentFWP, input));	
			listMer.add(mer);
			if(currentFWP==tmpC) currentFWP=currentFWP+1;
		}
		else if (!mer.getResult()) {
			System.out.println("--4-----");
			int tmpC=currentFWP;
			previousIU=currentIU;
			mer = checkLocalLinkFW(input,currentIU);
			if(mer!=null) buildSliceFW(mer, getChunkFW(currentFWP, input));	
			if(currentFWP==tmpC) currentFWP=currentFWP+1; 
			mer.setResult(true);
		}
		else {
			currentFWP=currentFWP+1;
		}
		/*{
			//System.out.println(currentIU.getUnit().getUseBoxes());
			/*List<ValueBox> useBoxes = currentIU.getUnit().getUseBoxes();
			boolean done=false;
			for (ValueBox vb : useBoxes) {
				if(vb instanceof InvokeExprBox && (vb.getValue() instanceof SpecialInvokeExpr)
				   && vb.getValue().toString().contains(previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0])) {
					System.out.println("currentIU>>>"+currentIU);
					System.out.println("previousIU>>>"+previousIU);
					previousIU=currentIU;
					mer = graphInMethod(currentIU);
					buildSlice(mer, getChunk(currentP, input));	
					listMer.add(mer);
					//vb.getValue().getUseBoxes()
					//System.out.println("her test..1.."+currentIU.getUnit());
					//System.out.println("her test..2.."+vb);
					//System.out.println("her test..3.."+vb.getValue().toString().contains(previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0]));
					//System.out.println("her test..4.."+(vb.getValue() instanceof SpecialInvokeExpr));
					//System.out.println("her test..5.."+vb.getValue().getUseBoxes());
					//System.out.println("her test..6.."+vb.getValue());
					//System.out.println("her test..7.."+vb.getTags());
					//System.out.println("her test..8.."+vb.getValue().toString());
					//System.out.println("her test..9.."+previousIU.getMethod().getDeclaringClass().getName().split("\\$")[0]);
					//System.out.println("test"+"aa".split("\\$")[0]);
					done=true;
					break;
				}
			}
			//if(currentIU.getUnit() instanceof AssignStmt && ((AssignStmt)currentIU.getUnit()).getRightOp()!=null && ((Value)((AssignStmt)currentIU.getUnit()).getRightOp()) instanceof StaticInvokeExpr){
				//System.out.println("here>>>"+currentP+","+currentIU.getUnit());
			//}
			
		}	*/
		}while(currentFWP<=endP);
		System.out.println("Done");
		return listMer;
	}
	
	//i dun know what is that? Hsu
	MethodResult checkLocalLinkFW(Input input,InstructionUnits iu) {
		System.out.println("checkLocalLink---");
		System.out.println("In checkLocalLink currentP---"+currentFWP);
		System.out.println("iu---"+iu.getUnit());
		MethodResult mer2=null;
		int position=currentFWP;
		String currentMethod = iu.getMethod().getName();
		String lastMethod = iu.getMethod().getName();
		position++;
		while (position <= endP) {
			//if (position == 1683) {
				//int kkr = 0;
			//}
			String nextKey = input.mapNoKey.get(position);
			InstructionUnits nextUnit = input.mapKeyUnits.get(nextKey);
			if (nextUnit == null || nextUnit.getUnit() == null) {
				position++;
				continue;
			}
			Unit unit = nextUnit.getUnit();
			String invokedMethod = "";
			if (unit instanceof AssignStmt) {
				AssignStmt assighStmt = (AssignStmt) unit;
				Value v = assighStmt.getRightOp();

				if (v instanceof VirtualInvokeExpr) {
					invokedMethod = ((VirtualInvokeExpr) v).getMethod().getName();
				}
				if (v instanceof StaticInvokeExpr) {
					invokedMethod = ((StaticInvokeExpr) v).getMethod().getName();
				}

				else if (v instanceof SpecialInvokeExpr) {
					invokedMethod = ((SpecialInvokeExpr) v).getMethod().getName();
				}

				else if (v instanceof InvokeExpr) {
					invokedMethod = ((InvokeExpr) v).getMethod().getName();
				}
			}

			if (unit instanceof InvokeStmt || unit instanceof VirtualInvokeExpr || unit instanceof SpecialInvokeExpr
					|| unit instanceof StaticInvokeExpr || unit instanceof InvokeExpr) {
				currentMethod = nextUnit.getMethod().getName();

				if (unit instanceof InvokeStmt) {
					InvokeExpr iex = ((InvokeStmt) unit).getInvokeExpr();
					invokedMethod = iex.getMethod().getName();
				}

				if (unit instanceof VirtualInvokeExpr) {
					invokedMethod = ((VirtualInvokeExpr) unit).getMethod().getName();
				}

				if (unit instanceof StaticInvokeExpr) {
					invokedMethod = ((VirtualInvokeExpr) unit).getMethod().getName();
				}

				else if (unit instanceof SpecialInvokeExpr) {
					invokedMethod = ((SpecialInvokeExpr) unit).getMethod().getName();
				}

				else if (unit instanceof InvokeExpr) {
					invokedMethod = ((SpecialInvokeExpr) unit).getMethod().getName();
				}
			}

			if (!invokedMethod.equals("")) {

				if (invokedMethod.equals(lastMethod)) {
					mer2 = graphInMethodFW(nextUnit);
					System.out.println("here>>>"+nextUnit.getUnit());
					currentFWP = position;
					return mer2;
				}
			}
			lastMethod = currentMethod;
			position++;
		}
		return mer2;
	
	}

}
