class student:
    def check_pass_fail(self,mark):
        if self.mark < 50:
            print("failed")
        else: print("passed")

student1 = student()
student1.mark(12)
print(student1.mark)