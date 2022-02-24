import random

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,
                               Schoolkid)

COMENDATIONS = ('Молодец!',
                'Отлично!',
                'Хорошо!',
                'Гораздо лучше, чем я ожидал!',
                'Ты меня приятно удивил!',
                'Великолепно!',
                'Прекрасно!',
                'Ты меня очень обрадовал!',
                'Именно этого я давно ждал от тебя!',
                'Сказано здорово – просто и ясно!',
                'Ты, как всегда, точен!',
                'Очень хороший ответ!',
                'Талантливо!',
                'Ты сегодня прыгнул выше головы!',
                'Я поражен!',
                'Уже существенно лучше!',
                'Потрясающе!',
                'Замечательно!',
                'Прекрасное начало!',
                'Так держать!',
                'Ты на верном пути!',
                'Здорово!',
                'Это как раз то, что нужно!',
                'Я тобой горжусь!',
                'С каждым разом у тебя получается всё лучше!',
                'Мы с тобой не зря поработали!',
                'Я вижу, как ты стараешься!',
                'Ты растешь над собой!',
                'Ты многое сделал, я это вижу!',
                'Теперь у тебя точно все получится!')


def get_schoolkid(kid_name: str) -> Schoolkid | None:
    return Schoolkid.objects.get(full_name__contains=kid_name)


def fix_marks(
        schoolkid: Schoolkid,
        bad_points: list[int],
        good_point: int) -> None:
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=bad_points)
    marks.update(points=good_point)


def remove_chastisements(schoolkid: Schoolkid) -> None:
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def get_last_lesson(schoolkid: Schoolkid, subject_title: str) -> Lesson | None:
    return Lesson.objects.filter(
        group_letter=schoolkid.group_letter,
        year_of_study=schoolkid.year_of_study,
        subject__title=subject_title).order_by('date').last()


def create_commendation(
        schoolkid: Schoolkid,
        lesson: Lesson,
        text: str) -> None:
    Commendation.objects.create(
        text=text,
        created=lesson.date,
        subject=lesson.subject,
        teacher=lesson.teacher,
        schoolkid=schoolkid)


kid_name = input("ФИО ученика: ").strip()
subject_title = input(
    "Название предмета для похвалы: ").strip().capitalize()
if not kid_name:
    print("Не указано имя ученика!")
    exit(1)
try:
    schoolkid = get_schoolkid(kid_name)
except Schoolkid.MultipleObjectsReturned:
    print("Найдено много учеников, укажите имя точнее!")
    exit(1)
except Schoolkid.DoesNotExist:
    print("Ученик не найден - проверьте имя!")
    exit(1)

lesson = get_last_lesson(schoolkid, subject_title)
if not lesson:
    print("Не найден урок - проверьте название предмета!")
    exit(1)

fix_marks(schoolkid, bad_points=[2, 3], good_point=5)
remove_chastisements(schoolkid)
create_commendation(schoolkid, lesson, random.choice(COMENDATIONS))

print("Шалость удалась!")
quit()
