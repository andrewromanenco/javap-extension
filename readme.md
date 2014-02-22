Javap extension script
======================

 **javap** is java class file disassembler from opendjk
 
 Running it as *javap -c SomeClass.class* prints all byte code operations. **javapx** extends javap output with byte codes for each operation name.
 
 Reads input from **stdin**, sends output to **stdout**.
 
 e.g.

    public static void main(java.lang.String[]);
        Code:
           0: getstatic     #3
           3: ldc           #4
           5: invokevirtual #5
           8: return 

 Run as:
 **javap -c Test.class|python javapx.py**

    public static void main(java.lang.String[]);
        Code:
            0 :  getstatic (b2)      #3
            3 :  ldc (12)            #4
            5 :  invokevirtual (b6)  #5
            8 :  return (b1)  

All op codes copied from wikipedia: http://en.wikipedia.org/wiki/Java_bytecode_instruction_listings