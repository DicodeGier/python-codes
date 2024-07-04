NAME 
ROWS
 N  OBJ
 E  R0      
 L  R1      
 L  R2      
 L  R3      
 L  R4      
 L  R5      
 L  R6      
 L  R7      
COLUMNS
    MARKER    'MARKER'                 'INTORG'
    delivery[Monday]  OBJ       -10
    delivery[Monday]  R0        1
    delivery[Monday]  R1        1
    delivery[Tuesday]  OBJ       -30
    delivery[Tuesday]  R0        1
    delivery[Tuesday]  R2        1
    delivery[Wednesday]  OBJ       -50
    delivery[Wednesday]  R0        1
    delivery[Wednesday]  R3        1
    delivery[Thursday]  OBJ       -90
    delivery[Thursday]  R0        1
    delivery[Thursday]  R4        1
    delivery[Friday]  OBJ       -180
    delivery[Friday]  R0        1
    delivery[Friday]  R5        1
    delivery[Saturday]  OBJ       -100
    delivery[Saturday]  R0        1
    delivery[Saturday]  R6        1
    delivery[Sunday]  OBJ       -60
    delivery[Sunday]  R0        1
    delivery[Sunday]  R7        1
    trucks[Monday]  OBJ       300
    trucks[Monday]  R1        -100
    trucks[Tuesday]  OBJ       300
    trucks[Tuesday]  R2        -100
    trucks[Wednesday]  OBJ       300
    trucks[Wednesday]  R3        -100
    trucks[Thursday]  OBJ       300
    trucks[Thursday]  R4        -100
    trucks[Friday]  OBJ       300
    trucks[Friday]  R5        -100
    trucks[Saturday]  OBJ       300
    trucks[Saturday]  R6        -100
    trucks[Sunday]  OBJ       300
    trucks[Sunday]  R7        -100
    MARKER    'MARKER'                 'INTEND'
RHS
    RHS1      OBJ       -72000
    RHS1      R0        1300
BOUNDS
 LI BND1      delivery[Monday]  0
 LI BND1      delivery[Tuesday]  0
 LI BND1      delivery[Wednesday]  0
 LI BND1      delivery[Thursday]  0
 LI BND1      delivery[Friday]  0
 LI BND1      delivery[Saturday]  0
 LI BND1      delivery[Sunday]  0
 LI BND1      trucks[Monday]  0
 LI BND1      trucks[Tuesday]  0
 LI BND1      trucks[Wednesday]  0
 LI BND1      trucks[Thursday]  0
 LI BND1      trucks[Friday]  0
 LI BND1      trucks[Saturday]  0
 LI BND1      trucks[Sunday]  0
QUADOBJ
    delivery[Monday]  delivery[Monday]  0.4
    delivery[Tuesday]  delivery[Tuesday]  0.4
    delivery[Wednesday]  delivery[Wednesday]  0.4
    delivery[Thursday]  delivery[Thursday]  0.4
    delivery[Friday]  delivery[Friday]  0.4
    delivery[Saturday]  delivery[Saturday]  0.4
    delivery[Sunday]  delivery[Sunday]  0.4
ENDATA
