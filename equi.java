package pack2;
import java.util.*;
public class equi {
	public static void main(String[] args) {
		Scanner obj = new Scanner(System.in);
		System.out.println("Enter side of triangle: ");
		double a = obj.nextDouble();
		double area = (Math.sqrt(3)/(4)*(a*a));
		System.out.println("Area of Triangle"+area);
	}
}
