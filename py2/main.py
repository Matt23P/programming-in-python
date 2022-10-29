import pandas
import matplotlib
import seaborn
import math


def avg(tab):
    l = len(tab)
    s = 0
    for i in range(l):
        s = s + tab[i]
    mean = s / l
    return mean


def std(tab):
    l = len(tab)
    su = 0
    mean = avg(tab)
    for i in range(l):
        su = pow(tab[i] - mean, 2)
    sigma = math.sqrt(su / l)
    return sigma


def minimum(tab):
    l = len(tab)
    mini = tab[0]
    for i in range(l):
        if tab[i] < mini:
            mini = tab[i]
        else:
            continue
    return mini


def maximum(tab):
    l = len(tab)
    maxi = tab[0]
    for i in range(l):
        if tab[i] < maxi:
            mini = tab[i]
        else:
            continue
    return maxi


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

    length = data_frame[data_frame.columns[1]]
    diameter = data_frame[data_frame.columns[2]]
    height = data_frame[data_frame.columns[3]]
    whole_weight = data_frame[data_frame.columns[4]]
    shucked_weight = data_frame[data_frame.columns[5]]
    viscera_weight = data_frame[data_frame.columns[6]]
    shell_weight = data_frame[data_frame.columns[7]]
    ring = data_frame[data_frame.columns[8]]
    length.tolist()
    diameter.tolist()
    height.tolist()
    whole_weight.tolist()
    shucked_weight.tolist()
    viscera_weight.tolist()
    shell_weight.tolist()
    ring.tolist()

    processed_data = {
        'mean': [avg(length), avg(diameter), avg(height), avg(whole_weight), avg(shucked_weight), avg(viscera_weight),
                 avg(shell_weight), avg(ring)],
        'std': [std(length), std(diameter), std(height), std(whole_weight), std(shucked_weight), std(viscera_weight),
                std(shell_weight), std(ring)],
        'min': [minimum(length), minimum(diameter), minimum(height), minimum(whole_weight), minimum(shucked_weight),
                minimum(viscera_weight), minimum(shell_weight), minimum(ring)],
        '25%': [length.quantile(0.25), diameter.quantile(0.25), height.quantile(0.25), whole_weight.quantile(0.25),
                shucked_weight.quantile(0.25), viscera_weight.quantile(0.25), shell_weight.quantile(0.25),
                ring.quantile(0.25)],
        '50%': [length.quantile(), diameter.quantile(), height.quantile(), whole_weight.quantile(),
                shucked_weight.quantile(), viscera_weight.quantile(), shell_weight.quantile(), ring.quantile()],
        '75%': [length.quantile(0.75), diameter.quantile(0.75), height.quantile(0.75), whole_weight.quantile(0.75),
                shucked_weight.quantile(0.75), viscera_weight.quantile(0.75), shell_weight.quantile(0.75),
                ring.quantile(0.75)],
        'max': [maximum(length), maximum(diameter), maximum(height), maximum(whole_weight), maximum(shucked_weight),
                maximum(viscera_weight), maximum(shell_weight), maximum(ring)]
    }

    df = pandas.DataFrame(processed_data, index=['Lenght', 'Diameter', 'Height', 'Whole weight',
                                                 'Shucked weight', 'Viscera weight', 'Shell weight',
                                                 'Rings'])
    print(df.to_string())

    exit(0)
