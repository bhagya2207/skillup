package pack2;
import java.util.*;
public class Switch {
	public static void main(String[] args) {
		Scanner obj = new Scanner(System.in);
		System.out.println("Enter any two numbers:");
		int a = obj.nextInt();
		int b = obj.nextInt();
		System.out.println("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division");
		int ch = obj.nextInt();
		switch(ch)
		{
		case 1:System.out.println("Addition is "+(a+b));
		break;
		case 2:System.out.println("Subtraction is"+(a-b));
		break;
		case 3:System.out.println("Multipilication is"+(a*b));
		break;
		case 4:System.out.println("Division is"+(a/b));
		break;
		default:System.out.println("Invalid Choice");
		}
	}

}
