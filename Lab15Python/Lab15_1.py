import pandas as pd

students_height = {
    "Петров": 180,
    "Огли": 175,
    "Гура": 190,
    "Штиря": 185,
    "Нестеренко": 178,
    "Павленко": 183,
    "Бакало": 182,
    "Шевченко": 175,
    "Бондарев": 177,
    "Василенко": 179
}

df = pd.DataFrame(list(students_height.items()), columns=["Student", "Height"])
print("Початковий датафрейм:")
print(df)

df["Course"] = [1, 2, 1, 2, 3, 3, 1, 2, 3, 2]  # Курс студента
df["Gender"] = ["Male", "Male", "Male", "Male", "Male", "Male", "Male", "Female", "Female", "Female"]  # Стать

print("\nДатафрейм з новими стовпцями:")
print(df)

grouped_by_course = df.groupby("Course")["Height"].agg(["mean", "max"])
print("\nАгрегація по курсу (середній та максимальний зріст):")
print(grouped_by_course)

grouped_by_gender = df.groupby("Gender")["Height"].agg(["mean", "min", "max", "count"])
print("\nАгрегація по статі (середній, мінімальний, максимальний зріст, кількість студентів):")
print(grouped_by_gender)
