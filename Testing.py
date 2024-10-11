import unittest


class survey():
    def __init__ (self, question):
        self.question = question
        self.responses = [ ]
    
    def showQuestion(self):
        print(self.question)

    def storeResponse (self,  new_response):
        self.responses.append(new_response)
    
    def result(self):
        for response in self.responses:
            print("-" + response)
        

question = input("enter any question:")
q = survey(question)

q.showQuestion()
print("enter a to quit\n")

while True:
    response = input("enter your response: ")
    if response == "a":
        break
    q.storeResponse(response)

print("the result is:")
q.result()



class Testing(unittest.TestCase):

    def test_store_response(self):
        ask = "hey"
        c = survey(ask)
        c.storeResponse("yup")

        self.assertIn("yup", c.responses)

        
    def three_store_response(self):
        ask = "hey"
        c = survey(ask)
        responses = ["hola", "hello", "yup"]
        for i in responses:
            c.storeResponse(i)

        for q in responses:
            self.assertIn(q, c.responses)

unittest.main()
