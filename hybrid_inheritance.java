package pack3;
class Student4
{
	String name;
	int rollno;
	Student4(String name,int rn)
	{
		this.name=name;
		rollno=rn;
	}
	void Display()
	{
		System.out.println("name="+name+ "rollno="+rollno);
	}
}
class Marks3 extends Student4
{
	int m1,m2;
	Marks3(String name,int rn,int m1,int m2)
	{
		super(name,rn);
		this.m1=m1;
		this.m2=m2;
	}
	void Display1()
	{
		System.out.println("m1="+m1+"m2="+m2);
	}
}
class Marks4 extends Marks3
{
	int m3,m4;
	Marks4(String name,int rn,int m1,int m2,int m3,int m4)
	{
		super(name,rn,m1,m2);
		this.m3 =m3;
		this.m4 =m4;
	}
	void Display2()
	{
		System.out.println("m3="+m3+"m4="+m4);
	}
}
class Result extends Student4
{
	int total,avg;
	Result(String name,int rn,int total,int avg)
	{
		super(name,rn);
		this.total=total;
		this.avg=avg;
	}
	void Display4()
	{
		System.out.println("total="+total+"avg="+avg);
	}
}
public class hybrid_inheritance {
	public static void main(String[] args) {
Marks4 obj = new Marks4("anu",22,32,43,54,76);
obj.Display();
obj.Display1();
obj.Display2();
Result obj2=new Result("anu",22,567,73);
obj2.Display4();
	}}

