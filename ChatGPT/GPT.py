import openai

openai.api_key = "" #bu alana chatGPT sitesinden aldığımız API key numarasını yazıyoruz..

while True:
    
    model_engine = "text-davinci-003"

    prompt = input("Bu Alana Yazabilirsiniz: ")

    if 'exit' in prompt or 'quit' in prompt:
        break

    completion = openai.Completion.create (

        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n=1, 
        stop = None,
    )


    responce =  completion.choices[0].text

    print(responce)