def stack_operation(self, operation):
   if operation == "push":
      input_value = input("Enter value to push into stack:")
      self.push(item=self.pop())
   elif operation == "pop":
      return self.pop()
