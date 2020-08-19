# UI -> User Interface


class Label():
    n = 60

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"\n#{self.text:^{self.n}}#\n"


class EmphasedLabel(Label):

    # OVERRIDING

    def __str__(self):
        self.n = Label.n
        nx = "#"*(Label.n + 2)
        return "\n" + nx + super().__str__().upper() + nx + "\n"


main_label = Label("Hello OOP!")
emp_label = EmphasedLabel("Another Label!!!")
print(main_label)
print(emp_label)
