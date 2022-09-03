# 🍊 Orange Compiler™
The Orange Compiler™ is a simple compiler used alongside the Orange Language™ to teach the inner workings of a compiler in a simple and enjoyable manner. It has a small hint of data analysis as an added bonus.

# 📝 Checkpoints
Checkpoints are given by our professor, although they can change during the semester and they are more like 'symbolic' checkpoints to help us complete the project. These checkpoints represent the core components of the compiler. It is strongly recommended to follow the order of the checkpoints since they follow the class syllabus and the compiler is built in a secuential manner (cannot skip to a further component without finishing previous ones).

### ✅ Checkpoint \#0
- ~~Project proposal~~
- ~~Token list~~
- ~~Syntax diagrams~~

### ✅ Checkpoint \#1: Lexical and Syntactical Analysis

### ⚠️ Checkpoint \#2: Basic variable semantics
- Procedure directory
- Variable table

### ❌ Checkpoint \#3: Expression semantics
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

