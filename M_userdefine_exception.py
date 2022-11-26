class InputValidationException(Exception):
      def __init__(self, msg):
          self.msg = msg

language = input("Enter language [Go or Python]: ")
if not language in ["Go","Python"]:
   raise InputValidationException("Invalid input, Please enter either Go or Python!!!")