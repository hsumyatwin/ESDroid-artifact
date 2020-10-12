import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class FLiADDmin3 {

	//static String packageName="net.androidcomics.acv/net.robotmedia.acv.ui.ComicViewerActivity";
	static String minFSoE="0.py";
	static ArrayList<String> header=new ArrayList<String>();
	static String logFile="logerr.txt";
    static Process mProcess;

    static LocalTime now;
    static LocalTime previous;
    static Duration duration;
    static List<Duration> durations = new ArrayList<>();
    
    static String exceptionType="RuntimeException";
    static String className="MainActivity";
    static int lineNumber=54;
    
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		previous = LocalTime.now();
		produceFSoE(minFSoE);
		now = LocalTime.now();
		duration = Duration.between(previous, now);
		durations.add(duration);
		
		Duration sum = Duration.ZERO;
	    for (Duration dur : durations) {
	        sum = sum.plus(dur);
	    }

	    System.out.println(sum);
		//runScript("test.py");
	}
	
	public static void produceFSoE(String fileName) {
		String line;
		int i=0;
		List<ArrayList<String>> tmp = new ArrayList<ArrayList<String>>();
		List<Integer> tmpInt = new ArrayList<Integer>();
		
		ArrayList<String> tmpArr=new ArrayList<String>();
		try (FileReader reader = new FileReader(fileName);
			     BufferedReader br = new BufferedReader(reader))
				{
	    		while ((line = br.readLine()) != null) 
	            {
	    			i+=1;
	    			if(i<22) {
	    				header.add(line);
	    				continue;
	    			}  			
	    			if(line.contains("MonkeyRunner.sleep")) {	    				
	    				if(tmpArr.size()>0) {
	    					tmp.add(tmpArr);
	    					tmpInt.add(tmp.size()-1);
	    				}	    				
	    				tmpArr = new ArrayList<String>();
	    				tmpArr.add(line);
	    			}else {
	    				tmpArr.add(line);
	    			}
	            }
				} catch (IOException e) {
					System.err.format("IOException: %s%n", e);
				}
			System.out.println(tmp.size());
			//System.out.println(tmp);
			int cnt=0;
			int n=2;
			while(tmpInt.size() >= 2)
			{
				List<List<Integer>> subsets = split(tmpInt,n);
				//System.out.println("subsets="+subsets.size());
				boolean complementFailing = false;
				for(List<Integer> subset : subsets){
					//System.out.println("subset data="+subset);
					List<Integer> complement = difference(tmpInt, subset);
					//System.out.println("complement="+complement);
					//print complement and run
					 cnt+=1;
					String runF=writeMonekyScriptToRun(tmp,complement,cnt);
					//get input data to continue
					// Using Console to input data from user
					Scanner scan = new Scanner(System.in);
					
					//time duration
					now = LocalTime.now();
					duration = Duration.between(previous, now);
					durations.add(duration);
					
					System.out.print("Emulator Ready For Run!!!!");
					previous = LocalTime.now();
				    scan.nextLine();
			        //if(name.equals("F")) {
					runScript(runF);	
					
					now = LocalTime.now();
					duration = Duration.between(previous, now);
					durations.add(duration);
					
					System.out.print("Script Run Finished!!!! Ready to read Log?");
					previous = LocalTime.now();
				    scan.nextLine();
			        if(findException()) {
			        	System.out.println("FSoE="+runF);
			        	tmpInt = complement;
						n = Math.max(n - 1, 2);
						complementFailing = true;
						break;
					}			       
				}

			        if (!complementFailing) {
						if (n == tmpInt.size()) {
							break;
						}
						// increase set granularity
						n = Math.min(n * 2, tmpInt.size());
						//System.out.println("increase grandularity???"+n);
						
			        }
				}
	}
	

  private static void runScript(String file){
    Process process;
	    try{
	         // process = Runtime.getRuntime().exec(new String[]{file,"arg1","arg2"});
	          process = Runtime.getRuntime().exec("\\AppData\\Local\\Android\\Sdk\\tools\\monkeyrunner.bat "+file);
	          mProcess = process;
	    }catch(Exception e) {
	       System.out.println("Exception Raised" + e.toString());
	    }
	    InputStream stdout = mProcess.getInputStream();
	    BufferedReader reader = new BufferedReader(new InputStreamReader(stdout,StandardCharsets.UTF_8));
	    String line;
	    try{
	       while((line = reader.readLine()) != null){
	            //System.out.println("stdout: "+ line);
	       }
	    }catch(IOException e){
	          System.out.println("Exception in reading output"+ e.toString());
	    }
  	}
	
	private static boolean findException() {
		String line="";
		boolean fEx=false;
		boolean fC=false;
		try (FileReader reader = new FileReader(logFile);
		     BufferedReader br = new BufferedReader(reader))
			{
	    		while ((line = br.readLine()) != null) 
	            {
	    			if(line!=null && line.contains(exceptionType)) {
	    				fEx=true;
	    			}
	    			if(line !=null && line.contains(className) && line.contains(""+lineNumber)) {
	    				fC=true;
	    			}
	            }
			} catch (IOException e) {
		System.err.format("IOException: %s%n", e);
		}
		return fEx && fC;	}
	
	private static List<List<Integer>> split(List<Integer> s, int n) {
		List<List<Integer>> subsets = new LinkedList<List<Integer>>();
		int position = 0;
		for (int i = 0; i < n; i++) {
			List<Integer> subset = s.subList(position, position + (s.size() - position) / (n - i));
			subsets.add(subset);
			position += subset.size();
		}
		return subsets;
	}
	
	private static List<Integer> difference(List<Integer> a, List<Integer> b) {
		List<Integer> result = new LinkedList<Integer>();
		result.addAll(a);
		result.removeAll(b);
		return result;
	}
	
	private static String writeMonekyScriptToRun(List<ArrayList<String>> tmp,List<Integer> tmpCnt,int cnt) {
    	try
    	{
    	PrintWriter writer = new PrintWriter(cnt+".py", "UTF-8");
    	 //writer.println("echo %date:~4,2%-%date:~7,2% %time%");
         //writer.println("adb shell am start -n "+packageName+" a");
         //writer.println("adb shell sleep 5 ");
    	for(String s:header) {
    		writer.println(s);
    	}
         for(Integer s:tmpCnt) {
        	 for(String st: tmp.get(s)){
            	 writer.println(st);
         	     //writer.println("sleep 3");
        	 }
     	      
         }  
        //writer.print("echo %date:~4,2%-%date:~7,2% %time%");
        writer.close();
    	}catch(Exception e) {e.printStackTrace();}
    		
        return cnt+".py";
    }

}