package pack3;
class Student3
{
	String name;
	int rollno;
	Student3(String name,int rn)
	{
		this.name=name;
		rollno=rn;
	}
	void Display()
	{
		System.out.println("name ="+name+"roll no ="+rollno);
	}
}
class Marks3 extends Student3
{
	int m1,m2;
	Marks3(String name,int rn,int m1,int m2)
	{
		super (name,rn);
		this.m1=m1;
		this.m2=m2;
	}
	void Display1()
	{
		System.out.println("m1 ="+m1+"m2="+m2);
	}
}
class Marks4 extends Marks3
{
	int m3,m4;
	Marks4(String name,int rn,int m1,int m2,int m3,int m4)
	{
		super(name,rn,m1,m2);
		this.m3=m3;
		this.m4=m4;
	}
	void Display2()
	{
		System.out.println("m3="+m3+"m4="+m4);
	}
}
public class multilevel_inheritance {
	public static void main(String[] args) {
Marks4 obj = new Marks4("anu",22,23,34,45,67);
obj.Display();
obj.Display1();
obj.Display2();
	}
}
