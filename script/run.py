from script.book import get_content_list, get_detailed_info
from script.document import create_word_doc

def run_script():
    book_title = input("Enter the book title: ")
    word_count = input("Enter the word count for each content item: ")
    while True:
        content = get_content_list(book_title)
        print("\nContent List:\n")
        print('\n'.join(content))

        confirm = input("\nAre you satisfied with the content list? (yes[Generate the book]/no[Regenerate the list]): ").lower()
        if confirm == 'yes':
            detailed_info_list = [get_detailed_info(item, word_count) for item in content]
            create_word_doc(book_title, content, detailed_info_list)
            print(f"Book generated successfully in MS Word with the filename '{book_title}.docx'.")
            break
        elif confirm == 'no':
            print("Generating a new content list...")
        else:
            print("Invalid response.")
