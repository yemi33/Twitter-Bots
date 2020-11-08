from engine import GrammarEngine

def component5a():
    engine = GrammarEngine(file_path="grammars/c5a_grammar.txt")
    
    for i in range(5):
      output = engine.generate(start_symbol_name="origin", debug=False) 
      output_list = output.split('\\n')
      for j in range (len(output_list)):
        print(f"{output_list[j]}")

def component5b():
    engine1 = GrammarEngine(file_path="grammars/c5b_grammar.txt")
    
    for i in range(5):
      output = engine1.generate(start_symbol_name="forest", debug=False)
      output_list = output.split('\\n')
      for j in range (len(output_list)):
        print(f"{output_list[j]}")
      print("")

def component5c():
    engine = GrammarEngine(file_path="grammars/c5c_grammar.txt")
    
    for i in range(5):
      output = engine.generate(start_symbol_name="origin", debug=False) 
      output_list = output.split('\\n')
      for j in range (len(output_list)):
        print(f"{output_list[j]}")
      print("")


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 5a -- ")
    component5a()
    print("\n\n-- Component 5b -- ")
    component5b()
    print("\n\n-- Component 5c -- ")
    component5c()