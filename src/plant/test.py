import openai, webbrowser

openai.api_key = "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"  # 这里要更换自己的API


def input_question(input_words):
    model_engine = "text-davinci-003"
    prompt = input_words
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5, )
    message = completions.choices[0].text
    return message


def plant(input_str):
    prompt = input_str
    if prompt == 'quit':
        return
    else:
        try:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            print(image_url)
            webbrowser.open_new(image_url)
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)


plant(input_question("a white cute cat"))
