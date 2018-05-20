public class api{
    public static void main(String[] args) {
        String str = "Welcome to Beginnersbook";
        String reversed = reverseString(str);
        System.out.println("The reversed string is: " + reversed);
    }
    public static String reverseString(String str) {
        if (str.isEmpty())
            return str;
        //Calling Function Recursively
        return reverseString(str.substring(1)) + str.charAt(0);
    }
}

public class database{
   public static void main(String[] args) {
      int num1 = 5, num2 = 15, sum;
      sum = num1 + num2;
      System.out.println("Sum of these numbers: "+sum);
   }
}

class sensor {
    void calculateArea(float x) {
        System.out.println("Area of the square: "+x*x+" sq units");
    }
    void calculateArea(float x, float y) {
        System.out.println("Area of the rectangle: "+x*y+" sq units");
    }
    void calculateArea(double r) {
        double area = 3.14*r*r;
        System.out.println("Area of the circle: "+area+" sq units");
    }
    public static void main(String args[]) {
        JavaExample obj = new JavaExample();
        /* This statement will call the first area() method
         * because we are passing only one argument with
         * the "f" suffix. f is used to denote the float numbers
         *
         */
	 obj.calculateArea(6.1f);
	 /* This will call the second method because we are passing
	  * two arguments and only second method has two arguments
	  */
	 obj.calculateArea(10,22);
	 /* This will call the second method because we have not suffixed
	  * the value with "f" when we do not suffix a float value with f
	  * then it is considered as type double.
	  */
	 obj.calculateArea(6.1);
    }
}
