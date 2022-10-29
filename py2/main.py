import pandas
import matplotlib
import seaborn


def gender(frame):
    matrix = frame[frame.columns[0]]
    matrix.tolist()
    all_sex = len(matrix)
    male, female, infant = 0, 0, 0
    for i in range(len(matrix)):
        if matrix[i] == "M":
            male += 1
        elif matrix[i] == "F":
            female += 1
        elif matrix[i] == "I":
            infant += 1
        else:
            continue

    female_perc = round((female / all_sex) * 100, 2)
    male_perc = round((male / all_sex) * 100, 2)
    infant_perc = round((infant / all_sex) * 100, 2)
    all_sex = male + female + infant
    all_perc = round(infant_perc + male_perc + female_perc)
    to_frame_data = {'count': [female, male, infant, '---------', all_sex],
                     '%': [female_perc, male_perc, infant_perc, '---------', all_perc]
                     }
    df = pandas.DataFrame(to_frame_data, index=['Female', 'Male', 'Infant', '---------', 'Sum'])

    print(df.to_string())


if __name__ == '__main__':
    data_frame = pandas.read_csv('./dataset/data.csv')
    gender(data_frame)
    exit(0)
