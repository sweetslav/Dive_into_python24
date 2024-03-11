# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os

def sort_files(source_directory):
    """
    Сортирует файлы из указанной директории в поддиректории в зависимости от их расширения.

    Аргументы:
    source_directory (str): Путь к исходной директории, содержащей файлы для сортировки.

    Возвращает:
    None: Функция ничего не возвращает.
    """
    video_extensions = ['.mp4', '.mkv', '.avi', '.webm']
    image_extensions = ['.png', '.jpg', '.jpeg']
    text_extensions = ['.txt', '.doc', '.pdf']

    for file in os.listdir(source_directory):
        if os.path.isfile(os.path.join(source_directory, file)):
            file_extension = os.path.splitext(file)[1]

            if file_extension in video_extensions:
                destination_folder = os.path.join(source_directory, 'Videos')
            elif file_extension in image_extensions:
                destination_folder = os.path.join(source_directory, 'Images')
            elif file_extension in text_extensions:
                destination_folder = os.path.join(source_directory, 'Text')
            else:
                destination_folder = os.path.join(source_directory, 'Other')

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            os.rename(os.path.join(source_directory, file), os.path.join(destination_folder, file))


if __name__ == '__main__':
    source_directory = r'C:\Users\slavu\PycharmProjects\Dive_Into_Python\Lesson7'
    sort_files(source_directory)
