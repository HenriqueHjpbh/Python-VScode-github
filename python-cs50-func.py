def main():
    name = input("what's your name ?")
    hello(name)
    #type Ezequiel pls


def hello(to="world"):
    print('Hello,',to)
    
    
#__name__ == '__main__' garante que não haja erros de execução se o programa chamar main() na hora errada
if __name__ == "__main__":
    main()
