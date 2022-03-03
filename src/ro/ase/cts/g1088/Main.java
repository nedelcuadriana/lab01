package ro.ase.cts.g1088;

import java.util.Locale;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
//        System.out.println("Testare");
        Scanner sc = new Scanner(System.in);
        System.out.println("Introduceti fraza: ");
        String str = sc.nextLine();

        try{
            if(str.toLowerCase() == str) {
                throw new ExceptieAllLower();
            }
            if(str.toUpperCase() == str) {
                throw new ExceptieAllUpper();
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

        System.out.println("Ati introdus: " + str);
    }
}
