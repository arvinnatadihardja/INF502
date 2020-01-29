/*

Desired Output:

Input statements (in JOptionPane) must be as follows:

"Enter number of mols"
"Enter temperature (K)"
"Enter volume (N/m^2)"


|====================================|
|     Value Name     |     Value     |
|--------------------|---------------|
| Number of mols     =        123.67 |
|--------------------|---------------|
| Temperature        =        456.23 |
|--------------------|---------------|
| Volume             =       8952.11 |
|--------------------|---------------|
| Pressure (Result)  =         52.40 |
|====================================|

|====================================|
|     Value Name     |     Value     |
|--------------------|---------------|
| Number of mols     =        123.67 |
|--------------------|---------------|
| Temperature        =        456.23 |
|--------------------|---------------|
| Volume             =       8952.11 |
|--------------------|---------------|
| Pressure (Result)  =         52.40 |
|====================================|


Provided Code:
*/

package package_2;
import java.util.Scanner;

public class IdealGasLawClass
   {
    private static final char ENDLINE_CHAR = '\n';
    private static final char SPACE = ' ';
    
    public static void main(String[] args)
    {
        // declare variables
        double numberOfMols, temp, volume;
        String numberOfMolsStr, tempStr, volumeStr;
        double gasConstant = 8.314;
        // get input from user
        System.out.print("Enter number of mols: ");
        numberOfMolsStr = new Scanner(System.in).next();
        System.out.print("Enter temperature (K): ");
        tempStr = new Scanner(System.in).next();
        System.out.print("Enter volume (N/m^2): ");
        volumeStr = new Scanner(System.in).next();
        
        
        // translate to double values
        numberOfMols = Double.parseDouble(numberOfMolsStr);
        temp = Double.parseDouble(tempStr);
        volume = Double.parseDouble(volumeStr);
        // calculate results
        
        // find numerator
        double numerator = numberOfMols*temp*gasConstant;
        // find pressure
        double pressure = numerator/volume;
        // display results

        // Display top/title line
        System.out.println("|====================================|");
        printChars(1, '|');
        printCenterJustifiedString("Value Name", 20);
        printChars(1, '|');
        printCenterJustifiedString("Value", 15);
        printChars(1, '|');
        printEndLine();
        System.out.println("|--------------------|---------------|");
        // display number of moles line
        printChars(1, '|');
        printLeftJustifiedString(" Number of mols", 20);
        printChars(1, '=');
        printRightJustifiedDouble(numberOfMols,2, 14);
        printChars(1, ' ');
        printChars(1, '|');
        printEndLine();
        System.out.println("|--------------------|---------------|");
        // display temperature line
         // display number of moles line
        printChars(1, '|');
        printLeftJustifiedString(" Temperature", 20);
        printChars(1, '=');
        printRightJustifiedDouble(temp,2, 14);
        printChars(1, ' ');
        printChars(1, '|');
        printEndLine();
        System.out.println("|--------------------|---------------|");
        // display volume line
         // display number of moles line
        printChars(1, '|');
        printLeftJustifiedString(" Volume", 20);
        printChars(1, '=');
        printRightJustifiedDouble(volume,2, 14);
        printChars(1, ' ');
        printChars(1, '|');
        printEndLine();
        System.out.println("|--------------------|---------------|");
        // display pressure line
         // display number of moles line
        printChars(1, '|');
        printLeftJustifiedString(" Pressure (Result)", 20);
        printChars(1, '=');
        printRightJustifiedDouble(pressure,2, 14);
        printChars(1, ' ');
        printChars(1, '|');
        printEndLine();
        System.out.println("|====================================|");
         }

// Supporting Methods - DO NOT MAKE ANY CHANGES TO THESE METHODS ///////////////

    public static void printEndLine()
       {
        System.out.print( ENDLINE_CHAR );
       }
          
    public static void printChars( int numChars, char outChar )
       {
        if( numChars > 0 )
           {
            printChars( numChars - 1, outChar );
                
            System.out.print( outChar );
           }
       }     
      
    public static void printCenterJustifiedString( String outString, 
                                                                 int blockSize )
       {
        int preSpaces = blockSize / 2 - outString.length() / 2;
        int postSpaces = blockSize - preSpaces - outString.length();
        
        printChars( preSpaces, SPACE );
        System.out.print( outString );
        printChars( postSpaces, SPACE );
       }
    
    public static void printLeftJustifiedString( String outString, 
                                                                 int blockSize )
       {
        int postSpaces = blockSize - outString.length();
        
        System.out.print( outString );
        printChars( postSpaces, SPACE );
       }

    public static void printRightJustifiedString( String outString, 
                                                                 int blockSize )
       {
        int preSpaces = blockSize - outString.length();
        
        printChars( preSpaces, SPACE );
        System.out.print( outString );
       }

    public static void printCenterJustifiedDouble( double outVal, 
                                                  int precision, int blockSize )
       {
        String outStr = setPrecision( outVal, precision );

        printCenterJustifiedString( outStr, blockSize );
       }

    public static void printLeftJustifiedDouble( double outVal, 
                                                  int precision, int blockSize )
       {
        String outStr = setPrecision( outVal, precision );

        printLeftJustifiedString( outStr, blockSize );
       }

    public static void printRightJustifiedDouble( double outVal, 
                                                  int precision, int blockSize )
       {
        String outStr = setPrecision( outVal, precision );
        
        printRightJustifiedString( outStr, blockSize );
       }
     
    public static String setPrecision( double outVal, int precision )
       {
        int tempPrecision = precision + 1;
        int wkgIntVal, outValInt = (int)outVal;
        double outValFraction = Math.abs( outVal - outValInt );
        String outValStr = "";
        
        while( tempPrecision > 1 )
           {
            outValFraction *= 10;
            
            wkgIntVal = (int)outValFraction;
            
            outValStr += wkgIntVal;
            
            outValFraction -= wkgIntVal;
            
            tempPrecision--;
           }

        outValFraction *= 100;
        
        if( outValFraction > 45 )
           {
            wkgIntVal = Integer.parseInt( outValStr ) + 1;
            
            outValStr = Integer.toString( wkgIntVal );
           }
        
        outValStr = Integer.toString( outValInt ) + "." + outValStr;
        
        return outValStr;
       }


   }