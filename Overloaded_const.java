package pack3;
class Bank
{
	String name;
	int acc_no;
	Bank() //constructor with no arguments
	{
		name = "Bhagya";
		acc_no = 22;
	}
	Bank(String name) //constructor with 1 argument
	{
		this.name=name;
		acc_no=22;
	}
	Bank(String name,int acc_no)  //constructor with 2 arguments
	{
		this.name= name;
		this.acc_no=acc_no;
	}
	void Show()
	{
		System.out.println("name :"+name);
		System.out.println("Account number : "+acc_no);
	}
}
public class Overloaded_const {
	public static void main(String[] args)
	{
		//Bank obj1 = new Bank();
		//obj1.Show();
		Bank obj2 = new Bank("Bhagya");
		obj2.Show();
		Bank obj3 = new Bank("sri",14);
		obj3.Show();
	}
}
