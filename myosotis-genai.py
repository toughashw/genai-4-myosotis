import openai
def chatBot(text):
    openai.api_key = "sk-proj-y71lVRntyGEWgGCoFig6T3BlbkFJSqRl2IVnInd0fq6r4zGw"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.3,
        max_tokens = 200,
    )
    return print(response.choices[0].text)
    
def main():
    while True:
        print('Chiedimi quello che vuoi sul Wedding:\n')
        domanda = input()
        chatBot(domanda)
        print('\n')
main()