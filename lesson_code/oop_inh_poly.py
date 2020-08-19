# UI -> User Interface

class Label():
    def __init__(self, text):
        self.text = text
    
    def __str__(self):
        return f"\n#{self.text:^30}#\n"



class EmphasedLabel(Label):
    
    # OVERRIDING
    
    def __str__(self):
        return "\n" + "#"*32 + super().__str__().upper() + "#"*32 + "\n"


main_label = Label("Hello OOP!")
emp_label = EmphasedLabel("Another Label!!!")
print(main_label)
print(emp_label)