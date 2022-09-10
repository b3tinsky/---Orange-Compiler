# 🍊 Orange Compiler™
The Orange Compiler™ is a simple compiler used alongside the Orange Language™ to teach the inner workings of a compiler in a simple and enjoyable manner. It has a small hint of data analysis as an added bonus.

# 📝 Checkpoints
Checkpoints are given by our professor, although they can change during the semester and they are more like 'symbolic' checkpoints to help us complete the project. These checkpoints represent the core components of the compiler. It is strongly recommended to follow the order of the checkpoints since they follow the class syllabus and the compiler is built in a secuential manner (cannot skip to a further component without finishing previous ones).

### ✅ Checkpoint \#0
- ~~Project proposal~~
- ~~Token list~~
- ~~Syntax diagrams~~

### ✅ Checkpoint \#1: Lexical and Syntactical Analysis

### ✅ Checkpoint \#2: Basic variable semantics
- ~~Procedure directory~~
- ~~Variable table~~

### ⚠️ Checkpoint \#3: Expression semantics
- Semantic cube
- Code generation for arithmetic expressions and secuential statutes
    - Assignment
    - Read
    - Write
    - Etc.

### ❌ Checkpoint \#4: Code generation for conditional statutes
- Decisions
- Cycles

### ❌ Checkpoint \#5: Code generation for functions

### ❌ Checkpoint \#6: Memory map for virtual machine
- Execution of arithmetic expressions
- Secuential statutes

### ❌ Checkpoint \#7: Code generation for arrays and structured types
- Execution of conditional statutes

### ❌ Checkpoint \#8: First version of documentation
- For a specific section
    - Code generation
    - Virtual machine

# 🗒️ Log

### 📆 August 23 🕓 23:13
Created repository. Started planning and design. Started checkpoint #0.

### 📆 August 26 🕓 17:22
Made list with tokens.

### 📆 August 29 🕓 19:03
Finished checkpoint #0 (proposal, token list and syntax diagrams). Things can still be changed or added, depending on teacher's feedback (more special functions, more structured types, etc).

### 📆 August 30 🕓 20:22
Designing and documenting test for the Orange Compiler. 

### 📆 September 01 🕓 15:29
Minor changes to syntax diagrams and proposal document. Added first input files to testing folder.

### 📆 September 02 🕓 23:16
Finished first version of parser. Instead of staying with PLY, I gave SLY a go. I felt that it has a little bit better syntax, and in the worst case scenario, I don't think its that complicated to change it to PLY again. I finished the parser based on the LittleDuck homework, and my proposal's syntax diagrams. As I was making the parser, I noticed several areas where problems my arise (reduction conflicts, redundance, etc.), but this version only serves as a backup while I keep working on fixing said issues. Also, I still don't know why Git/Github is not signing my commits.

### 📆 September 05 🕓 17:10
Solved a reduce/reduce conflict with the block contents. I have a slight suspicion that the same issue might happen again with other rules, but the fix is very simple.
For the block contents I had the rules:

blockcontents -> statute | statute blockcontents | empty

And all I did was remove the 'statute' rule. It fixes the conflict because now if there is only one statute in the block, it can exit through the empty rule, instead of having to decide.

I think this will happen again because I have a vague memory of doing something similar in other rules, but I believe those problems will become easily visible if I keep making more tests to poke at the grammar rules.

### 📆 September 05 🕓 19:35
Watched recorded class (September 20) where the teacher talks about semantics. This recording was needed to begin writing basic variable semantics and the development of a procedure directory and a variable table.

### 📆 September 06 🕓 16:48
Watched recorded class (September 23) where the teacher talks about semantics and focuses more on development and refinement of the function directory/variable table. Started development of function directory and variable table components. 

### 📆 September 09 🕓 23:38
Main program now accepts arguments to run/test the scanner, the parser, or both. Finished an implementation for function directory and variable table. When the parser enters a new function, I added a rule BEFORE the current rule ends where the current context is switched. This means that for a rule like < MAIN LPAREN RPAREN block > I added the rule < MAIN changecontext LPAREN RPAREN block > so that the context changes for everything inside the main block and not everything after it. The implementation works by creating an object for the function directory and an object for the variable table. When the parser passes through a new context, the variable table is cleared. All the variables declared in said context are added to the variable table, and then the whole variable table is added to the current function/context in the function directory. I also added some tags to identify important parts in the project. I still to make sure everything is working correctly with the function directory and the variable tables, but for now its good progress. In later commits, I want to add more testing input files. I also want to implement a testing framework (pytest or unittest) or maybe develop my own testing, but that will depend on which I find more convenient. I should also refine my testing document (add more testing points, design tests, document more, etc.).
 
# Tags
TODO:    Tasks to be done
HACK:    Neat ideas to solve problems or cool ideas
FIXME:   It works, but not always (could break or not tested)
BUG:     It doesn't work
WARNING: Could potentially have problems
DOC:     Documentation pending for this section