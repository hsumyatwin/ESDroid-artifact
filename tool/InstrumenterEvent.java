import java.util.Iterator;
import java.util.Map;

import soot.Body;
import soot.BodyTransformer;
import soot.Local;
import soot.PackManager;
import soot.PatchingChain;
import soot.RefType;
import soot.Scene;
import soot.SootClass;
import soot.SootMethod;
import soot.Transform;
import soot.Unit;
import soot.jimple.AbstractStmtSwitch;
import soot.jimple.AssignStmt;
import soot.jimple.DefinitionStmt;
import soot.jimple.IfStmt;
import soot.jimple.InvokeStmt;
import soot.jimple.Jimple;
import soot.jimple.LookupSwitchStmt;
import soot.jimple.Stmt;
import soot.jimple.StringConstant;
import soot.jimple.SwitchStmt;
import soot.jimple.infoflow.android.SetupApplication;
import soot.jimple.infoflow.android.config.SootConfigForAndroid;
import soot.options.Options;

public class InstrumenterEvent {
	
	public static void main(String[] args) {
		String domainName="com.muledog.calculator";
		Options.v().set_src_prec(Options.src_prec_apk);		
		//output as APK, too//-f J
		Options.v().set_output_format(Options.output_format_dex);
		Options.v().force_android_jar();
        // resolve the PrintStream and System soot-classes
		Scene.v().addBasicClass("java.io.PrintStream",SootClass.SIGNATURES);
        Scene.v().addBasicClass("java.lang.System",SootClass.SIGNATURES);

        PackManager.v().getPack("jtp").add(new Transform("jtp.myInstrumenter", new BodyTransformer() {

			@Override
			protected void internalTransform(final Body b, String phaseName, @SuppressWarnings("rawtypes") Map options) {
				//System.out.println("#################"+Options.v().process_multiple_dex());
				SootClass sc = b.getMethod().getDeclaringClass();
				SootMethod sm = b.getMethod();	
				final PatchingChain<Unit> units = b.getUnits();
				if(b.getMethod().getName().startsWith("on") && b.getMethod().getDeclaringClass().getName().contains(domainName)) {isEvent=true;eventCnt+=1;}
				else isEvent=false;
				for(Iterator<Unit> iter = units.snapshotIterator(); iter.hasNext();) {
					final Unit u = iter.next();
					 cls = sc;
				     mtd = sm;
					u.apply(new AbstractStmtSwitch() {
						public void caseInvokeStmt(InvokeStmt stmt) {
							//InvokeExpr invokeExpr = stmt.getInvokeExpr();
							//if(invokeExpr.getMethod().getName().equals("onDraw")){}
								Local tmpRef = addTmpRef(b);
								Local tmpString = addTmpString(b);
								String payload = getPayload(u, cls, mtd);	
								if(isEvent)
			            		{
			            			payload = "EVENTID_"+eventCnt+": " + payload;
			            			isEvent = false;
			            		}
								  // insert "tmpRef = java.lang.System.out;" 
							    units.insertBefore(Jimple.v().newAssignStmt( 
							              tmpRef, Jimple.v().newStaticFieldRef( 
							              Scene.v().getField("<java.lang.System: java.io.PrintStream out>").makeRef())), u);

							    // insert "tmpLong = 'HELLO';" 
							    units.insertBefore(Jimple.v().newAssignStmt(tmpString, 
							                  StringConstant.v(payload)), u);

							    // insert "tmpRef.println(tmpString);" 
							    SootMethod toCall = Scene.v().getSootClass("java.io.PrintStream").getMethod("void println(java.lang.String)");                    
							    units.insertBefore(Jimple.v().newInvokeStmt(
							                  Jimple.v().newVirtualInvokeExpr(tmpRef, toCall.makeRef(), tmpString)), u);

							    //check that we did not mess up the Jimple
							    b.validate();
						}
						public void caseAssignStmt(AssignStmt stmt)
						{
							//InvokeExpr invokeExpr = stmt.getInvokeExpr();
							//if(invokeExpr.getMethod().getName().equals("onDraw")){}
								Local tmpRef = addTmpRef(b);
								Local tmpString = addTmpString(b);
								String payload = getPayload(u, cls, mtd);	
								if(isEvent)
			            		{
									payload = "EVENTID_"+eventCnt+": " + payload;
			            			isEvent = false;
			            		}
								  // insert "tmpRef = java.lang.System.out;" 
							    units.insertBefore(Jimple.v().newAssignStmt( 
							              tmpRef, Jimple.v().newStaticFieldRef( 
							              Scene.v().getField("<java.lang.System: java.io.PrintStream out>").makeRef())), u);

							    // insert "tmpLong = 'HELLO';" 
							    units.insertBefore(Jimple.v().newAssignStmt(tmpString, 
							                  StringConstant.v(payload)), u);

							    // insert "tmpRef.println(tmpString);" 
							    SootMethod toCall = Scene.v().getSootClass("java.io.PrintStream").getMethod("void println(java.lang.String)");                    
							    units.insertBefore(Jimple.v().newInvokeStmt(
							                  Jimple.v().newVirtualInvokeExpr(tmpRef, toCall.makeRef(), tmpString)), u);

							    //check that we did not mess up the Jimple
							    b.validate();
						}
			            	
						
						public void caseDefinitionStmt(DefinitionStmt stmt)
						{
							//InvokeExpr invokeExpr = stmt.getInvokeExpr();
							//if(invokeExpr.getMethod().getName().equals("onDraw")){}
								Local tmpRef = addTmpRef(b);
								Local tmpString = addTmpString(b);
								String payload = getPayload(u, cls, mtd);	
								if(isEvent)
			            		{
									payload = "EVENTID_"+eventCnt+": " + payload;
			            			isEvent = false;
			            		}
								  // insert "tmpRef = java.lang.System.out;" 
							    units.insertBefore(Jimple.v().newAssignStmt( 
							              tmpRef, Jimple.v().newStaticFieldRef( 
							              Scene.v().getField("<java.lang.System: java.io.PrintStream out>").makeRef())), u);

							    // insert "tmpLong = 'HELLO';" 
							    units.insertBefore(Jimple.v().newAssignStmt(tmpString, 
							                  StringConstant.v(payload)), u);

							    // insert "tmpRef.println(tmpString);" 
							    SootMethod toCall = Scene.v().getSootClass("java.io.PrintStream").getMethod("void println(java.lang.String)");                    
							    units.insertBefore(Jimple.v().newInvokeStmt(
							                  Jimple.v().newVirtualInvokeExpr(tmpRef, toCall.makeRef(), tmpString)), u);

							    //check that we did not mess up the Jimple
							    b.validate();
						}
						
						public void caseLookupSwitchStmt(LookupSwitchStmt stmt)
						{
							//InvokeExpr invokeExpr = stmt.getInvokeExpr();
							//if(invokeExpr.getMethod().getName().equals("onDraw")){}
								Local tmpRef = addTmpRef(b);
								Local tmpString = addTmpString(b);
								String payload = getPayload(u, cls, mtd);
								if(isEvent)
			            		{
									payload = "EVENTID_"+eventCnt+": " + payload;
			            			isEvent = false;
			            		}
								  // insert "tmpRef = java.lang.System.out;" 
							    units.insertBefore(Jimple.v().newAssignStmt( 
							              tmpRef, Jimple.v().newStaticFieldRef( 
							              Scene.v().getField("<java.lang.System: java.io.PrintStream out>").makeRef())), u);

							    // insert "tmpLong = 'HELLO';" 
							    units.insertBefore(Jimple.v().newAssignStmt(tmpString, 
							                  StringConstant.v(payload)), u);

							    // insert "tmpRef.println(tmpString);" 
							    SootMethod toCall = Scene.v().getSootClass("java.io.PrintStream").getMethod("void println(java.lang.String)");                    
							    units.insertBefore(Jimple.v().newInvokeStmt(
							                  Jimple.v().newVirtualInvokeExpr(tmpRef, toCall.makeRef(), tmpString)), u);

							    //check that we did not mess up the Jimple
							    b.validate();
						}
						public void caseSwitchStmt(SwitchStmt stmt)
						{
							//InvokeExpr invokeExpr = stmt.getInvokeExpr();
							//if(invokeExpr.getMethod().getName().equals("onDraw")){}
								Local tmpRef = addTmpRef(b);
								Local tmpString = addTmpString(b);
								String payload = getPayload(u, cls, mtd);	
								if(isEvent)
			            		{
									payload = "EVENTID_"+eventCnt+": " + payload;
			            			isEvent = false;
			            		}
								  // insert "tmpRef = java.lang.System.out;" 
							    units.insertBefore(Jimple.v().newAssignStmt( 
							              tmpRef, Jimple.v().newStaticFieldRef( 
							              Scene.v().getField("<java.lang.System: java.io.PrintStream out>").makeRef())), u);

							    // insert "tmpLong = 'HELLO';" 
							    units.insertBefore(Jimple.v().newAssignStmt(tmpString, 
							                  StringConstant.v(payload)), u);

							    // insert "tmpRef.println(tmpString);" 
							    SootMethod toCall = Scene.v().getSootClass("java.io.PrintStream").getMethod("void println(java.lang.String)");                    
							    units.insertBefore(Jimple.v().newInvokeStmt(
							                  Jimple.v().newVirtualInvokeExpr(tmpRef, toCall.makeRef(), tmpString)), u);

							    //check that we did not mess up the Jimple
							    b.validate();
						}
						public void caseIfStmt(IfStmt stmt)
						{
							//InvokeExpr invokeExpr = stmt.getInvokeExpr();
							//if(invokeExpr.getMethod().getName().equals("onDraw")){}
								Local tmpRef = addTmpRef(b);
								Local tmpString = addTmpString(b);
								String payload = getPayload(u, cls, mtd);	
								if(isEvent)
			            		{
									payload = "EVENTID_"+eventCnt+": " + payload;
			            			isEvent = false;
			            		}
								  // insert "tmpRef = java.lang.System.out;" 
							    units.insertBefore(Jimple.v().newAssignStmt( 
							              tmpRef, Jimple.v().newStaticFieldRef( 
							              Scene.v().getField("<java.lang.System: java.io.PrintStream out>").makeRef())), u);

							    // insert "tmpLong = 'HELLO';" 
							    units.insertBefore(Jimple.v().newAssignStmt(tmpString, 
							                  StringConstant.v(payload)), u);

							    // insert "tmpRef.println(tmpString);" 
							    SootMethod toCall = Scene.v().getSootClass("java.io.PrintStream").getMethod("void println(java.lang.String)");                    
							    units.insertBefore(Jimple.v().newInvokeStmt(
							                  Jimple.v().newVirtualInvokeExpr(tmpRef, toCall.makeRef(), tmpString)), u);

							    //check that we did not mess up the Jimple
							    b.validate();
						}
						
						public void caseStmt(Stmt stmt)
						{
							//InvokeExpr invokeExpr = stmt.getInvokeExpr();
							//if(invokeExpr.getMethod().getName().equals("onDraw")){}
								Local tmpRef = addTmpRef(b);
								Local tmpString = addTmpString(b);
								String payload = getPayload(u, cls, mtd);	
								if(isEvent)
			            		{
									payload = "EVENTID_"+eventCnt+": " + payload;
			            			isEvent = false;
			            		}
								  // insert "tmpRef = java.lang.System.out;" 
							    units.insertBefore(Jimple.v().newAssignStmt( 
							              tmpRef, Jimple.v().newStaticFieldRef( 
							              Scene.v().getField("<java.lang.System: java.io.PrintStream out>").makeRef())), u);

							    // insert "tmpLong = 'HELLO';" 
							    units.insertBefore(Jimple.v().newAssignStmt(tmpString, 
							                  StringConstant.v(payload)), u);

							    // insert "tmpRef.println(tmpString);" 
							    SootMethod toCall = Scene.v().getSootClass("java.io.PrintStream").getMethod("void println(java.lang.String)");                    
							    units.insertBefore(Jimple.v().newInvokeStmt(
							                  Jimple.v().newVirtualInvokeExpr(tmpRef, toCall.makeRef(), tmpString)), u);

							    //check that we did not mess up the Jimple
							    b.validate();
						}		            	
						
					});
				}
			}


		}));
		soot.Main.main(args);
		//Options.v().set_process_multiple_dex(true);
		//System.out.println("**************"+Options.v().process_multiple_dex());
		
		/*SetupApplication setupApplication = new SetupApplication("jarPath","apkPath");
        
		SootConfigForAndroid sootConf = new SootConfigForAndroid() {
		            @Override
		            public void setSootOptions(Options options) {
		                // we need to specify soot options here since FlowDroid resets them
		                super.setSootOptions(options);
		                options.set_process_multiple_dex(true);
		            }
		};
		setupApplication.setSootConfig(sootConf);*/
		
	}

    private static Local addTmpRef(Body body)
    {
        Local tmpRef = Jimple.v().newLocal("tmpRef", RefType.v("java.io.PrintStream"));
        body.getLocals().add(tmpRef);
        return tmpRef;
    }
    
    private static Local addTmpString(Body body)
    {
        Local tmpString = Jimple.v().newLocal("tmpString", RefType.v("java.lang.String")); 
        body.getLocals().add(tmpString);
        return tmpString;
    }
    
    static String getPayload(Unit u, SootClass sc, SootMethod sm)
	{
		String header = u.getJavaSourceStartLineNumber() +"ZZZ"+ sc.getName() + "ZZZ" + sm.getName();
		String tag = "FLiAD: ";
		String typeStr = "__inst__";
		
		/*switch(type)
		{
			case DIRECTOR:
				typeStr = "__director__";
				break;
			case HEAD:
				typeStr = "__head__";
				break;
			case TAIL:
				typeStr = "__tail__";
				break;
			case INST:
				typeStr = "__inst__";
				break;
			default:
				break;
		}*/
		return tag+"ZZZ" + header + "ZZZ" + typeStr+"ZZZ" + u.toString();
	}
    static SootClass cls ;
   	static SootMethod  mtd ;
   	static boolean isEvent = false;
   	static int eventCnt=0;
}
