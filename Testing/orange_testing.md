# 🍊 Orange Compiler Tests

The inputs in this folder are made to test the Orange Compiler, it's features and it's caveats. An input file might focus on one or more specific features of the Orange Language, and they must be stated in this file. The input files must state their expected output (Success or Fail) to determine if the compiler is working correctly.

## Features to test
- Lowercase and uppercase usage
- Creating a program without \<program\> reserved word
- Variable Declaration
    - Declare a variable
    - Declare multiple variables with commas
    - No variable type mixing
- Function names can't be the same as variable names and viceversa

## Tests
These input files must be designed with tests in mind before the compiler is finished. Each input file must state in itself what its testing as a comment in the Orange Language as well.

### Input_1