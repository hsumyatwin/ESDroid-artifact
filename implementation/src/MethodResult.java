import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class MethodResult {
		Map <String, InstructionUnits> mapInstUnits;
		boolean isEnd;
		private String methodName;
		//boolean linkMethod;
		boolean isComingFromSecondCase;
		private boolean foundGlobalVariable=false;
		private String className;
		
		
		MethodResult(String methodName)
		{
			mapInstUnits = new LinkedHashMap();
			isEnd =true;
			this.setMethodName(methodName);
		}
		
		MethodResult(String methodName,String className)
		{
			mapInstUnits = new LinkedHashMap();
			isEnd =true;
			this.setMethodName(methodName);
			this.setClassName(className);
		}
		
		Map <String, InstructionUnits> getMap()
		{
			return mapInstUnits;
		}
		boolean getResult()
		{
			return isEnd;
		}
		
		void setResult(boolean result)
		{
			isEnd = result;
		}
		void addInsList(List <InstructionUnits> listIUs)
		{
			for(InstructionUnits iu: listIUs)
			{
				mapInstUnits.put(iu.getUnitId(), iu);
			}
			
		}
		void addIns(InstructionUnits iu)
		{
			if(!iu.getMethod().getName().equals(""))
			{
				if(mapInstUnits.get(iu.getUnitId())==null)
				{
					
					mapInstUnits.put(iu.getUnitId(), iu);
					
				}
				else
				{
					mapInstUnits.put(iu.getUnitId(), iu);
				}
			}
		}

		/*public boolean isLinkMethod() {
			return linkMethod;
		}

		public void setLinkMethod(boolean linkMethod) {
			this.linkMethod = linkMethod;
		}*/

		public boolean isComingFromSecondCase() {
			return isComingFromSecondCase;
		}

		public void setComingFromSecondCase(boolean isComingFromSecondCase) {
			this.isComingFromSecondCase = isComingFromSecondCase;
		}

		public boolean isFoundGlobalVariable() {
			return foundGlobalVariable;
		}

		public void setFoundGlobalVariable(boolean foundGlobalVariable) {
			this.foundGlobalVariable = foundGlobalVariable;
		}

		public String getMethodName() {
			return methodName;
		}

		public void setMethodName(String methodName) {
			this.methodName = methodName;
		}

		public String getClassName() {
			return className;
		}

		public void setClassName(String className) {
			this.className = className;
		}

}
