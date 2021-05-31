from scipy import stats


def open_and_reformat_file(file_name):
    """
    Open data_files and create list of numbers
    !!!.txt files must contain numbers separated by spaces!!!

    Parameters:
    ----------
    file_name: .txt filename
    """

    with open(f'files_data/{file_name}', 'r', encoding='UTF-8') as file:
        argument = file.read()
        argument = argument.split(' ')
    output = [float(x) for x in argument]
    return output


def count_correlation(first_file, second_file):
    """
    checks list of numbers for normality and calculates the correlation of these lists

    Parameters:
    -----------
    first_file: .txt filename
    second_file: .txt filename
    """
    first_number = open_and_reformat_file(f'{first_file}')
    second_number = open_and_reformat_file(f'{second_file}')

    normaltest_for_first = stats.normaltest(first_number)
    normaltest_for_second = stats.normaltest(second_number)

    if min(normaltest_for_first[1], normaltest_for_second[1]) > 0.05:
        correlation = stats.pearsonr(first_number, second_number)
        method = 'pearson'
    else:
        correlation = stats.spearmanr(first_number, second_number)
        method = 'spearman'
    json = {'correlation_coef': correlation[0],
            'p-value': correlation[1],
            'method': method}

    return json



