package pack3;
class Student
{
	String name;
	int roll;
	
	Student(String name, int roll)
	{
		this.name=name;
		this.roll= roll;
	}
	public void printStudent()
	{
		System.out.println("name :"+name);
		System.out.println("roll :"+roll);
	}
}
public class Constructor 
{
	public static void main(String[] args)
	{
	Student obj = new Student("bhagya",22);
	obj.printStudent();

	}

}
