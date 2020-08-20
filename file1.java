package pack3;
class A1  // composition or sub class
{
	public void sum(int x , int y)
	{
		System.out.println("sum = " + (x+y));
	}
}
public class file1  // Aggregation or main class 
{
	public static void main(String[] args) 
	{
	 A1 obj = new A1();
	 obj.sum(20,10);
	 System.out.println("Main class");
	}
}
