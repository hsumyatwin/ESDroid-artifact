import soot.SootClass;
import soot.SootMethod;

public class ConDe {
	ConDe(){}
	ConDe(SootClass cntr,SootMethod cntrM,SootClass flwr,Boolean bb){
		setControler(cntr);
		setControlerMethod(cntrM);
		setFollower(flwr);
		setFound(bb);
	}
	private SootClass controler;
	private SootClass follower;
	private Boolean found;
	private SootMethod controlerMethod;
	
	public Boolean getFound() {
		return found;
	}
	public void setFound(Boolean found) {
		this.found = found;
	}
	public SootClass getControler() {
		return controler;
	}
	public void setControler(SootClass controler) {
		this.controler = controler;
	}
	public SootClass getFollower() {
		return follower;
	}
	public void setFollower(SootClass follower) {
		this.follower = follower;
	}
	public SootMethod getControlerMethod() {
		return controlerMethod;
	}
	public void setControlerMethod(SootMethod controlerMethod) {
		this.controlerMethod = controlerMethod;
	}
	

}
