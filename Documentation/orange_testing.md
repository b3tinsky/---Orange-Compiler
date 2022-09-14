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
    - [] Variable block [] Function Block
    - [x] Variable block [] Function Block
    - [] Variable block [x] Function Block
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