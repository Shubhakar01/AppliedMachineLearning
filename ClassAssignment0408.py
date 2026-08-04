#5
class Game:
    def __init__(self, name, genre, platform):
        self.name = name
        self.genre = genre
        self.platform = platform

    def print_details(self):
        print(f'{self.name} is a {self.genre} game available on {self.platform} platform.')

class Program:
    def lambda_function(self):
        #Q1
        odd_numbers = filter(lambda x:x%2!=0,range(1,200))
        print(list(odd_numbers))
        #Q2
        three_parameters = lambda x,y,z:x+y
        print(three_parameters(12,23,34))
        #Q3
        greatest_number = lambda x,y,z:max(x,y,z)
        print(greatest_number(12,23,34))

    def mapping_function(self):
        #Q4
        example_list = [1,2,3,4,5]
        double_list = list(map(lambda x:x*2,example_list))
        print(double_list)
    #Q6
    def list_comprehension_function(self):
        example_list = [(12,23),(45,56,67),(78,89,90,10)]
        length_list  = [len(x) for x in example_list]
        print(length_list)

def main():
    game1 = Game('Spider-Man 2', 'Action-Adventure', 'PlayStation 5')
    game1.print_details()
    game2 =Game('Assetto Corsa', 'Racing', 'PC')
    game2.print_details()

    program = Program()
    program.lambda_function()
    program.mapping_function()
    program.list_comprehension_function()

main()