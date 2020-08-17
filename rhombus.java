package pack2;
import java.util.*;
public class rhombus {
	public static void main(String[] args) {
		Scanner obj = new Scanner(System.in);
		System.out.println("Enter Diagonal 1: ");
		double d1 = obj.nextDouble();
		System.out.println("Enter Diagonal 2: ");
		double d2 = obj.nextDouble();
		double area = (d1*d2)/2;
		System.out.println("Area of Rhombus "+area);
	}
}
