import pandas as pd


def get_race_count(df):
    # Begin here 
    race_array = df['race'].tolist()
    race_wo_dup_array = df['race'].drop_duplicates().tolist()
    race_dict = dict() 
    for item in race_wo_dup_array:
        race_dict[item] = race_array.count(item)
    
    # return pd.DataFrame(race_dict.items(), columns=['race', 'race_count'])
    return pd.Series(race_dict)
    
def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_data.csv', sep=',')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = get_race_count(df)

    # What is the average age of men?
    average_age_men = round(df[df['sex']=='Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    Bachelor_df = df[df['education'] == 'Bachelors']
    
    percentage_bachelors = round((Bachelor_df['education'].count()/df['education'].count()) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])] 

    high_salary_df = higher_education[higher_education['salary'] == '>50K']
    lower_education_high_salary_df  = lower_education[lower_education['salary'] == '>50K']
  
    # percentage with salary >50K
    percent_higher = high_salary_df['age'].count()/higher_education['age'].count()
    percent_lower = lower_education_high_salary_df['age'].count()/lower_education['age'].count()

    higher_education_rich = round(percent_higher * 100, 1)
    lower_education_rich = round(percent_lower * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers_df = df[df['hours-per-week'] == min_work_hours]
    
    min_workers_rich_df = num_min_workers_df[num_min_workers_df['salary'] == '>50K']

    rich_percentage = (min_workers_rich_df['age'].count()/num_min_workers_df['age'].count()) * 100


    # What country has the highest percentage of people that earn >50K?
    high_salary_df = df[df['salary'] == '>50K']
    high_salary_country = high_salary_df['native-country'].tolist()
    country = max(high_salary_country, key=high_salary_country.count)    
    print("Country: {}".format(high_salary_country))
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
