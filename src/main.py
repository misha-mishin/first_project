
def print_author():
    # Импорт load_dotenv.
    from dotenv import load_dotenv 

    # Импорт библиотеки для работы с окружением.
    import os  

    # Загрузка переменных из .env
    load_dotenv(dotenv_path='/Users/mishamishin/Desktop/Data Science/Практикум/Проекты/Спринт 8/second_new_project/first_project/.env')

    author = os.getenv('AUTHOR')
    print(f"Автор проекта: {author}")

print_author()