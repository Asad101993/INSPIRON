public class PrintAsciivalue {
public static void main(String[] args) {
char ch = 'H';
int ascii = ch;
// You can also cast char to int
int castAscii = (int) ch;
System.out.println("The ASCII value of " + ch + " is: " + ascii);
System.out.println("The ASCII value of " + ch + " is: " + castAscii);
}
}