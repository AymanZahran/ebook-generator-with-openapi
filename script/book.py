from script.api import call_openai

def get_content_list(book_title):
    prompt = f"Generate a list of content items for the book '{book_title}' in bullet point format."
    return call_openai(prompt).split('\n')

def get_detailed_info(item, word_count):
    prompt = f"Provide detailed content, in about '{word_count}' words, of the content item: {item}"
    return call_openai(prompt)
