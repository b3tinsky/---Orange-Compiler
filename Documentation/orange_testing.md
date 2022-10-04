# 🍊 Orange Compiler Tests

The inputs in this folder are made to test the Orange Compiler, it's features and it's caveats. An input file might focus on one or more specific features of the Orange Language, and they must be stated in this file. The input files must state their expected output (Success or Fail) to determine if the compiler is working correctly. 

The PYTEST Framework is used for automatic testing. The directory structure is organized in the following way:

Testing
- Inputs
    - Input file 01
    - Input file 02
    - Input file 03
- Tests
    - Pytest test 01
    - Pytest test 02
    - Pytest test 03

The inputs are source code for the Orange Language and the tests are classes with functions as individual tests for each input file.

In my case, I'm using VS Code's built in testing section for Python, but in case a user without VS Code or the built in testing section wants to see the test results, pytest must be installed and imported in a separate entry file to run the tests.

Input 00 is a "temporary" input file I used during development, and the main purpose was to see immediate results to changes in the compiler, hence why there are no tests for input 00 (constantly changing the file would require constant changes to the tests as well). 

## Features to test
- Global Declaration Block
    - [ ] Variable block [ ] Function Block
    - [x] Variable block [ ] Function Block
    - [ ] Variable block [x] Function Block
    - [x] Variable block [x] Function Block
- Lowercase and uppercase usage
- Creating a program without \<program\> reserved word
- Having variables the same name as the program name
- Having functions with the same name as the program name
- Variable Declaration
    - Single line variable declaration
    - Single line with commas variable declaration
    - Multi line variable declaration
    - Multi type variable declaration
    - Vars keyword without variables declared
- Function names can't be the same as variable names and viceversa

## Tests
These input files must be designed with tests in mind before the compiler is finished. Each input file must state in itself what its testing as a comment in the Orange Language as well.

### Input_01
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '❌'
In the global variable declaration block, one of the variables has the name '0'. This should be ok for the scanner, but not the parser, since a 0 is a valid token (CTEINT), but during a declaration, an ID was expected.

### Input_02
__Expected LEX status__:    '❌'
__Expected SYNTAX status__: '❌'
In the global variable declaration, an illegal character is given ('!'). This should not be accepted by the scanner, and by consequence the parser should also have an error status.

### Input_03
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
- Program WITHOUT global variable declaration block
- Program WITHOUT function declaration block

### Input_04
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEMANTIC status__: '✅'
- Program WITH global variable declaration block
- Program WITHOUT function declaration block

### Input_05
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
- Program WITHOUT global variable declaration block
- Program WITH function declaration block

### Input_06
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
- Program WITH global variable declaration block
- Program WITH function declaration block

### Input_07
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '❌'
Two functions have the same name, which is not allowed in the Orange Language. This feature is valid in other languages, since the user can declare functions with the same name, but different amount of parameters. That is beyond the scope of this language, hence why only unique function names are allowed.

### Input_08
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Local variable names CAN be repeated in the global scope.

### Input_09
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '❌'
Local variable names CAN NOT be repeated in the same scope.

### Input_10
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Variables can have the same name as their scope and other function names as long as they're not reserved words (for example a variable can't be called 'main').

### Input_11
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '❌'
__Expected SEM status__: '✅'
Variables CANT be identified as a reserved word. For example: vars int main; 

### Input_12
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Functions using undeclared local vars, but global vars exist

### Input_13
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '❌'
Functions using undeclared local vars, but global vars dont exist

### Input_14
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Main using undeclared local vars, but global vars exist

### Input_15
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '❌'
Main using undeclared local vars, but global vars dont exist

### Input_16
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '❌'
Main using local vars, but requested var exists in function

### Input_17
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Precedence, associativity and order of operations should be correct when generating quadruples for arithmetic expressions. In this case the operation uses sums, substractions, division, multiplication, parenthesis, and also a relation.

### Input_18
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Precedence, associativity and order of operations should be correct when generating quadruples for arithmetic expressions. In this case the operation uses sums, substractions, division, multiplication, parenthesis, and also a relation.

### Input_19
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
While testing arithemtic operations, also test print statements, input statements and constant variables. The goal of this test is focused on quadruple generation (correct quadruples, correct order, etc.)

### Input_20
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Single conditional statement must generate correct quadruples in the correct order. The focus of this test is on the "jumps" a conditional statement creates. In this case it only accounts for a single IF statement.

### Input_21
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Single conditional statement must generate correct quadruples in the correct order. The focus of this test is on the "jumps" a conditional statement creates. In this case it accounts for an  IF statement with an ELSE clause.

### Input_22
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Single conditional statement must generate correct quadruples in the correct order. The focus of this test is on the "jumps" a conditional statement creates. In this case it accounts for an  IF statement with nested IF statements and an ELSE clause.

### Input_23
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
While loop must generate correct quadruples in the correct order. This test focuses on the GOTOF and GOTO a while loop must generate.

### Input_24
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
Do while loop must generate correct quadruples in the correct order. This test focuses on the GOTOT, GOTOF and GOTO a do while loop must generate. It also has nested conditions, while and do-while loops.

### Input_25
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '❌'
Arithmetic expressions must be of correct type. For example: An integer and a boolean should result in an error.

### Input_26
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '❌'
Relational expressions must be of correct type. For example: An integer and a boolean should result in an error.

### Input_27
__Expected LEX status__:    '✅'
__Expected SYNTAX status__: '✅'
__Expected SEM status__: '✅'
IF statement inside a FOR LOOP. Quadruples must be created correctly and its jumps must be in the correct order.