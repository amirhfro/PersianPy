if __name__ == '__main__':
    lexer = BasicLexer()
    parser = BasicParser()
    print('GFG Language')
    env = {}
      
    while True:
          
        try:
            text = input('GFG Language > ')
          
        except EOFError:
            break
          
        if text:
            tree = parser.parse(lexer.tokenize(text))
            BasicExecute(tree, env)