class Person:
    institute = 'Manipal School of Information Sciences'
    def set_name(self, new_name):
        self.name = new_name
    def set_location(self, new_location):
        self.location = new_location
    def print_details(self):
        # print(f'{self.name} lives in {self.location} and studies at Institute: {self.institute}')
        print('{} lives in {} and studies at Institute: {}'.format(self.name, self.location, self.institute))

person1=Person()
person1.set_name('Shubhakar')
person1.set_location('Manipal, Udupi, Karnataka')
person1.print_details()

person2=Person()
person2.set_name('Ujwal')
person2.set_location('Manipal, Udupi, Karnataka')
person2.print_details()

