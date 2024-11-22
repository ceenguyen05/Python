from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight , AKnave) ,  # either a knight or knave
    Not(And(AKnight , AKnave)) , # cant be a knight and a knave
    Implication(AKnight , And(AKnight , AKnave)) , # if A is a knight , then A is both a Knight and A Knave
    Implication(AKnave , Not(And(AKnight , AKnave))) # If A is a knave , then cant be both
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight , AKnave) ,  # A is either a knight or knave
    Not(And(AKnight , AKnave)) , # A cant be a knight and a knave
    Or(BKnight , BKnave) ,  # B either a knight or knave
    Not(And(BKnight , BKnave)) , # B cant be a knight and a knave
    Implication(AKnight , And(AKnave , BKnave)) , # If A is a knight , then A and B are both Knaves
    Implication(AKnave , Not(And(AKnave , BKnave))) # If A is a knave , then A and B are both not knaves
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight , AKnave) ,  # A is either a knight or knave
    Not(And(AKnight , AKnave)) , # A cant be a knight and a knave
    Or(BKnight , BKnave) ,  # B either a knight or knave
    Not(And(BKnight , BKnave)) , # B cant be a knight and a knave
    Implication(AKnight , Or(And(AKnight , BKnight) , And(AKnave , BKnave))) , # If a is a knight , then A and B are knights or knaves
    Implication(AKnave , Or(And(AKnave , BKnight) , And(AKnight , BKnave))) , # If a is a knave , then A and B are not knights or knaves
    Implication(BKnight , Or(And(AKnave , BKnight) , And(AKnight , BKnave))) , # if B is a knight , they are not the same kind
    Implication(BKnave , Or(And(AKnight , BKnight) , And(AKnave , BKnave))) # if B is a Knave , they are of same kinds

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Basic Rules
    Or(AKnight , AKnave) ,
    Not(And(AKnight , AKnave)) ,
    Or(BKnight , BKnave) ,
    Not(And(BKnight , BKnave)) ,
    Or(CKnight , CKnave) ,
    Not(And(CKnight , CKnave)) ,
    Implication(AKnight , Or(AKnight , AKnave)) , # if he is a knight , he is either a knight or a knave is true
    Implication(AKnave , And(AKnight , AKnave)) , # if he is a knave , then he is both a knight and a knave
    Implication(BKnight , AKnave) , # if B is a knight , then A is a knave
    Implication(BKnave , AKnight) , # if B is a knave , then A is a knight
    Implication(BKnight , CKnave) , # if B is a knight , C must be a knave
    Implication(BKnave , CKnight) , # if B is a knave , C is a knight
    Implication(CKnight , AKnight) , # if C is a knight then A is a knight
    Implication(CKnave , AKnave) # if C is a knave , then A is a knave 
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
