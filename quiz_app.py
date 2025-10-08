import streamlit as st

# Quiz data structure
QUIZ_DATA = {
    "1. Statistics_QA": {
        "title": "Statistics Quiz",
        "questions": [
            {
                "question": "In statistics, a population refers to:",
                "options": [
                    "A subset of observations",
                    "The entire group under study",
                    "Only numerical values",
                    "Data collected from experiments"
                ],
                "correct": 1,
                "explanation": "The entire group under study. Application: In an election survey, all eligible voters form the population."
            },
            {
                "question": "A sample is:",
                "options": [
                    "A summary of data",
                    "A smaller group chosen from the population",
                    "The shape of data distribution",
                    "Always equal to the population"
                ],
                "correct": 1,
                "explanation": "A smaller group chosen from the population. Application: Out of 10,000 employees, selecting 500 for a survey is a sample."
            },
            {
                "question": "Which statement is true?",
                "options": [
                    "Population mean is a statistic; sample mean is a parameter",
                    "Population mean is a parameter; sample mean is a statistic",
                    "Both are statistics",
                    "Both are parameters"
                ],
                "correct": 1,
                "explanation": "Population mean is a parameter; sample mean is a statistic. Application: Company-wide average salary vs survey average."
            },
            {
                "question": "Which of the following is continuous data?",
                "options": [
                    "Number of goals scored in a football match",
                    "Age in years",
                    "Height of students",
                    "Number of students in class"
                ],
                "correct": 2,
                "explanation": "Height of students. Application: Continuous data is used in BMI calculation."
            },
            {
                "question": "Discrete data can best be described as:",
                "options": [
                    "Data that can take infinite values",
                    "Data measured with precision",
                    "Data that takes distinct countable values",
                    "Data with decimal places"
                ],
                "correct": 2,
                "explanation": "Data that takes distinct countable values. Application: Number of cars in a parking lot."
            },
            {
                "question": "Which is a categorical (qualitative) variable?",
                "options": [
                    "Temperature in Celsius",
                    "Student's grade (A, B, C)",
                    "Monthly income",
                    "Number of books"
                ],
                "correct": 1,
                "explanation": "Student's grade (A, B, C). Application: Used in grading systems."
            },
            {
                "question": "Which measure is best when data has extreme outliers?",
                "options": [
                    "Mean",
                    "Median",
                    "Mode",
                    "Range"
                ],
                "correct": 1,
                "explanation": "Median. Application: Median house price reflects market better."
            },
            {
                "question": "Which of the following is most suitable for categorical data?",
                "options": [
                    "Mean",
                    "Median",
                    "Mode",
                    "Variance"
                ],
                "correct": 2,
                "explanation": "Mode. Application: Most common blood group type."
            },
            {
                "question": "The interquartile range (IQR) is defined as:",
                "options": [
                    "Difference between maximum and minimum",
                    "Difference between Q3 and Q1",
                    "Average of all values",
                    "Standard deviation"
                ],
                "correct": 1,
                "explanation": "Difference between Q3 and Q1. Application: Used in boxplots to detect outliers."
            },
            {
                "question": "Which spread measure is in the same units as the data?",
                "options": [
                    "Variance",
                    "Standard deviation",
                    "Skewness",
                    "Kurtosis"
                ],
                "correct": 1,
                "explanation": "Standard deviation. Application: In stock market, SD is used to measure risk."
            },
            {
                "question": "A histogram is mainly used for:",
                "options": [
                    "Showing relationship between variables",
                    "Displaying frequency distribution of continuous data",
                    "Showing averages",
                    "Comparing means"
                ],
                "correct": 1,
                "explanation": "Displaying frequency distribution of continuous data. Application: Age distribution in a mall."
            },
            {
                "question": "Which distribution is symmetric and bell-shaped?",
                "options": [
                    "Positively skewed",
                    "Negatively skewed",
                    "Normal distribution",
                    "Leptokurtic"
                ],
                "correct": 2,
                "explanation": "Normal distribution. Application: IQ scores follow normal distribution."
            },
            {
                "question": "In a positively skewed distribution:",
                "options": [
                    "Mean < Median < Mode",
                    "Mode < Median < Mean",
                    "Mean = Median = Mode",
                    "Mean > Mode > Median"
                ],
                "correct": 1,
                "explanation": "Mode < Median < Mean. Application: Income distribution in a city."
            },
            {
                "question": "If exam results are negatively skewed, it means:",
                "options": [
                    "Most students scored low",
                    "Most students scored high",
                    "Scores are uniformly distributed",
                    "Data is symmetric"
                ],
                "correct": 1,
                "explanation": "Most students scored high. Application: Easy exams lead to negative skew."
            },
            {
                "question": "A distribution with flat peak and thin tails is called:",
                "options": [
                    "Mesokurtic",
                    "Platykurtic",
                    "Leptokurtic",
                    "Skewed"
                ],
                "correct": 1,
                "explanation": "Platykurtic. Application: Used in manufacturing quality checks."
            }
        ]
    },
    "2. Visualization_QA": {
        "title": "Visualization Quiz",
        "questions": [ {
            "question": "A bar graph is most useful for:",
            "options": [
                "Showing frequency distribution of continuous data",
                "Comparing categorical variables",
                "Showing correlations between variables",
                "Measuring variance"
            ],
            "correct": 1,
            "explanation": "Comparing categorical variables. Application: Comparing sales of products (e.g., laptops vs mobiles vs tablets)."
        },
        {
            "question": "In a bar graph, the bars are:",
            "options": [
                "Always vertical",
                "Can be vertical or horizontal",
                "Always horizontal",
                "Always equal in height"
            ],
            "correct": 1,
            "explanation": "Can be vertical or horizontal. Application: Horizontal bar graphs compare population by states."
        },
        {
            "question": "Which statement is correct about bar graphs?",
            "options": [
                "Bars touch each other",
                "Bars do not touch each other",
                "Bars represent continuous data",
                "Bars are only used for numerical data"
            ],
            "correct": 1,
            "explanation": "Bars do not touch each other. Application: Used in student grade distribution (A, B, C, D)."
        },
        {
            "question": "What does the box in a box plot represent?",
            "options": [
                "Mean and variance",
                "Minimum and maximum values",
                "Interquartile range (IQR)",
                "Standard deviation"
            ],
            "correct": 2,
            "explanation": "Interquartile range (IQR). Application: Salary distribution analysis in HR."
        },
        {
            "question": "Whiskers in a box plot extend up to:",
            "options": [
                "Minimum and maximum values always",
                "1.5 × IQR from Q1 and Q3",
                "Mean ± 2 SD",
                "Mode ± Range"
            ],
            "correct": 1,
            "explanation": "1.5 × IQR from Q1 and Q3. Application: Detecting outliers in exam scores."
        },
        {
            "question": "Points lying beyond whiskers in a box plot are:",
            "options": [
                "Median values",
                "Outliers",
                "Normal distribution",
                "Quartiles"
            ],
            "correct": 1,
            "explanation": "Outliers. Application: Fraud detection in transactions."
        },
        {
            "question": "A scatter plot shows:",
            "options": [
                "Relationship between two variables",
                "Frequency distribution of data",
                "Central tendency",
                "Box and whiskers"
            ],
            "correct": 0,
            "explanation": "Relationship between two variables. Application: Height vs Weight of students."
        },
        {
            "question": "If points in a scatter plot slope upwards (left to right), it indicates:",
            "options": [
                "Negative correlation",
                "Positive correlation",
                "No correlation",
                "Symmetric distribution"
            ],
            "correct": 1,
            "explanation": "Positive correlation. Application: Study time vs Exam marks."
        },
        {
            "question": "If points are randomly scattered without pattern:",
            "options": [
                "Positive correlation",
                "Negative correlation",
                "No correlation",
                "Symmetry"
            ],
            "correct": 2,
            "explanation": "No correlation. Application: Shoe size vs IQ."
        },
        {
            "question": "Which type of correlation does a downward slope in scatter plot indicate?",
            "options": [
                "Positive",
                "Negative",
                "Neutral",
                "Symmetric"
            ],
            "correct": 1,
            "explanation": "Negative correlation. Application: Stress levels vs Productivity."
        },
        {
            "question": "Correlation coefficient ranges between:",
            "options": [
                "0 to 1",
                "-∞ to +∞",
                "-1 to +1",
                "0 to 100"
            ],
            "correct": 2,
            "explanation": "−1 to +1. Application: Finance – stocks correlation."
        },
        {
            "question": "If correlation = +1, it means:",
            "options": [
                "Perfect positive linear relationship",
                "Perfect negative linear relationship",
                "No relationship",
                "Weak relationship"
            ],
            "correct": 0,
            "explanation": "Perfect positive linear relationship. Application: Celsius vs Fahrenheit scale."
        },
        {
            "question": "If correlation = 0:",
            "options": [
                "Strong relation",
                "Weak negative relation",
                "No linear relationship",
                "Perfect neutral"
            ],
            "correct": 2,
            "explanation": "No linear relationship. Application: Height vs Mobile bill."
        },
        {
            "question": "Strong negative correlation means:",
            "options": [
                "As one increases, the other decreases",
                "Both increase together",
                "No connection",
                "Both remain constant"
            ],
            "correct": 0,
            "explanation": "As one increases, the other decreases. Application: Exercise time vs Body fat %."
        },
        {
            "question": "Which of the following tools is used to visualize correlation?",
            "options": [
                "Histogram",
                "Scatter plot",
                "Pie chart",
                "Bar graph"
            ],
            "correct": 1,
            "explanation": "Scatter plot. Application: Used in data science for variable dependency checks."
        }
        ]
    },
    "3. Python_Basics_QA": {
        "title": "Python Basics Quiz",
        "questions": [
        {
            "question": "Which of the following is an immutable datatype in Python?",
            "options": [
                "List",
                "Dictionary",
                "Tuple",
                "Set"
            ],
            "correct": 2,
            "explanation": "Tuples are used to store fixed data like geographical coordinates."
        },
        {
            "question": "Which datatype is best suited for key-value pair storage?",
            "options": [
                "List",
                "Tuple",
                "Dictionary",
                "Set"
            ],
            "correct": 2,
            "explanation": "Used in storing student roll numbers with names."
        },
        {
            "question": "A set in Python:",
            "options": [
                "Allows duplicate values",
                "Maintains insertion order",
                "Stores unique unordered elements",
                "Is immutable"
            ],
            "correct": 2,
            "explanation": "Stores unique unordered elements. Application: Used in removing duplicates from customer email lists."
        },
        {
            "question": "What will be the result of 10 // 3 in Python?",
            "options": [
                "3.33",
                "3",
                "3.0",
                "Error"
            ],
            "correct": 1,
            "explanation": "Floor division is used in installment calculations."
        },
        {
            "question": "Which operator is used for logical AND in Python?",
            "options": [
                "&",
                "&&",
                "and",
                "All of the above"
            ],
            "correct": 2,
            "explanation": "Checking multiple conditions in authentication systems."
        },
        {
            "question": "What is the output of 5 == 5 and 10 > 5?",
            "options": [
                "True",
                "False",
                "Error",
                "None"
            ],
            "correct": 0,
            "explanation": "Used in conditional validations in programs."
        },
        {
            "question": "Which method adds an element at the end of a list?",
            "options": [
                "insert()",
                "append()",
                "extend()",
                "add()"
            ],
            "correct": 1,
            "explanation": "Adding new customers to a list."
        },
        {
            "question": "Which method is used to combine two lists?",
            "options": [
                "insert()",
                "extend()",
                "append()",
                "merge()"
            ],
            "correct": 1,
            "explanation": "Combining monthly sales lists into yearly sales."
        },
        {
            "question": "Which method removes an element at a specified index?",
            "options": [
                "pop()",
                "remove()",
                "delete()",
                "discard()"
            ],
            "correct": 0,
            "explanation": "Removing a selected item from a shopping cart."
        },
        {
            "question": "Which list method returns the index of the first occurrence of a value?",
            "options": [
                "find()",
                "locate()",
                "index()",
                "count()"
            ],
            "correct": 2,
            "explanation": "Finding position of a student’s name in a class list."
        },
        {
            "question": "Which list method counts occurrences of an element?",
            "options": [
                "find()",
                "index()",
                "count()",
                "locate()"
            ],
            "correct": 2,
            "explanation": "Counting frequency of product orders."
        },
        {
            "question": "Which method sorts a list in place?",
            "options": [
                "order()",
                "sort()",
                "arrange()",
                "sorted()"
            ],
            "correct": 1,
            "explanation": "Sorting exam scores from lowest to highest."
        },
        {
            "question": "Tuples differ from lists because:",
            "options": [
                "Tuples are mutable",
                "Tuples are immutable",
                "Tuples store only numbers",
                "Tuples allow duplicates only"
            ],
            "correct": 1,
            "explanation": "Configuration settings stored as tuples."
        },
        {
            "question": "Which dictionary method returns all keys?",
            "options": [
                "dict.values()",
                "dict.keys()",
                "dict.items()",
                "dict.all()"
            ],
            "correct": 1,
            "explanation": "Extracting all student roll numbers."
        },
        {
            "question": "Which set operation returns common elements?",
            "options": [
                "union()",
                "intersection()",
                "difference()",
                "symmetric_difference()"
            ],
            "correct": 1,
            "explanation": "Finding students enrolled in both Math and Science courses."
        }
        ]
    },
    "4. Python_Loops_NumPy_Pandas_QA": {
        "title": "Python Loops, NumPy & Pandas Quiz",
        "questions": [
        {
            "question": "What is the main use of a for loop in Python?",
            "options": [
                "To repeat tasks until condition is false",
                "To iterate over sequences",
                "To stop code execution",
                "To assign variables"
            ],
            "correct": 1,
            "explanation": "Iterating through student names in a class list."
        },
        {
            "question": "Which of the following correctly prints numbers from 1 to 5?",
            "options": [
                "for i in range(1,6): print(i)",
                "for i in range(5): print(i)",
                "for i in range(1,5): print(i)",
                "for i in range(0,5): print(i+1)"
            ],
            "correct": 0,
            "explanation": "Printing roll numbers in a class."
        },
        {
            "question": "What keyword is used to skip the current iteration in a loop?",
            "options": [
                "stop",
                "exit",
                "continue",
                "break"
            ],
            "correct": 2,
            "explanation": "Skipping invalid entries in survey data."
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "def",
                "function",
                "define",
                "fun"
            ],
            "correct": 0,
            "explanation": "Creating reusable salary calculation functions."
        },
        {
            "question": "Which statement is true about functions?",
            "options": [
                "Functions reduce reusability",
                "Functions cannot return values",
                "Functions make code modular",
                "Functions are slower"
            ],
            "correct": 2,
            "explanation": "Used in modular software development."
        },
        {
            "question": "Default return value of a Python function without return?",
            "options": [
                "0",
                "Null",
                "None",
                "Error"
            ],
            "correct": 2,
            "explanation": "Used in logging functions where return isn’t needed."
        },
        {
            "question": "NumPy stands for:",
            "options": [
                "Numerical Python",
                "Number Python",
                "Numeric Program",
                "None"
            ],
            "correct": 0,
            "explanation": "Used in scientific computations."
        },
        {
            "question": "Which function creates a 1D NumPy array?",
            "options": [
                "np.array([1,2,3])",
                "np.vector(1,2,3)",
                "np.scalar([1,2,3])",
                "np.list([1,2,3])"
            ],
            "correct": 0,
            "explanation": "Storing monthly sales figures."
        },
        {
            "question": "How do you create a 2D NumPy array?",
            "options": [
                "np.array([[1,2],[3,4]])",
                "np.array((1,2),(3,4))",
                "np.array[1,2;3,4]",
                "np.matrix([1,2,3,4])"
            ],
            "correct": 0,
            "explanation": "Representing matrix operations in ML."
        },
        {
            "question": "Which function generates random integers in NumPy?",
            "options": [
                "np.random.num()",
                "np.randint()",
                "np.random.randint()",
                "np.generate()"
            ],
            "correct": 2,
            "explanation": "Simulating dice rolls."
        },
        {
            "question": "A scalar in NumPy represents:",
            "options": [
                "Single number",
                "Row of numbers",
                "Column of numbers",
                "Matrix"
            ],
            "correct": 0,
            "explanation": "Representing single unit prices."
        },
        {
            "question": "To convert NumPy array into Pandas DataFrame:",
            "options": [
                "pd.list()",
                "pd.DataFrame()",
                "np.to_pd()",
                "DataFrame.convert()"
            ],
            "correct": 1,
            "explanation": "Converting numerical results to labeled data."
        },
        {
            "question": "How do you assign column names in Pandas DataFrame?",
            "options": [
                "df.column()",
                "df.set()",
                "df.columns = ['A','B']",
                "df.setnames()"
            ],
            "correct": 2,
            "explanation": "Naming columns in survey data."
        },
        {
            "question": "Which method reads a CSV file into Pandas?",
            "options": [
                "pd.load_csv()",
                "pd.read_csv()",
                "pd.import_csv()",
                "pd.csv_read()"
            ],
            "correct": 1,
            "explanation": "Importing Excel/CSV datasets."
        },
        {
            "question": "Which function gives first 5 rows of a DataFrame?",
            "options": [
                "df.tail()",
                "df.head()",
                "df.describe()",
                "df.rows()"
            ],
            "correct": 1,
            "explanation": "Previewing dataset before analysis."
        }
        ]
    },
    "5. Pandas_Advanced_QA": {
        "title": "Pandas Advanced Quiz",
        "questions": [
            {
            "question": "What does df.info() provide?",
            "options": [
                "Statistical summary of numerical columns",
                "Memory usage, datatypes, non-null counts",
                "First 5 rows of the DataFrame",
                "Shape of DataFrame"
            ],
            "correct": 1,
            "explanation": "Checking data quality in large datasets."
        },
        {
            "question": "Which of the following shows number of non-null entries in each column?",
            "options": [
                "df.shape",
                "df.info()",
                "df.describe()",
                "df.head()"
            ],
            "correct": 1,
            "explanation": "Used in data cleaning process."
        },
        {
            "question": "How do you select a single column in Pandas?",
            "options": [
                "df.get('col')",
                "df.col",
                "df['col']",
                "Both b and c"
            ],
            "correct": 3,
            "explanation": "Selecting salary column in HR dataset."
        },
        {
            "question": "How do you select multiple columns?",
            "options": [
                "df[['col1','col2']]",
                "df('col1','col2')",
                "df.get(col1,col2)",
                "df.col1,col2"
            ],
            "correct": 0,
            "explanation": "Selecting sales and profit columns together."
        },
        {
            "question": "Correct way to drop a column permanently?",
            "options": [
                "df.drop('col', inplace=True, axis=1)",
                "df.remove('col')",
                "df.dropcolumn('col')",
                "df.delete('col')"
            ],
            "correct": 0,
            "explanation": "Dropping unused ID fields."
        },
        {
            "question": "Axis=1 in drop() refers to:",
            "options": [
                "Row",
                "Column",
                "Index",
                "Both rows and columns"
            ],
            "correct": 1,
            "explanation": "Dropping extra columns in survey data."
        },
        {
            "question": "What does groupby() do?",
            "options": [
                "Merge DataFrames",
                "Summarizes data by categories",
                "Remove duplicates",
                "Select rows"
            ],
            "correct": 1,
            "explanation": "Total sales per region."
        },
        {
            "question": "Which function is often used after groupby()?",
            "options": [
                "sum(), mean()",
                "drop()",
                "fillna()",
                "concat()"
            ],
            "correct": 0,
            "explanation": "Finding average marks per subject."
        },
        {
            "question": "Concatenating DataFrames row-wise is done with:",
            "options": [
                "pd.concat([df1,df2], axis=0)",
                "pd.concat([df1,df2], axis=1)",
                "df1.append(df2) only",
                "df1+df2"
            ],
            "correct": 0,
            "explanation": "Combining monthly reports into yearly report."
        },
        {
            "question": "Concatenating DataFrames column-wise is done with:",
            "options": [
                "axis=0",
                "axis=1",
                "append()",
                "merge()"
            ],
            "correct": 1,
            "explanation": "Joining customer info with their purchase history."
        },
        {
            "question": "Which function merges two DataFrames on keys?",
            "options": [
                "pd.concat()",
                "pd.merge()",
                "df.append()",
                "df.join()"
            ],
            "correct": 1,
            "explanation": "Merging employee details with salary data."
        },
        {
            "question": "What is the default join type in pd.merge()?",
            "options": [
                "inner",
                "outer",
                "left",
                "right"
            ],
            "correct": 0,
            "explanation": "Fetching common students in two course lists."
        },
        {
            "question": "Which function removes duplicate rows?",
            "options": [
                "df.drop()",
                "df.remove()",
                "df.drop_duplicates()",
                "df.unique()"
            ],
            "correct": 2,
            "explanation": "Removing duplicate customer entries."
        },
        {
            "question": "Which function is used to fill NaN values?",
            "options": [
                "df.fill()",
                "df.fillna()",
                "df.replace()",
                "df.fillmissing()"
            ],
            "correct": 1,
            "explanation": "Filling missing salary data."
        },
        {
            "question": "Filling missing values with column mean is done by:",
            "options": [
                "df.fillna(df.mean())",
                "df.replace(df.mean())",
                "df.missing(df.mean())",
                "df.fill(df.mean())"
            ],
            "correct": 0,
            "explanation": "Replacing missing exam scores with average."
        }
        ]
    },
    "6. EDA_Visualization_QA": {
        "title": "EDA & Visualization Quiz",
        "questions": [
        {
            "question": "What does a histogram show?",
            "options": [
                "Relationship between two variables",
                "Frequency distribution of continuous data",
                "Categorical variable comparison",
                "Average values"
            ],
            "correct": 1,
            "explanation": "Age distribution of customers in retail."
        },
        {
            "question": "Which Python library function is commonly used for histograms?",
            "options": [
                "plt.hist()",
                "sns.hist()",
                "df.hist()",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Used in exam score analysis."
        },
        {
            "question": "What does a boxplot display?",
            "options": [
                "Central tendency only",
                "Mean, variance, correlation",
                "Quartiles, IQR, outliers",
                "Relationship between 2 variables"
            ],
            "correct": 2,
            "explanation": "Salary distribution in a company."
        },
        {
            "question": "Which function in seaborn plots boxplots?",
            "options": [
                "sns.box()",
                "sns.boxplot()",
                "plt.boxplot()",
                "Both b and c"
            ],
            "correct": 3,
            "explanation": "Detecting fraudulent transaction outliers."
        },
        {
            "question": "A bar graph is suitable for:",
            "options": [
                "Continuous data",
                "Categorical data",
                "Outlier detection",
                "Correlation analysis"
            ],
            "correct": 1,
            "explanation": "Comparing product sales."
        },
        {
            "question": "Which Seaborn function is used for bar graphs?",
            "options": [
                "sns.bar()",
                "sns.barplot()",
                "plt.bargraph()",
                "sns.columnplot()"
            ],
            "correct": 1,
            "explanation": "Comparing average marks per subject."
        },
        {
            "question": "Scatter plots show:",
            "options": [
                "Frequency distribution",
                "Outlier detection",
                "Relationship between two variables",
                "Quartiles"
            ],
            "correct": 2,
            "explanation": "Hours studied vs exam marks."
        },
        {
            "question": "Which Seaborn function creates scatter plots?",
            "options": [
                "sns.scatter()",
                "sns.scatterplot()",
                "plt.scatterplot()",
                "sns.pointplot()"
            ],
            "correct": 1,
            "explanation": "Advertising spend vs sales revenue."
        },
        {
            "question": "A heatmap in EDA is used for:",
            "options": [
                "Visualizing correlation matrix",
                "Showing categorical counts",
                "Frequency distribution",
                "Showing variance"
            ],
            "correct": 0,
            "explanation": "Stock correlation analysis."
        },
        {
            "question": "Which function creates heatmaps in seaborn?",
            "options": [
                "sns.heat()",
                "sns.heatmap()",
                "plt.heatmap()",
                "sns.map()"
            ],
            "correct": 1,
            "explanation": "Customer behavior analysis across features."
        },
        {
            "question": "Which library is mainly used along with Seaborn for EDA?",
            "options": [
                "NumPy",
                "Pandas",
                "Matplotlib",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Data preprocessing + visualization workflow."
        },
        {
            "question": "Which plot is best for detecting outliers?",
            "options": [
                "Histogram",
                "Boxplot",
                "Barplot",
                "Heatmap"
            ],
            "correct": 1,
            "explanation": "Identifying extreme medical bills."
        },
        {
            "question": "Which plot is best for correlation analysis?",
            "options": [
                "Histogram",
                "Scatter plot",
                "Heatmap",
                "Bar graph"
            ],
            "correct": 2,
            "explanation": "Correlation among financial indicators."
        },
        {
            "question": "Which plot is best for comparing categories?",
            "options": [
                "Bar graph",
                "Scatter plot",
                "Heatmap",
                "Boxplot"
            ],
            "correct": 0,
            "explanation": "Comparing monthly sales of products."
        },
        {
            "question": "Which Seaborn plot can show both distribution and density?",
            "options": [
                "sns.distplot()",
                "sns.histplot()",
                "sns.kdeplot()",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Website traffic analysis."
        }
        ]
    },
    "7. Normal_Distribution_QA": {
        "title": "Normal Distribution Quiz",
        "questions": [
        {
            "question": "A normal distribution curve is also known as:",
            "options": [
                "Skewed curve",
                "Bell curve",
                "Flat curve",
                "Exponential curve"
            ],
            "correct": 1,
            "explanation": "IQ scores typically follow normal distribution."
        },
        {
            "question": "In a normal distribution, mean, median, and mode are:",
            "options": [
                "Always different",
                "Equal",
                "Opposite",
                "Undefined"
            ],
            "correct": 1,
            "explanation": "Height of population often shows this property."
        },
        {
            "question": "About 68% of data in normal distribution lies within:",
            "options": [
                "1 SD",
                "2 SD",
                "3 SD",
                "4 SD"
            ],
            "correct": 0,
            "explanation": "Used in quality control."
        },
        {
            "question": "Z-score measures:",
            "options": [
                "Distance from mean in SD units",
                "Probability of event",
                "Median position",
                "Outliers only"
            ],
            "correct": 0,
            "explanation": "Detecting outliers in student marks."
        },
        {
            "question": "Z-score of 0 means:",
            "options": [
                "At mean",
                "Maximum",
                "Minimum",
                "Outlier"
            ],
            "correct": 0,
            "explanation": "Standardized exam scores."
        },
        {
            "question": "If a student scores Z=+2, it means:",
            "options": [
                "2 points above mean",
                "2 SD above mean",
                "2% above mean",
                "None"
            ],
            "correct": 1,
            "explanation": "Identifying top performers."
        },
        {
            "question": "Z tables are used to:",
            "options": [
                "Find SD",
                "Find probability",
                "Find mean",
                "Find variance"
            ],
            "correct": 1,
            "explanation": "Hypothesis testing."
        },
        {
            "question": "The cumulative probability for Z=0 is:",
            "options": [
                "0.25",
                "0.50",
                "0.75",
                "1.00"
            ],
            "correct": 1,
            "explanation": "Half of the area under the bell curve."
        },
        {
            "question": "The Z table gives probability from:",
            "options": [
                "-∞ to z",
                "z to ∞",
                "-z to +z",
                "0 to z"
            ],
            "correct": 0,
            "explanation": "Confidence intervals."
        },
        {
            "question": "Normal distribution is widely used in:",
            "options": [
                "QC",
                "Finance",
                "Biology",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Stock returns, blood pressure levels."
        },
        {
            "question": "In Six Sigma, how many SDs cover almost all data?",
            "options": [
                "3",
                "4",
                "6",
                "2"
            ],
            "correct": 2,
            "explanation": "Manufacturing defect reduction."
        },
        {
            "question": "Which library is used for normal distribution in Python?",
            "options": [
                "NumPy",
                "Pandas",
                "Matplotlib",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Simulation, storage, visualization."
        },
        {
            "question": "Function to generate normal distribution in NumPy:",
            "options": [
                "np.normal()",
                "np.random.normal()",
                "np.random.gaussian()",
                "np.norm()"
            ],
            "correct": 1,
            "explanation": "Simulating heights of people."
        },
        {
            "question": "A 95% confidence interval means:",
            "options": [
                "95% correct",
                "95% probability true mean lies in interval",
                "95% valid",
                "None"
            ],
            "correct": 1,
            "explanation": "Medical trial effectiveness."
        },
        {
            "question": "Confidence interval gets narrower if:",
            "options": [
                "Sample size increases",
                "Decreases",
                "SD increases",
                "Confidence level increases"
            ],
            "correct": 0,
            "explanation": "Larger surveys give precise estimates."
        }
        ]
    },
    "8. Hypothesis_Testing_QA": {
        "title": "Hypothesis Testing Quiz",
        "questions": [
        {
            "question": "What does the level of significance (α) represent in hypothesis testing?",
            "options": [
                "Probability of rejecting a true null hypothesis",
                "Probability of accepting a false null hypothesis",
                "Confidence level",
                "Test statistic value"
            ],
            "correct": 0,
            "explanation": "In medical trials, α = 0.05 means 5% chance of concluding a drug is effective when it’s not."
        },
        {
            "question": "What is the null hypothesis (H0) usually about?",
            "options": [
                "Difference exists",
                "No difference exists",
                "Always false",
                "Always true"
            ],
            "correct": 1,
            "explanation": "Testing if a new fertilizer increases crop yield compared to the old one."
        },
        {
            "question": "A one-sample Z-test is used when:",
            "options": [
                "Comparing one sample mean to a population mean",
                "Comparing two sample means",
                "Population standard deviation is unknown",
                "Used for categorical data"
            ],
            "correct": 0,
            "explanation": "Checking if the average weight of apples from a farm is 100g."
        },
        {
            "question": "A two-sample Z-test is appropriate when:",
            "options": [
                "One population mean is tested",
                "Two population means are compared",
                "Variance is unknown",
                "Used for nominal data"
            ],
            "correct": 1,
            "explanation": "Comparing average exam scores of two classes."
        },
        {
            "question": "A t-test is usually used when:",
            "options": [
                "Population variance is known",
                "Population variance is unknown",
                "For categorical data",
                "For correlation analysis"
            ],
            "correct": 1,
            "explanation": "Comparing average salaries between two departments with small sample sizes."
        },
        {
            "question": "The smaller the p-value:",
            "options": [
                "The stronger the evidence against H0",
                "The stronger the evidence for H0",
                "Always proves H1 is true",
                "Significance level decreases"
            ],
            "correct": 0,
            "explanation": "p=0.001 in a cancer drug trial strongly suggests effectiveness."
        },
        {
            "question": "If α = 0.05, what confidence level is implied?",
            "options": [
                "90%",
                "95%",
                "99%",
                "100%"
            ],
            "correct": 1,
            "explanation": "Business decision-making under 95% confidence interval of customer demand forecasting."
        },
        {
            "question": "Which test is more robust for small sample sizes?",
            "options": [
                "Z-test",
                "t-test",
                "Chi-square test",
                "ANOVA"
            ],
            "correct": 1,
            "explanation": "Testing the effect of a training program on a group of 20 employees."
        },
        {
            "question": "In hypothesis testing, Type I error occurs when:",
            "options": [
                "Accepting a true H0",
                "Rejecting a true H0",
                "Rejecting a false H0",
                "Accepting a false H0"
            ],
            "correct": 1,
            "explanation": "Declaring a machine defective when it is working fine."
        },
        {
            "question": "Type II error means:",
            "options": [
                "Accepting a true H0",
                "Rejecting a true H0",
                "Accepting a false H0",
                "Rejecting a false H0"
            ],
            "correct": 2,
            "explanation": "Failing to detect a disease when the patient actually has it."
        },
        {
            "question": "What is the formula for Z in a one-sample Z-test?",
            "options": [
                "(X - µ) / (σ/√n)",
                "(X - µ) / (s/√n)",
                "(ΣX - µ)/σ",
                "µ/σ"
            ],
            "correct": 0,
            "explanation": "Testing if average height of men in a city is 170 cm."
        },
        {
            "question": "What is the test statistic for a t-test?",
            "options": [
                "(X - µ) / (σ/√n)",
                "(X - µ) / (s/√n)",
                "(ΣX - µ)/σ",
                "µ/σ"
            ],
            "correct": 1,
            "explanation": "Comparing average productivity of two small manufacturing plants."
        },
        {
            "question": "In hypothesis testing, p < α means:",
            "options": [
                "Fail to reject H0",
                "Reject H0",
                "Accept H0",
                "Test inconclusive"
            ],
            "correct": 1,
            "explanation": "Concluding a new ad campaign increases sales when p=0.03 < α=0.05."
        },
        {
            "question": "Why is the t-distribution wider than Z-distribution?",
            "options": [
                "Accounts for unknown variance",
                "Always incorrect",
                "Depends on categorical variables",
                "Only for proportions"
            ],
            "correct": 0,
            "explanation": "Small sample experiment results in wider confidence intervals."
        },
        {
            "question": "A paired t-test is used when:",
            "options": [
                "Comparing two independent groups",
                "Comparing two related groups",
                "Comparing variance",
                "Comparing categorical data"
            ],
            "correct": 1,
            "explanation": "Measuring weight of patients before and after a new diet plan."
        }
        ]
    },
    "9. Linear_Regression_QA": {
        "title": "Linear Regression Quiz",
        "questions": [
        {
            "question": "Which of the following is the formula for a simple linear regression line?",
            "options": [
                "y = β + β x + ε",
                "y = mx + c",
                "y = ax² + bx + c",
                "y = log(x)"
            ],
            "correct": 0,
            "explanation": "Predicting house prices based on square footage."
        },
        {
            "question": "What does R² (coefficient of determination) indicate?",
            "options": [
                "Average error",
                "Percentage of variance explained",
                "Correlation sign",
                "Regression slope"
            ],
            "correct": 1,
            "explanation": "R² = 0.85 means 85% of variation in salary is explained by years of experience."
        },
        {
            "question": "Which metric penalizes large errors more heavily?",
            "options": [
                "RMSE",
                "R²",
                "MAE",
                "Adjusted R²"
            ],
            "correct": 0,
            "explanation": "In energy consumption prediction, RMSE highlights large deviations."
        },
        {
            "question": "Which assumption is required for Multiple Linear Regression?",
            "options": [
                "Linearity",
                "Homoscedasticity",
                "No multicollinearity",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Residuals must be normally distributed in sales forecasting."
        },
        {
            "question": "What is multicollinearity?",
            "options": [
                "Correlation among independent variables",
                "Correlation among dependent variables",
                "Errors correlated",
                "R² = 1"
            ],
            "correct": 0,
            "explanation": "Predicting revenue using both 'number of ads' and 'marketing spend' which are highly correlated."
        },
        {
            "question": "Which statistic is used to detect multicollinearity?",
            "options": [
                "R²",
                "RMSE",
                "VIF",
                "p-value"
            ],
            "correct": 2,
            "explanation": "VIF > 10 in credit risk analysis indicates redundant variables."
        },
        {
            "question": "What happens when RMSE is 0?",
            "options": [
                "Perfect prediction",
                "Poor model",
                "No variance explained",
                "Multicollinearity present"
            ],
            "correct": 0,
            "explanation": "A stock price model predicting actual values without error."
        },
        {
            "question": "Which regression method handles multiple predictors?",
            "options": [
                "SLR",
                "MLR",
                "Logistic regression",
                "Polynomial regression"
            ],
            "correct": 1,
            "explanation": "Predicting medical costs using age, BMI, and smoking status."
        },
        {
            "question": "Which variable selection method is based on step-by-step addition?",
            "options": [
                "Backward elimination",
                "Forward selection",
                "Ridge regression",
                "None"
            ],
            "correct": 1,
            "explanation": "Used in econometrics to build parsimonious models."
        },
        {
            "question": "Adjusted R² is preferred over R² because:",
            "options": [
                "It increases with added variables",
                "It adjusts for number of predictors",
                "It decreases error always",
                "None"
            ],
            "correct": 1,
            "explanation": "Ensures model fairness in employee performance prediction."
        },
        {
            "question": "Which test checks significance of regression coefficients?",
            "options": [
                "Z-test",
                "t-test",
                "ANOVA F-test",
                "Chi-square"
            ],
            "correct": 1,
            "explanation": "Checking if advertising budget has a significant effect on sales."
        },
        {
            "question": "Which regression assumption is violated if residuals increase with x?",
            "options": [
                "Linearity",
                "Homoscedasticity",
                "Independence",
                "Normality"
            ],
            "correct": 1,
            "explanation": "Income prediction errors increasing for higher salaries."
        },
        {
            "question": "If R² is very high but RMSE is also high, what does it indicate?",
            "options": [
                "Good model",
                "Overfitting",
                "Model bias",
                "Poor prediction accuracy"
            ],
            "correct": 3,
            "explanation": "Variance explained is high but errors are large."
        },
        {
            "question": "Which regularization technique is used to reduce multicollinearity?",
            "options": [
                "Lasso",
                "Ridge",
                "Elastic Net",
                "All"
            ],
            "correct": 3,
            "explanation": "Ridge regression stabilizes regression when predictors are correlated."
        },
        {
            "question": "When does multicollinearity affect regression?",
            "options": [
                "When predictors are highly independent",
                "When predictors are highly correlated",
                "When residuals are small",
                "Never"
            ],
            "correct": 1,
            "explanation": "Predicting house prices using 'size in sqft' and 'number of rooms' which overlap."
        }
        ]
    },
    "10. Data_Transformation_QA": {
        "title": "Data Transformation Quiz",
        "questions": [
          {
            "question": "Which scaler transforms data by removing the mean and scaling to unit variance?",
            "options": [
                "MinMaxScaler",
                "StandardScaler",
                "RobustScaler",
                "LabelEncoder"
            ],
            "correct": 1,
            "explanation": "Used in algorithms like Logistic Regression and SVM where features should follow standard normal distribution."
        },
        {
            "question": "MinMaxScaler transforms features into a range of:",
            "options": [
                "(-∞, ∞)",
                "(0, 1)",
                "(-1, 1)",
                "(0, ∞)"
            ],
            "correct": 1,
            "explanation": "Image pixel normalization (0 to 255 scaled into 0 to 1)."
        },
        {
            "question": "Label Encoding converts:",
            "options": [
                "Numeric to categorical",
                "Categorical to numeric",
                "Text to images",
                "Continuous to discrete"
            ],
            "correct": 1,
            "explanation": "Converting categories like ['Male', 'Female'] into [0,1]."
        },
        {
            "question": "One-Hot Encoding is preferred over Label Encoding when:",
            "options": [
                "Data is continuous",
                "Categories have no order",
                "Categories are numeric",
                "Data is normalized"
            ],
            "correct": 1,
            "explanation": "Encoding cities like ['Delhi', 'Mumbai', 'Chennai'] into dummy variables."
        },
        {
            "question": "Which of the following is a drawback of One-Hot Encoding?",
            "options": [
                "Introduces bias",
                "Increases dimensionality",
                "Causes multicollinearity",
                "Reduces accuracy"
            ],
            "correct": 1,
            "explanation": "Large datasets with thousands of categories can cause memory issues."
        },
        {
            "question": "StandardScaler assumes the data is:",
            "options": [
                "Uniformly distributed",
                "Normally distributed",
                "Skewed",
                "Discrete"
            ],
            "correct": 1,
            "explanation": "Essential for PCA since it is variance-based."
        },
        {
            "question": "What is the primary purpose of data partitioning?",
            "options": [
                "Increase accuracy",
                "Reduce overfitting",
                "Reduce data size",
                "Convert categorical data"
            ],
            "correct": 1,
            "explanation": "Splitting into train/test ensures model generalization."
        },
        {
            "question": "In scikit-learn, which function is used to split data into training and test sets?",
            "options": [
                "split_data()",
                "train_test_split()",
                "partition()",
                "data_split()"
            ],
            "correct": 1,
            "explanation": "Used before fitting any ML model in Python."
        },
        {
            "question": "What percentage split is most commonly used for train-test partitioning?",
            "options": [
                "50-50",
                "60-40",
                "70-30",
                "90-10"
            ],
            "correct": 2,
            "explanation": "Provides balance between enough training data and sufficient test evaluation."
        },
        {
            "question": "Which encoding method is best for categorical variables with many levels?",
            "options": [
                "Label Encoding",
                "One-Hot Encoding",
                "Target Encoding",
                "MinMax Scaling"
            ],
            "correct": 2,
            "explanation": "Reduces dimensionality compared to One-Hot Encoding in datasets like product IDs."
        },
        {
            "question": "Which encoding can introduce artificial order in categorical variables?",
            "options": [
                "One-Hot Encoding",
                "Label Encoding",
                "StandardScaler",
                "MinMaxScaler"
            ],
            "correct": 1,
            "explanation": "['Red', 'Green', 'Blue'] → [0,1,2] may create false order."
        },
        {
            "question": "Filling missing categorical values before encoding can be done using:",
            "options": [
                "Mode imputation",
                "Mean imputation",
                "Median imputation",
                "Standardization"
            ],
            "correct": 0,
            "explanation": "Filling missing gender values with the most frequent category."
        },
        {
            "question": "Why do we scale features before applying KNN?",
            "options": [
                "To reduce overfitting",
                "Because distance metrics are scale-dependent",
                "To increase accuracy",
                "To reduce dimensionality"
            ],
            "correct": 1,
            "explanation": "Ensures fair comparison in Euclidean distance calculation."
        },
        {
            "question": "Which technique prevents data leakage during transformation?",
            "options": [
                "Scaling before splitting",
                "Splitting before scaling",
                "One-Hot Encoding",
                "Label Encoding"
            ],
            "correct": 1,
            "explanation": "Train-test split must be done before scaling to avoid leaking test data statistics."
        },
        {
            "question": "One-Hot Encoding results in:",
            "options": [
                "Categorical columns replaced by a single numeric column",
                "Each category converted into binary column",
                "Normalized values",
                "None of the above"
            ],
            "correct": 1,
            "explanation": "Customer type ['Gold', 'Silver', 'Platinum'] → separate binary columns."
        }
        ]
    },
    "11. Classification_Metrics_QA": {
        "title": "Classification Metrics Quiz",
        "questions": [
        {
            "question": "What is the primary purpose of classification models?",
            "options": [
                "Predict continuous values",
                "Predict categorical outcomes",
                "Perform clustering",
                "Reduce dimensionality"
            ],
            "correct": 1,
            "explanation": "Email spam detection – classifying mails as 'spam' or 'not spam'."
        },
        {
            "question": "When is Logistic Regression most suitable?",
            "options": [
                "When the dependent variable is categorical",
                "For predicting continuous sales data",
                "For image classification",
                "For clustering"
            ],
            "correct": 0,
            "explanation": "Predicting whether a patient has diabetes (Yes/No)."
        },
        {
            "question": "Which metric is derived from the confusion matrix?",
            "options": [
                "RMSE",
                "Accuracy",
                "R²",
                "Variance"
            ],
            "correct": 1,
            "explanation": "Accuracy is used to evaluate credit card fraud detection models."
        },
        {
            "question": "In a confusion matrix, what do True Positives (TP) represent?",
            "options": [
                "Correctly predicted negatives",
                "Incorrectly predicted positives",
                "Correctly predicted positives",
                "Incorrectly predicted negatives"
            ],
            "correct": 2,
            "explanation": "Correctly diagnosing patients with cancer."
        },
        {
            "question": "Which of the following measures model sensitivity?",
            "options": [
                "TP / (TP+FN)",
                "TN / (TN+FP)",
                "TP / (TP+FP)",
                "(TP+TN) / Total"
            ],
            "correct": 0,
            "explanation": "Sensitivity is crucial in medical diagnosis to minimize false negatives."
        },
        {
            "question": "Specificity is defined as:",
            "options": [
                "TN / (TN+FP)",
                "TP / (TP+FN)",
                "(TP+FP) / Total",
                "FN / (TP+FN)"
            ],
            "correct": 0,
            "explanation": "Specificity is important in security systems to avoid false alarms."
        },
        {
            "question": "Precision is mathematically defined as:",
            "options": [
                "TP / (TP+FP)",
                "TP / (TP+FN)",
                "TN / (TN+FP)",
                "(TP+TN) / Total"
            ],
            "correct": 0,
            "explanation": "Precision is critical in information retrieval (search engines)."
        },
        {
            "question": "Which metric combines precision and recall into one?",
            "options": [
                "Accuracy",
                "RMSE",
                "F1 Score",
                "AUC"
            ],
            "correct": 2,
            "explanation": "F1 score is used in imbalanced datasets like fraud detection."
        },
        {
            "question": "Which curve plots True Positive Rate against False Positive Rate?",
            "options": [
                "ROC Curve",
                "Precision-Recall Curve",
                "Histogram",
                "Boxplot"
            ],
            "correct": 0,
            "explanation": "ROC curve is used to evaluate medical test performance."
        },
        {
            "question": "The area under the ROC curve is known as:",
            "options": [
                "Precision",
                "Recall",
                "AUC",
                "Sensitivity"
            ],
            "correct": 2,
            "explanation": "AUC is widely used in binary classification to measure model separability."
        },
        {
            "question": "High sensitivity but low specificity means:",
            "options": [
                "Few false negatives, many false positives",
                "Many false negatives, few false positives",
                "Few true positives, many true negatives",
                "Perfect accuracy"
            ],
            "correct": 0,
            "explanation": "Screening tests catch most patients but may wrongly classify healthy people."
        },
        {
            "question": "Which metric is best when the dataset is imbalanced?",
            "options": [
                "Accuracy",
                "Precision/Recall",
                "RMSE",
                "Variance"
            ],
            "correct": 1,
            "explanation": "In fraud detection, precision-recall is more informative than accuracy."
        },
        {
            "question": "Logistic regression outputs:",
            "options": [
                "Continuous values",
                "Probabilities between 0 and 1",
                "Clusters",
                "Residuals"
            ],
            "correct": 1,
            "explanation": "Predicting churn probability for telecom customers."
        },
        {
            "question": "The threshold in classification models is used to:",
            "options": [
                "Determine cut-off for class prediction",
                "Calculate variance",
                "Measure spread",
                "Reduce features"
            ],
            "correct": 0,
            "explanation": "Threshold tuning is applied in credit approval systems."
        },
        {
            "question": "Which combination of metrics is best to evaluate binary classifiers?",
            "options": [
                "Accuracy & RMSE",
                "Precision, Recall & F1",
                "Variance & Standard Deviation",
                "R² & RMSE"
            ],
            "correct": 1,
            "explanation": "Used in spam classification where accuracy alone is misleading."
        }
        ]
    },
    "12. CrossValidation_BiasVariance_QA": {
        "title": "Cross Validation & Bias-Variance Quiz",
        "questions": [
          {
            "question": "Which of the following cross-validation methods ensures that each fold has the same proportion of class labels?",
            "options": [
                "K-Fold CV",
                "Stratified K-Fold CV",
                "Shuffle Split",
                "Leave-One-Out CV"
            ],
            "correct": 1,
            "explanation": "Used in medical diagnosis datasets to handle class imbalance."
        },
        {
            "question": "In K-Fold Cross Validation, if K=5, how many models are trained?",
            "options": [
                "1",
                "4",
                "5",
                "10"
            ],
            "correct": 2,
            "explanation": "Used in financial forecasting models to check stability."
        },
        {
            "question": "Shuffle Split Cross Validation is useful when:",
            "options": [
                "Data is imbalanced",
                "Random splits are needed",
                "Sequential patterns exist",
                "Dataset is very small"
            ],
            "correct": 1,
            "explanation": "Random train/test splits in recommender systems."
        },
        {
            "question": "Underfitting occurs when:",
            "options": [
                "Model is too complex",
                "Model learns noise",
                "Model is too simple",
                "Model generalizes well"
            ],
            "correct": 2,
            "explanation": "Using linear regression on non-linear stock market data."
        },
        {
            "question": "Overfitting occurs because:",
            "options": [
                "Lack of training",
                "Noise in data",
                "Too many epochs",
                "Too many variables"
            ],
            "correct": [1,2,3],
            "explanation": "Over-training a neural network on small medical datasets."
        },
        {
            "question": "Which plot helps visualize bias-variance tradeoff?",
            "options": [
                "Histogram",
                "Learning Curve",
                "Scatter Plot",
                "Pie Chart"
            ],
            "correct": 1,
            "explanation": "Evaluating ML models in e-commerce predictions."
        },
        {
            "question": "Best fit model lies between:",
            "options": [
                "High variance & Low bias",
                "High bias & Low variance",
                "Balanced bias and variance",
                "None"
            ],
            "correct": 2,
            "explanation": "Predicting housing prices with linear regression."
        },
        {
            "question": "Feature Engineering helps in:",
            "options": [
                "Improving accuracy",
                "Reducing dimensionality",
                "Handling categorical data",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Adding new features in fraud detection models."
        },
        {
            "question": "Label encoding is risky when:",
            "options": [
                "Classes are unordered",
                "Classes are continuous",
                "Data is small",
                "Data is large"
            ],
            "correct": 0,
            "explanation": "Incorrect encoding in gender classification."
        },
        {
            "question": "One-hot encoding is preferred when:",
            "options": [
                "Categories have order",
                "Categories are nominal",
                "Features are numeric",
                "None"
            ],
            "correct": 1,
            "explanation": "Encoding country names in travel booking data."
        },
        {
            "question": "What is the drawback of One-hot encoding?",
            "options": [
                "Data loss",
                "Adds dimensionality",
                "Reduces interpretability",
                "Causes bias"
            ],
            "correct": 1,
            "explanation": "Encoding thousands of zip codes in logistics data."
        },
        {
            "question": "Which technique can reduce overfitting?",
            "options": [
                "Adding noise",
                "Feature selection",
                "Regularization",
                "All"
            ],
            "correct": 3,
            "explanation": "Avoiding spam detection model overfitting."
        },
        {
            "question": "Variance refers to:",
            "options": [
                "Model complexity",
                "Sensitivity to noise",
                "Bias in predictions",
                "Training error"
            ],
            "correct": 1,
            "explanation": "Stock prediction model changing drastically with new data."
        },
        {
            "question": "Bias refers to:",
            "options": [
                "Error due to wrong assumptions",
                "Variability in predictions",
                "Generalization power",
                "None"
            ],
            "correct": 0,
            "explanation": "Linear model applied on non-linear disease progression."
        },
        {
            "question": "Cross-validation reduces:",
            "options": [
                "Variance",
                "Overfitting",
                "Bias",
                "None"
            ],
            "correct": 1,
            "explanation": "CV in credit scoring models to ensure robustness."
        }
        ]
    },
    "13. SVM_QA": {
        "title": "SVM Quiz",
        "questions": [
          {
            "question": "What is the main objective of SVM?",
            "options": [
                "Minimize training time",
                "Maximize the margin between classes",
                "Minimize the number of features",
                "Reduce overfitting"
            ],
            "correct": 1,
            "explanation": "SVM is used in text classification to clearly separate spam vs non-spam emails."
        },
        {
            "question": "What does the hyperplane in SVM represent?",
            "options": [
                "The decision boundary separating classes",
                "The mean of all points",
                "The point with the highest density",
                "None of the above"
            ],
            "correct": 0,
            "explanation": "Hyperplanes are applied in medical imaging to classify malignant vs benign tumors."
        },
        {
            "question": "What are support vectors?",
            "options": [
                "Points farthest from the hyperplane",
                "Points closest to the hyperplane",
                "Randomly selected training points",
                "Centroid points of each class"
            ],
            "correct": 1,
            "explanation": "In handwriting recognition, support vectors define boundaries between similar digits."
        },
        {
            "question": "What is the role of the maximum margin classifier?",
            "options": [
                "To maximize training data size",
                "To find a hyperplane with the largest margin",
                "To reduce variance",
                "To minimize standard deviation"
            ],
            "correct": 1,
            "explanation": "Used in fraud detection where classes need a clear separation."
        },
        {
            "question": "Which kernel is best for non-linear classification?",
            "options": [
                "Linear",
                "Polynomial",
                "RBF",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "RBF kernel is widely used in image classification problems; choice depends on data."
        },
        {
            "question": "In SVM, what does the C parameter control?",
            "options": [
                "Degree of polynomial kernel",
                "Trade-off between margin size and misclassification",
                "Random state of the model",
                "Number of support vectors"
            ],
            "correct": 1,
            "explanation": "In customer churn prediction, adjusting C controls tolerance for misclassified data."
        },
        {
            "question": "Which kernel is commonly used for text classification?",
            "options": [
                "Linear",
                "RBF",
                "Polynomial",
                "Sigmoid"
            ],
            "correct": 0,
            "explanation": "Linear kernel SVMs are heavily used in document categorization."
        },
        {
            "question": "What does the gamma parameter in RBF kernel control?",
            "options": [
                "Number of features",
                "Influence of a single training point",
                "Margin size",
                "Iteration count"
            ],
            "correct": 1,
            "explanation": "In facial recognition, gamma controls how far the influence of each face extends."
        },
        {
            "question": "Which of the following is true for SVM?",
            "options": [
                "Works well for both linear and non-linear data",
                "Works only for linear data",
                "Works only when data has low variance",
                "Cannot handle high-dimensional data"
            ],
            "correct": 0,
            "explanation": "SVMs are popular in bioinformatics for protein classification."
        },
        {
            "question": "Which kernel resembles a neural network activation function?",
            "options": [
                "RBF",
                "Polynomial",
                "Sigmoid",
                "Linear"
            ],
            "correct": 2,
            "explanation": "Used in hybrid models combining SVM with deep learning approaches."
        },
        {
            "question": "What is the computational complexity of training SVMs?",
            "options": [
                "Linear",
                "Quadratic or more",
                "Constant",
                "Logarithmic"
            ],
            "correct": 1,
            "explanation": "Large datasets may require approximate methods for SVM training."
        },
        {
            "question": "What is the main disadvantage of SVMs?",
            "options": [
                "Not interpretable",
                "High computational cost for large datasets",
                "Cannot handle non-linear data",
                "Cannot be combined with kernels"
            ],
            "correct": 1,
            "explanation": "For big data, SVM may be replaced with logistic regression or tree-based models."
        },
        {
            "question": "Which library in Python is used to implement SVM?",
            "options": [
                "TensorFlow",
                "sklearn.svm",
                "Numpy",
                "Pandas"
            ],
            "correct": 1,
            "explanation": "sklearn provides SVC class to implement SVM for various tasks."
        },
        {
            "question": "What is a soft margin in SVM?",
            "options": [
                "Allows some misclassification",
                "Allows only linear separation",
                "Does not use kernels",
                "Ignores support vectors"
            ],
            "correct": 0,
            "explanation": "In noisy real-world datasets like financial transactions, soft margin SVMs perform better."
        },
        {
            "question": "Why use SVM instead of logistic regression?",
            "options": [
                "Handles high-dimensional data better",
                "Easier to interpret",
                "Requires less computation",
                "Always gives higher accuracy"
            ],
            "correct": 0,
            "explanation": "Used in text mining where features are in thousands of dimensions."
        }

        ]
    },
    "14. Decision_Trees_QA": {
        "title": "Decision Trees Quiz",
        "questions": [
          {
            "question": "In a Decision Tree, the topmost node is called the:",
            "options": [
                "Internal Node",
                "Root Node",
                "Terminal Node",
                "Branch Node"
            ],
            "correct": 1,
            "explanation": "In a loan approval system, the root node could represent the most important feature, such as income."
        },
        {
            "question": "Which nodes in a decision tree represent the final outcomes?",
            "options": [
                "Root Node",
                "Internal Node",
                "Terminal Node (Leaf Node)",
                "Branch Node"
            ],
            "correct": 2,
            "explanation": "In medical diagnosis, terminal nodes represent the predicted disease based on patient symptoms."
        },
        {
            "question": "Which metric measures the impurity of a node in classification tasks?",
            "options": [
                "RMSE",
                "Gini Impurity",
                "R-squared",
                "Variance"
            ],
            "correct": 1,
            "explanation": "Used in classification models like customer churn prediction to split nodes."
        },
        {
            "question": "Entropy in Decision Trees is used to measure:",
            "options": [
                "Homogeneity of data",
                "Variance",
                "Margin width",
                "Accuracy"
            ],
            "correct": 0,
            "explanation": "In email spam filters, entropy helps in splitting based on word frequencies."
        },
        {
            "question": "Information Gain is defined as:",
            "options": [
                "Increase in bias",
                "Reduction in impurity after a split",
                "Increase in variance",
                "Depth of the tree"
            ],
            "correct": 1,
            "explanation": "Used to decide the best attribute to split in classification problems like fraud detection."
        },
        {
            "question": "Overfitting in decision trees occurs when:",
            "options": [
                "The model is too simple",
                "The model captures noise in training data",
                "Model does not train enough",
                "Features are irrelevant"
            ],
            "correct": 1,
            "explanation": "An overfitted decision tree might predict training data with 100% accuracy but fail in real test cases."
        },
        {
            "question": "Which method is used to reduce overfitting in decision trees?",
            "options": [
                "Bagging",
                "Boosting",
                "Pruning",
                "Normalization"
            ],
            "correct": 2,
            "explanation": "In product recommendation, pruning helps avoid overly complex rules."
        },
        {
            "question": "Pre-pruning involves:",
            "options": [
                "Trimming branches after training",
                "Limiting depth or minimum samples per split",
                "Removing duplicates",
                "Normalizing features"
            ],
            "correct": 1,
            "explanation": "In HR attrition models, pre-pruning avoids deep trees with biased outcomes."
        },
        {
            "question": "Post-pruning is performed:",
            "options": [
                "During tree construction",
                "After the tree is built",
                "Before splitting data",
                "Before encoding features"
            ],
            "correct": 1,
            "explanation": "In healthcare diagnostics, post-pruning avoids too many small branches that reduce interpretability."
        },
        {
            "question": "Which hyperparameter controls the maximum depth of a decision tree?",
            "options": [
                "max_depth",
                "n_estimators",
                "learning_rate",
                "criterion"
            ],
            "correct": 0,
            "explanation": "Helps avoid overfitting when predicting student performance."
        },
        {
            "question": "Which hyperparameter decides the minimum number of samples required to split an internal node?",
            "options": [
                "min_samples_leaf",
                "min_samples_split",
                "max_features",
                "max_leaf_nodes"
            ],
            "correct": 1,
            "explanation": "Ensures stability in decision-making for credit scoring models."
        },
        {
            "question": "Gini Impurity equals 0 when:",
            "options": [
                "Node is pure",
                "Node has equal classes",
                "Node is empty",
                "Tree has no root"
            ],
            "correct": 0,
            "explanation": "In spam detection, a node with only spam emails has Gini=0."
        },
        {
            "question": "Entropy is highest when:",
            "options": [
                "Data is completely homogeneous",
                "Data is evenly split among classes",
                "Node is pure",
                "Only one feature is used"
            ],
            "correct": 1,
            "explanation": "In sentiment analysis, entropy is high when reviews are equally positive and negative."
        },
        {
            "question": "Which metric is NOT used for splitting in decision trees?",
            "options": [
                "Information Gain",
                "Gini Index",
                "Variance Reduction",
                "Gradient Boost"
            ],
            "correct": 3,
            "explanation": "Gradient Boosting is a separate ensemble technique, not a splitting metric."
        },
        {
            "question": "Hyperparameters like max_features and max_depth help to:",
            "options": [
                "Increase overfitting",
                "Control complexity of the model",
                "Ignore irrelevant features",
                "Reduce entropy"
            ],
            "correct": 1,
            "explanation": "In weather forecasting, limiting features prevents noise from dominating."
        }
        ]
    },
    "15. Ensemble_Methods_QA": {
        "title": "Ensemble Methods Quiz",
        "questions": [
           {
            "question": "Which of the following is an example of a bagging method?",
            "options": [
                "Gradient Boosting",
                "Random Forest",
                "AdaBoost",
                "XGBoost"
            ],
            "correct": 1,
            "explanation": "Used in credit scoring to reduce variance and avoid overfitting."
        },
        {
            "question": "Bagging primarily helps to reduce:",
            "options": [
                "Bias",
                "Variance",
                "Both Bias and Variance",
                "None"
            ],
            "correct": 1,
            "explanation": "In stock market trend prediction, bagging stabilizes model predictions."
        },
        {
            "question": "In Random Forest, each tree is trained on:",
            "options": [
                "The full dataset",
                "A bootstrap sample",
                "Weighted sample",
                "Sequential data"
            ],
            "correct": 1,
            "explanation": "Healthcare diagnostics use bootstrap aggregation for stable predictions."
        },
        {
            "question": "What hyperparameter in Random Forest helps control overfitting?",
            "options": [
                "Number of trees",
                "Maximum depth",
                "Learning rate",
                "Gamma"
            ],
            "correct": 1,
            "explanation": "In fraud detection, limiting tree depth avoids overfitting to anomalies."
        },
        {
            "question": "Gradient Boosting works by:",
            "options": [
                "Averaging models",
                "Combining residuals sequentially",
                "Random selection",
                "Feature bagging"
            ],
            "correct": 1,
            "explanation": "In sales forecasting, it iteratively improves weak learners."
        },
        {
            "question": "AdaBoost assigns more weight to:",
            "options": [
                "Easy samples",
                "Misclassified samples",
                "Random samples",
                "Balanced samples"
            ],
            "correct": 1,
            "explanation": "In face detection, misclassified images are given higher weight."
        },
        {
            "question": "Which boosting method is optimized for speed and memory efficiency?",
            "options": [
                "AdaBoost",
                "Gradient Boosting",
                "LightGBM",
                "XGBoost"
            ],
            "correct": 2,
            "explanation": "Used in large-scale click-through rate prediction in ads."
        },
        {
            "question": "XGBoost stands for:",
            "options": [
                "Extreme Gradient Boosting",
                "Extended Gradient Boosting",
                "Xtra Gradient Boosting",
                "None"
            ],
            "correct": 0,
            "explanation": "Widely used in Kaggle competitions for structured data challenges."
        },
        {
            "question": "Which method handles categorical features natively?",
            "options": [
                "AdaBoost",
                "LightGBM",
                "Gradient Boosting",
                "Random Forest"
            ],
            "correct": 1,
            "explanation": "E-commerce product recommendation systems use LightGBM for mixed data."
        },
        {
            "question": "Bagging reduces variance while boosting reduces:",
            "options": [
                "Variance",
                "Bias",
                "Noise",
                "Dimensionality"
            ],
            "correct": 1,
            "explanation": "Boosting improves weak learners in medical risk predictions."
        },
        {
            "question": "What parameter in Gradient Boosting controls overfitting?",
            "options": [
                "Learning rate",
                "Number of epochs",
                "Batch size",
                "Random seed"
            ],
            "correct": 0,
            "explanation": "In insurance claim prediction, low learning rate prevents overfitting."
        },
        {
            "question": "Random Forest improves over Decision Trees by:",
            "options": [
                "Pruning",
                "Bagging multiple trees",
                "Sequential learning",
                "Increasing variance"
            ],
            "correct": 1,
            "explanation": "Used in credit scoring to stabilize predictions compared to single tree."
        },
        {
            "question": "AdaBoost stops when:",
            "options": [
                "All samples classified correctly",
                "Max iterations reached",
                "Error threshold met",
                "Both A & B"
            ],
            "correct": 3,
            "explanation": "In spam detection, it iterates until misclassifications reduce significantly."
        },
        {
            "question": "Which ensemble method can be parallelized easily?",
            "options": [
                "Bagging",
                "AdaBoost",
                "Gradient Boosting",
                "LightGBM"
            ],
            "correct": 0,
            "explanation": "Weather prediction models use bagging for parallel processing efficiency."
        },
        {
            "question": "In LightGBM, leaf-wise tree growth can cause:",
            "options": [
                "Faster convergence",
                "Overfitting",
                "Better accuracy",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "High-frequency trading models use LightGBM for fast, accurate decisions."
        }
        ]
    },
    "16. Dimensional_Reduction_QA": {
        "title": "Dimensional Reduction Quiz",
        "questions": [
          {
            "question": "What is the main purpose of Dimensional Reduction?",
            "options": [
                "To increase computation time",
                "To reduce redundancy and noise",
                "To add more features",
                "To increase dataset size"
            ],
            "correct": 1,
            "explanation": "In image recognition, PCA reduces image dimensions while retaining important features."
        },
        {
            "question": "PCA is mainly used for:",
            "options": [
                "Feature extraction",
                "Data duplication",
                "Data labeling",
                "Outlier removal"
            ],
            "correct": 0,
            "explanation": "Used in face recognition systems to extract essential features for classification."
        },
        {
            "question": "What mathematical concept is the foundation of PCA?",
            "options": [
                "Linear regression",
                "Eigenvectors and Eigenvalues",
                "Decision trees",
                "Random forests"
            ],
            "correct": 1,
            "explanation": "In genetics, PCA helps reduce SNP (Single Nucleotide Polymorphism) data."
        },
        {
            "question": "In PCA, Eigenvectors represent:",
            "options": [
                "Directions of maximum variance",
                "Magnitude of data points",
                "Mean of dataset",
                "Noise in data"
            ],
            "correct": 0,
            "explanation": "In marketing, PCA helps identify customer buying patterns."
        },
        {
            "question": "What does Eigenvalue represent in PCA?",
            "options": [
                "Noise factor",
                "Importance of a principal component",
                "Random variability",
                "Sample size"
            ],
            "correct": 1,
            "explanation": "In finance, PCA reduces correlated stock indicators into fewer variables."
        },
        {
            "question": "PCA is especially useful when:",
            "options": [
                "Features are highly correlated",
                "Dataset is small",
                "Dataset is error-free",
                "There are no patterns"
            ],
            "correct": 0,
            "explanation": "Used in medical imaging to reduce dimensions while keeping diagnostic info."
        },
        {
            "question": "Which of the following is NOT an advantage of PCA?",
            "options": [
                "Reduces computational cost",
                "Improves visualization",
                "Adds more redundancy",
                "Removes correlated features"
            ],
            "correct": 2,
            "explanation": "PCA helps visualize high-dimensional stock market trends in 2D/3D plots."
        },
        {
            "question": "PCA transforms original variables into:",
            "options": [
                "Independent principal components",
                "Dependent features",
                "Noise factors",
                "Random features"
            ],
            "correct": 0,
            "explanation": "Speech recognition systems use PCA to reduce sound feature space."
        },
        {
            "question": "PCA works best with:",
            "options": [
                "Normalized data",
                "Raw unprocessed data",
                "Sparse data only",
                "Binary encoded data"
            ],
            "correct": 0,
            "explanation": "PCA improves machine learning models in credit scoring."
        },
        {
            "question": "What is a disadvantage of PCA?",
            "options": [
                "Loss of interpretability",
                "Increases redundancy",
                "Slows training",
                "Reduces noise"
            ],
            "correct": 0,
            "explanation": "In healthcare, PCA reduces clinical dataset features but sometimes loses meaning."
        },
        {
            "question": "PCA is often applied before:",
            "options": [
                "Clustering",
                "Noise addition",
                "Outlier removal",
                "Randomization"
            ],
            "correct": 0,
            "explanation": "PCA is used before K-Means clustering to reduce feature space."
        },
        {
            "question": "The number of principal components chosen depends on:",
            "options": [
                "Total variance explained",
                "Random choice",
                "Outlier count",
                "Dataset size"
            ],
            "correct": 0,
            "explanation": "In IoT, PCA is used to compress sensor readings."
        },
        {
            "question": "PCA reduces dimensionality by projecting data onto:",
            "options": [
                "Lower-dimensional subspace",
                "Original feature space",
                "Noise axis",
                "Decision boundaries"
            ],
            "correct": 0,
            "explanation": "Used in fraud detection to reduce transaction dataset size."
        },
        {
            "question": "Eigen decomposition is applied on:",
            "options": [
                "Covariance matrix",
                "Raw dataset",
                "Frequency table",
                "Histogram"
            ],
            "correct": 0,
            "explanation": "In stock market analysis, PCA helps find uncorrelated indicators."
        },
        {
            "question": "Which library is commonly used in Python for PCA?",
            "options": [
                "pandas",
                "scikit-learn",
                "matplotlib",
                "seaborn"
            ],
            "correct": 1,
            "explanation": "scikit-learn PCA implementation reduces features in ML pipelines."
        }
        ]
    },
    "17. Clustering_QA": {
        "title": "Clustering Quiz",
        "questions": [
          {
            "question": "What is clustering mainly used for?",
            "options": [
                "Supervised classification",
                "Grouping unlabeled data",
                "Regression analysis",
                "Feature scaling"
            ],
            "correct": 1,
            "explanation": "Customer segmentation in marketing."
        },
        {
            "question": "Which of the following is a distance metric commonly used in clustering?",
            "options": [
                "Cosine Similarity",
                "Euclidean Distance",
                "Manhattan Distance",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Image recognition using Euclidean distance, Manhattan distance, or Cosine similarity."
        },
        {
            "question": "K-means clustering aims to:",
            "options": [
                "Minimize within-cluster variance",
                "Maximize between-cluster variance",
                "Both A and B",
                "None"
            ],
            "correct": 2,
            "explanation": "Grouping customers by purchasing behavior."
        },
        {
            "question": "DBSCAN stands for:",
            "options": [
                "Density-Based Spatial Clustering of Applications with Noise",
                "Data-Based Spatial Classification and Normalization",
                "Distance-Based Similarity Clustering Algorithm",
                "None"
            ],
            "correct": 0,
            "explanation": "Detecting fraud transactions in banking data."
        },
        {
            "question": "The Elbow Method is used for:",
            "options": [
                "Choosing the number of clusters",
                "Reducing noise",
                "Measuring correlation",
                "Normalization"
            ],
            "correct": 0,
            "explanation": "Identifying ideal groups in sales data."
        },
        {
            "question": "Silhouette score measures:",
            "options": [
                "Compactness and separation of clusters",
                "Accuracy of classification",
                "Correlation of variables",
                "Data normalization"
            ],
            "correct": 0,
            "explanation": "Evaluating quality of clustering in healthcare datasets."
        },
        {
            "question": "In K-means, centroids are:",
            "options": [
                "Random points in dataset",
                "Mean of cluster points",
                "Outliers",
                "None"
            ],
            "correct": 1,
            "explanation": "Defining central behavior of groups in telecom churn analysis."
        },
        {
            "question": "DBSCAN differs from K-means because:",
            "options": [
                "It requires specifying number of clusters",
                "It can find clusters of arbitrary shape",
                "It is supervised",
                "None"
            ],
            "correct": 1,
            "explanation": "Identifying clusters in geospatial data."
        },
        {
            "question": "Outliers in DBSCAN are labeled as:",
            "options": [
                "Core points",
                "Border points",
                "Noise points",
                "Centroids"
            ],
            "correct": 2,
            "explanation": "Fraudulent credit card transaction detection."
        },
        {
            "question": "Which algorithm works better for large, spherical clusters?",
            "options": [
                "K-means",
                "DBSCAN",
                "Hierarchical",
                "Regression"
            ],
            "correct": 0,
            "explanation": "Market basket analysis in retail."
        },
        {
            "question": "Which distance metric is sensitive to scale?",
            "options": [
                "Manhattan",
                "Euclidean",
                "Cosine",
                "Jaccard"
            ],
            "correct": 1,
            "explanation": "Pattern recognition in scaled datasets."
        },
        {
            "question": "Clustering can be applied in which domain?",
            "options": [
                "Marketing",
                "Healthcare",
                "Image recognition",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Patient group classification in healthcare."
        },
        {
            "question": "Which is a limitation of K-means?",
            "options": [
                "Sensitive to outliers",
                "Requires predefined clusters",
                "Works only with spherical clusters",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Inconsistent segmentation in noisy datasets."
        },
        {
            "question": "Which clustering method is density-based?",
            "options": [
                "K-means",
                "DBSCAN",
                "Hierarchical",
                "PCA"
            ],
            "correct": 1,
            "explanation": "Cluster formation in anomaly detection."
        },
        {
            "question": "Elbow method is based on which metric?",
            "options": [
                "SSE (Sum of Squared Errors)",
                "Accuracy",
                "Precision",
                "Recall"
            ],
            "correct": 0,
            "explanation": "Optimal cluster selection in customer profiling."
        }
        ]
    },
    "18. Recommendation_Systems_QA": {
        "title": "Recommendation Systems Quiz",
        "questions": [
          {
            "question": "What is the main purpose of a recommendation system?",
            "options": [
                "To replace search engines",
                "To suggest relevant items to users",
                "To store user data",
                "To monitor user activities"
            ],
            "correct": 1,
            "explanation": "Netflix recommends movies based on your watch history."
        },
        {
            "question": "Why are recommendation systems important in business?",
            "options": [
                "They increase user engagement",
                "They personalize the customer experience",
                "They help boost sales",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "Amazon product recommendations increase sales conversions."
        },
        {
            "question": "Which of the following is an example of Collaborative Filtering?",
            "options": [
                "Suggesting movies based on similar users' ratings",
                "Suggesting movies based on the movie’s genre",
                "Suggesting items based on metadata",
                "None"
            ],
            "correct": 0,
            "explanation": "Spotify suggests songs based on other users with similar tastes."
        },
        {
            "question": "Which of the following is an example of Content-Based Filtering?",
            "options": [
                "Recommending books based on user’s previous choices",
                "Recommending trending products to everyone",
                "Recommending items randomly",
                "None"
            ],
            "correct": 0,
            "explanation": "Goodreads recommends similar books based on genres you liked."
        },
        {
            "question": "Which of these is a limitation of Collaborative Filtering?",
            "options": [
                "Cold start problem",
                "Requires large data",
                "Scalability issues",
                "All of the above"
            ],
            "correct": 3,
            "explanation": "A new user on Netflix won’t get good recommendations initially."
        }
        ]
    },
    "19. TimeSeries_QA": {
        "title": "Time Series Quiz",
        "questions": [
          {
            "question": "Which of the following is NOT a component of time series?",
            "options": ["Trend", "Seasonality", "Regression", "Cyclic"],
            "correct": 2,
            "explanation": "Regression is a modeling technique, not a direct component. Example: Electricity consumption shows trend + seasonality."
        },
        {
            "question": "A trend in time series refers to:",
            "options": ["Long-term movement in data", "Random variation", "Seasonal fluctuation", "Outliers only"],
            "correct": 0,
            "explanation": "Stock market indices showing upward trend over years."
        },
        {
            "question": "Which visualization best identifies seasonality in time series?",
            "options": ["Histogram", "Seasonal Plot", "Scatter Plot", "Heatmap"],
            "correct": 1,
            "explanation": "Retail sales showing spikes during festive months."
        },
        {
            "question": "Lag plots are used to:",
            "options": ["Identify randomness", "Identify correlation with past values", "Forecast trends", "Detect anomalies only"],
            "correct": 1,
            "explanation": "Autocorrelation in stock returns."
        },
        {
            "question": "ARIMA stands for:",
            "options": ["Auto-Regressive Integrated Moving Average", "Automated Regression Internal Model Approach", "Analytical Regression Integrated Model Application", "None of the above"],
            "correct": 0,
            "explanation": "Forecasting airline passengers."
        },
        {
            "question": "Which Python library provides ARIMA implementation?",
            "options": ["Matplotlib", "Statsmodels", "Seaborn", "Scikit-learn"],
            "correct": 1,
            "explanation": "statsmodels.tsa.arima_model.ARIMA."
        },
        {
            "question": "The 'Integrated' part of ARIMA refers to:",
            "options": ["Differencing data to remove trend", "Combining models", "Seasonal adjustment", "Regression correction"],
            "correct": 0,
            "explanation": "Converting non-stationary series to stationary."
        },
        {
            "question": "Which metric is commonly used to evaluate ARIMA model?",
            "options": ["RMSE", "R²", "Precision", "Recall"],
            "correct": 0,
            "explanation": "Forecast accuracy in weather prediction."
        },
        {
            "question": "Which of the following is an assumption of ARIMA?",
            "options": ["Data should be stationary", "Data must be normally distributed", "No autocorrelation", "Features must be independent"],
            "correct": 0,
            "explanation": "GDP growth after differencing."
        },
        {
            "question": "ACF and PACF plots are used for:",
            "options": ["Parameter selection in ARIMA", "Detecting anomalies", "Normalization", "Partitioning data"],
            "correct": 0,
            "explanation": "Identifying AR (p) and MA (q) parameters."
        },
        {
            "question": "Seasonal ARIMA is denoted as:",
            "options": ["SARIMA(p,d,q)(P,D,Q,s)", "ARIMA(p,d,q)", "AR(p) + MA(q)", "ARIMA++"],
            "correct": 0,
            "explanation": "Airline passengers dataset."
        },
        {
            "question": "In time series partition, why do we avoid random shuffling?",
            "options": ["It loses temporal order", "It improves variance", "It increases bias", "It is mandatory"],
            "correct": 0,
            "explanation": "Train-test split must follow time sequence."
        },
        {
            "question": "Which distance metric is often used in time series clustering?",
            "options": ["Euclidean", "Manhattan", "Dynamic Time Warping", "Cosine"],
            "correct": 2,
            "explanation": "Comparing ECG signals."
        },
        {
            "question": "Residual component in time series represents:",
            "options": ["Random variation left after removing trend & seasonality", "Trend", "Seasonality", "Outliers only"],
            "correct": 0,
            "explanation": "Unexpected economic shock impact."
        },
        {
            "question": "Which function in pandas is commonly used to parse dates for time series?",
            "options": ["pd.read_csv(..., parse_dates=True)", "pd.plot()", "pd.groupby()", "pd.merge()"],
            "correct": 0,
            "explanation": "Reading stock price data with Date index."
        }
        ]
    },
    "20. NeuralNetworks_QA": {
        "title": "Neural Networks Quiz",
        "questions": [
          {
            "question": "What does a perceptron do in neural networks?",
            "options": ["Classifies linearly separable data", "Performs clustering", "Normalizes data", "Reduces dimensions"],
            "correct": 0,
            "explanation": "Real-time example: Email spam classification."
        },
        {
            "question": "Which activation function is most suitable for binary classification?",
            "options": ["ReLU", "Sigmoid", "Tanh", "Softmax"],
            "correct": 1,
            "explanation": "Predicting yes/no outcomes like fraud detection."
        },
        {
            "question": "Which function introduces non-linearity in neural networks?",
            "options": ["Loss function", "Activation function", "Optimizer", "Gradient"],
            "correct": 1,
            "explanation": "ReLU helps in image classification tasks."
        },
        {
            "question": "Backpropagation is used to:",
            "options": ["Initialize weights", "Update weights", "Compute bias", "None"],
            "correct": 1,
            "explanation": "Training speech recognition models."
        },
        {
            "question": "Which optimizer is widely used for deep learning due to adaptive learning rate?",
            "options": ["SGD", "Adam", "RMSProp", "Adagrad"],
            "correct": 1,
            "explanation": "Used in NLP models like BERT."
        },
        {
            "question": "Gradient descent minimizes:",
            "options": ["Accuracy", "Loss function", "Activation", "Data variance"],
            "correct": 1,
            "explanation": "Reducing error in predicting house prices."
        },
        {
            "question": "Softmax activation is generally used for:",
            "options": ["Regression", "Multi-class classification", "Clustering", "Binary classification"],
            "correct": 1,
            "explanation": "Handwritten digit recognition (0-9)."
        },
        {
            "question": "The perceptron can fail when:",
            "options": ["Data is noisy", "Data is non-linear", "Too many layers are used", "Both A & B"],
            "correct": 3,
            "explanation": "XOR problem can't be solved by a single perceptron."
        },
        {
            "question": "What is the main drawback of sigmoid activation?",
            "options": ["Exploding gradient", "Vanishing gradient", "High variance", "Overfitting"],
            "correct": 1,
            "explanation": "Deep neural nets failing to learn."
        },
        {
            "question": "Which optimizer works best with sparse data?",
            "options": ["Adam", "RMSProp", "Adagrad", "SGD"],
            "correct": 2,
            "explanation": "NLP models with large vocabularies."
        },
        {
            "question": "In gradient descent, learning rate controls:",
            "options": ["Step size", "Epochs", "Bias initialization", "Batch size"],
            "correct": 0,
            "explanation": "Small rate → slow learning, Large rate → divergence."
        },
        {
            "question": "A multilayer perceptron (MLP) differs from a single perceptron by:",
            "options": ["Having biases", "Multiple hidden layers", "Linear outputs", "No activation"],
            "correct": 1,
            "explanation": "Image recognition tasks."
        },
        {
            "question": "Which optimizer combines momentum with adaptive learning?",
            "options": ["Adam", "SGD", "RMSProp", "Adadelta"],
            "correct": 0,
            "explanation": "Deep CNNs for medical image analysis."
        },
        {
            "question": "ReLU activation outputs:",
            "options": ["0 to 1", "-1 to 1", "0 or positive values", "Only integers"],
            "correct": 2,
            "explanation": "Object detection in images."
        },
        {
            "question": "Which ANN method updates weights layer by layer backwards?",
            "options": ["Forward propagation", "Backpropagation", "Gradient descent", "Dropout"],
            "correct": 1,
            "explanation": "Training Google Translate models."
        }
        ]
    },
    "21. RNN_LSTM_GRU_QA": {
        "title": "RNN, LSTM & GRU Quiz",
        "questions": [
          {
            "question": "Which of the following is a key use case of RNNs?",
            "options": [
                "Image classification",
                "Time series forecasting",
                "Object detection",
                "Clustering"
            ],
            "correct": 1,
            "explanation": "Time series forecasting. Real-time application: Stock market prediction using past trends."
        },
        {
            "question": "What problem occurs in RNNs due to long sequences?",
            "options": [
                "Overfitting",
                "Vanishing/Exploding gradients",
                "Data leakage",
                "Bias-variance tradeoff"
            ],
            "correct": 1,
            "explanation": "Vanishing/Exploding gradients. Real-time application: Long text processing like document translation."
        },
        {
            "question": "In vanishing gradients, weights become:",
            "options": [
                "Too large",
                "Too small",
                "Negative always",
                "Constant"
            ],
            "correct": 1,
            "explanation": "Too small. Real-time example: RNNs failing to learn dependencies in long customer behavior logs."
        },
        {
            "question": "Exploding gradients can be handled using:",
            "options": [
                "Dropout",
                "Gradient clipping",
                "Early stopping",
                "Normalization"
            ],
            "correct": 1,
            "explanation": "Gradient clipping. Real-time application: Training RNNs for speech recognition without instability."
        },
        {
            "question": "What is the main difference between LSTM and vanilla RNN?",
            "options": [
                "LSTM uses convolution layers",
                "LSTM has gates for memory control",
                "LSTM is unsupervised",
                "LSTM uses clustering"
            ],
            "correct": 1,
            "explanation": "LSTM has gates for memory control. Real-time application: Sentiment analysis in long reviews."
        },
        {
            "question": "Which of the following is NOT an LSTM gate?",
            "options": [
                "Input gate",
                "Forget gate",
                "Update gate",
                "Output gate"
            ],
            "correct": 2,
            "explanation": "Update gate. Real-time example: Update gate belongs to GRU, not LSTM."
        },
        {
            "question": "GRU differs from LSTM by:",
            "options": [
                "Using more gates",
                "Having fewer gates",
                "No recurrent connections",
                "Larger memory cells"
            ],
            "correct": 1,
            "explanation": "Having fewer gates. Real-time application: Faster text classification in chatbots."
        },
        {
            "question": "Which gate in LSTM decides what information to discard?",
            "options": [
                "Input gate",
                "Forget gate",
                "Output gate",
                "Reset gate"
            ],
            "correct": 1,
            "explanation": "Forget gate. Real-time application: Ignoring irrelevant context in language translation."
        },
        {
            "question": "A practical application of GRU is:",
            "options": [
                "Forecasting electricity demand",
                "Object detection in images",
                "Sorting customer IDs",
                "Clustering music files"
            ],
            "correct": 0,
            "explanation": "Forecasting electricity demand."
        },
        {
            "question": "What is the key similarity between LSTM and GRU?",
            "options": [
                "Both use gates for memory management",
                "Both are feedforward",
                "Both use convolution layers",
                "Both are unsupervised"
            ],
            "correct": 0,
            "explanation": "Both use gates for memory management. Real-time example: Text-to-speech systems."
        }
        ]
    },
    "22. Text_Data_QA": {
        "title": "Text Data Quiz",
        "questions": [
          {
            "question": "What is Text Data?",
            "options": [
                "Data in numerical form",
                "Data in unstructured linguistic form",
                "Tabular data only",
                "Graphical data"
            ],
            "correct": 1,
            "explanation": "Data in unstructured linguistic form. Application: Emails, social media posts, product reviews are text data."
        },
        {
            "question": "Which is NOT a form of text data?",
            "options": [
                "Documents",
                "Audio files",
                "Tweets",
                "Articles"
            ],
            "correct": 1,
            "explanation": "Audio files. Application: Tweets and product reviews are common text data forms."
        },
        {
            "question": "What is Tokenization?",
            "options": [
                "Removing stopwords",
                "Splitting text into smaller units (words)",
                "Lemmatizing words",
                "Counting word frequencies"
            ],
            "correct": 1,
            "explanation": "Splitting text into smaller units (words). Application: Tokenization helps break sentences for text mining tasks."
        },
        {
            "question": "Which preprocessing step reduces words to base dictionary form?",
            "options": [
                "Stemming",
                "Lemmatization",
                "Normalization",
                "Tokenization"
            ],
            "correct": 1,
            "explanation": "'Lemmatization'. Application: 'Running' → 'Run' using WordNet Lemmatizer in NLP tasks."
        },
        {
            "question": "What is the purpose of removing stopwords?",
            "options": [
                "To increase dataset size",
                "To reduce noise by removing common words",
                "To add punctuation",
                "To normalize case"
            ],
            "correct": 1,
            "explanation": "To reduce noise by removing common words. Application: Improves sentiment classification accuracy by ignoring irrelevant words."
        },
        {
            "question": "What is Bag of Words (BoW)?",
            "options": [
                "Statistical model to represent text as word counts",
                "Sequence model",
                "Topic modeling technique",
                "Deep learning algorithm"
            ],
            "correct": 0,
            "explanation": "Statistical model to represent text as word counts. Application: Spam detection models often use BoW."
        },
        {
            "question": "What does TF in TF-IDF stand for?",
            "options": [
                "Total Frequency",
                "Term Frequency",
                "Token Factor",
                "True Frequency"
            ],
            "correct": 1,
            "explanation": "Term Frequency. Application: Used in search engines to rank results based on relevance."
        },
        {
            "question": "What does IDF in TF-IDF represent?",
            "options": [
                "Inverse Data Factor",
                "Inverse Document Frequency",
                "Internal Data Function",
                "Indexed Data Frame"
            ],
            "correct": 1,
            "explanation": "Inverse Document Frequency. Application: Helps reduce weight of common words like 'the' in text mining."
        },
        {
            "question": "Which visualization is commonly used for text analysis?",
            "options": [
                "Line chart",
                "Word Cloud",
                "Histogram",
                "Scatter plot"
            ],
            "correct": 1,
            "explanation": "Word Cloud. Application: Word Clouds visualize most frequent words in customer reviews."
        },
        {
            "question": "Which step converts all text to lowercase?",
            "options": [
                "Normalization",
                "Tokenization",
                "Lemmatization",
                "Stemming"
            ],
            "correct": 0,
            "explanation": "Normalization. Application: Ensures 'Dog' and 'dog' are treated equally in sentiment models."
        },
        {
            "question": "What is Stemming?",
            "options": [
                "Splitting sentences",
                "Removing common words",
                "Reducing words to root form",
                "Counting tokens"
            ],
            "correct": 2,
            "explanation": "Reducing words to root form. Application: 'Playing' → 'Play' used in search engines to improve retrieval."
        },
        {
            "question": "Which metric evaluates sentiment polarity in text?",
            "options": [
                "RMSE",
                "Sentiment Score",
                "TF-IDF",
                "Cosine Similarity"
            ],
            "correct": 1,
            "explanation": "Sentiment Score. Application: Used in social media monitoring for brand reputation."
        },
        {
            "question": "Which preprocessing technique helps handle synonyms better?",
            "options": [
                "Stemming",
                "Lemmatization",
                "Normalization",
                "Tokenization"
            ],
            "correct": 1,
            "explanation": "Lemmatization. Application: Useful in chatbot NLP pipelines to maintain context."
        },
        {
            "question": "What is Sentiment Analysis?",
            "options": [
                "Identifying emotions in text",
                "Counting words",
                "Removing punctuation",
                "Normalizing data"
            ],
            "correct": 0,
            "explanation": "Identifying emotions in text. Application: Used in analyzing customer reviews for positive/negative opinions."
        },
        {
            "question": "Which representation technique weighs words based on importance across documents?",
            "options": [
                "BoW",
                "TF-IDF",
                "Sentiment Score",
                "Cosine Similarity"
            ],
            "correct": 1,
            "explanation": "TF-IDF. Application: Used by Google search to rank documents based on relevance."
        }
        ]
    },
    "23. NER_WordEmbedding_LanguageModeling_QA": {
        "title": "NER, Word Embedding & Language Modeling Quiz",
        "questions": [
          {
            "question": "What is Named Entity Recognition (NER)?",
            "options": [
                "Identifying relations between words",
                "Identifying named entities like persons, places",
                "Identifying stopwords",
                "Identifying part of speech"
            ],
            "correct": 1,
            "explanation": "Identifying named entities like persons, places. Real-time Application: Extracting people and organization names from news articles."
        },
        {
            "question": "Which of the following is NOT a named entity type commonly recognized by NER systems?",
            "options": [
                "Person",
                "Location",
                "Organization",
                "Stopword"
            ],
            "correct": 3,
            "explanation": "Stopword. Real-time Application: Legal document analysis to identify company names."
        },
        {
            "question": "What is Word Embedding?",
            "options": [
                "Representation of text in sparse vectors",
                "Representation of words in dense vector space",
                "Representation of documents only",
                "Representation of data in tables"
            ],
            "correct": 1,
            "explanation": "Representation of words in dense vector space. Real-time Application: Sentiment analysis in customer reviews."
        },
        {
            "question": "Which is a pre-trained word embedding model?",
            "options": [
                "Word2Vec",
                "TF-IDF",
                "Count Vectorization",
                "Bag of Words"
            ],
            "correct": 0,
            "explanation": "Word2Vec. Real-time Application: Chatbots using Word2Vec embeddings."
        },
        {
            "question": "Word2Vec Skip-gram model predicts:",
            "options": [
                "Context from target word",
                "Target word from context",
                "Document from sentence",
                "Sentence from word"
            ],
            "correct": 0,
            "explanation": "Context from target word. Real-time Application: Predicting similar words in search engines."
        },
        {
            "question": "CBOW model in Word2Vec predicts:",
            "options": [
                "Target word from surrounding context",
                "Context from target word",
                "Document from context",
                "Vector from text"
            ],
            "correct": 0,
            "explanation": "Target word from surrounding context. Real-time Application: Autocomplete in search queries."
        },
        {
            "question": "Eigenvectors in word embedding space represent:",
            "options": [
                "Random directions",
                "Directions of maximum variance",
                "Stopwords",
                "Clustering only"
            ],
            "correct": 1,
            "explanation": "Directions of maximum variance. Real-time Application: Dimensionality reduction for NLP tasks."
        },
        {
            "question": "N-gram models capture:",
            "options": [
                "Word meaning",
                "Word co-occurrence",
                "Document similarity",
                "Embedding density"
            ],
            "correct": 1,
            "explanation": "Word co-occurrence. Real-time Application: Predicting next word in SMS keyboards."
        },
        {
            "question": "The problem with N-gram models is:",
            "options": [
                "High memory requirement",
                "Low accuracy",
                "No sequence modeling",
                "No embeddings"
            ],
            "correct": 0,
            "explanation": "High memory requirement. Real-time Application: Limited use in large corpora."
        },
        {
            "question": "Neural Language Models overcome N-gram issues using:",
            "options": [
                "Count tables",
                "Dense vectors & neural nets",
                "TF-IDF",
                "One-hot encoding"
            ],
            "correct": 1,
            "explanation": "Dense vectors & neural nets. Real-time Application: Google Translate."
        },
        {
            "question": "RNNs are suitable for:",
            "options": [
                "Independent data",
                "Sequential data",
                "Tabular data",
                "Images only"
            ],
            "correct": 1,
            "explanation": "Sequential data. Real-time Application: Speech recognition systems."
        },
        {
            "question": "LSTM is better than RNN because:",
            "options": [
                "Simple structure",
                "Handles vanishing gradient",
                "Works only with small data",
                "Requires no training"
            ],
            "correct": 1,
            "explanation": "Handles vanishing gradient. Real-time Application: Stock price prediction."
        },
        {
            "question": "GRU vs LSTM difference is:",
            "options": [
                "GRU has fewer gates",
                "LSTM has more hidden layers",
                "GRU is slower",
                "Both are same"
            ],
            "correct": 0,
            "explanation": "GRU has fewer gates. Real-time Application: Real-time recommendation engines."
        },
        {
            "question": "TF-IDF differs from BoW because:",
            "options": [
                "It uses weights",
                "It counts words",
                "It ignores frequency",
                "It has no features"
            ],
            "correct": 0,
            "explanation": "It uses weights. Real-time Application: Spam detection in emails."
        },
        {
            "question": "A real-time application of NER is:",
            "options": [
                "Identifying stopwords",
                "Extracting named entities from resumes",
                "Counting words",
                "Sorting words"
            ],
            "correct": 1,
            "explanation": "Extracting named entities from resumes. Real-time Application: Resume shortlisting."
        }
        ]
    },
    "24. LLM_Transformers_QA": {
        "title": "LLM & Transformers Quiz",
        "questions": [
          {
            "question": "What is the primary characteristic of Large Language Models (LLMs)?",
            "options": [
                "Small training data",
                "Few parameters",
                "Billions of parameters trained on vast text corpora",
                "Limited vocabulary"
            ],
            "correct": 2,
            "explanation": "Billions of parameters trained on vast text corpora. Real-time Application: LLMs like GPT are used in chatbots, customer support automation, and content generation."
        },
        {
            "question": "Which of the following is a benefit of Transfer Learning in NLP?",
            "options": [
                "Reduces the need for large labeled datasets",
                "Always requires training from scratch",
                "Increases model complexity unnecessarily",
                "Eliminates the need for tokenization"
            ],
            "correct": 0,
            "explanation": "Reduces the need for large labeled datasets. Real-time Application: Transfer learning allows fine-tuning BERT for sentiment analysis in movie reviews with fewer labeled examples."
        },
        {
            "question": "Pre-trained NLP models are trained on:",
            "options": [
                "Only numeric datasets",
                "Large general-purpose text corpora",
                "Audio signals",
                "Image datasets"
            ],
            "correct": 1,
            "explanation": "Large general-purpose text corpora. Real-time Application: Pre-trained BERT is fine-tuned for question-answering tasks in customer FAQs."
        },
        {
            "question": "Which architecture underpins transformers?",
            "options": [
                "CNN",
                "RNN",
                "Attention mechanism",
                "Decision trees"
            ],
            "correct": 2,
            "explanation": "Attention mechanism. Real-time Application: Transformers power machine translation tools like Google Translate."
        },
        {
            "question": "Hugging Face library is mainly used for:",
            "options": [
                "Game development",
                "NLP and transformer-based models",
                "Image recognition",
                "Database queries"
            ],
            "correct": 1,
            "explanation": "NLP and transformer-based models. Real-time Application: Hugging Face provides APIs for summarization, translation, and sentiment analysis."
        },
        {
            "question": "What does 'fine-tuning' mean in transfer learning?",
            "options": [
                "Training from scratch",
                "Adjusting a pre-trained model on domain-specific data",
                "Removing layers from a model",
                "Changing activation functions"
            ],
            "correct": 1,
            "explanation": "Adjusting a pre-trained model on domain-specific data. Real-time Application: Fine-tuning GPT for legal document summarization."
        },
        {
            "question": "Which is NOT an example of a pre-trained transformer model?",
            "options": [
                "BERT",
                "GPT",
                "RoBERTa",
                "Naïve Bayes"
            ],
            "correct": 3,
            "explanation": "Naïve Bayes. Real-time Application: BERT and GPT are widely used in conversational AI."
        },
        {
            "question": "The transformer architecture solves which limitation of RNNs?",
            "options": [
                "High accuracy",
                "Handling sequential dependencies",
                "Parallelization and long-range dependencies",
                "Reducing memory requirements"
            ],
            "correct": 2,
            "explanation": "Parallelization and long-range dependencies. Real-time Application: Transformers enable efficient document summarization across long paragraphs."
        },
        {
            "question": "Which Hugging Face feature allows sharing and using models easily?",
            "options": [
                "TensorFlow Hub",
                "Model Hub",
                "PyTorch Lightning",
                "DataFrames"
            ],
            "correct": 1,
            "explanation": "Model Hub. Real-time Application: Developers download pre-trained models for text summarization in one line of code."
        },
        {
            "question": "What is the role of 'attention' in transformers?",
            "options": [
                "Ignoring key words",
                "Focusing on important tokens in context",
                "Reducing vocabulary size",
                "Increasing training data"
            ],
            "correct": 1,
            "explanation": "Focusing on important tokens in context. Real-time Application: In translation, attention ensures 'bank' in English is correctly mapped depending on sentence context."
        },
        {
            "question": "Which model introduced the concept of bidirectional attention?",
            "options": [
                "GPT",
                "Word2Vec",
                "BERT",
                "LSTM"
            ],
            "correct": 2,
            "explanation": "BERT. Real-time Application: BERT is applied in Google Search for understanding queries contextually."
        },
        {
            "question": "LLMs are prone to which common issue?",
            "options": [
                "Lack of scalability",
                "Hallucination of facts",
                "Zero generalization",
                "Inability to tokenize"
            ],
            "correct": 1,
            "explanation": "Hallucination of facts. Real-time Application: Chatbots sometimes generate fabricated but plausible-sounding answers."
        },
        {
            "question": "Which optimization technique is often used in training transformers?",
            "options": [
                "Gradient descent",
                "Adam optimizer",
                "RMSProp",
                "Genetic algorithms"
            ],
            "correct": 1,
            "explanation": "Adam optimizer. Real-time Application: Used in training BERT/GPT efficiently."
        },
        {
            "question": "Hugging Face datasets library is useful for:",
            "options": [
                "Creating SQL queries",
                "Loading and processing NLP datasets",
                "Game simulations",
                "Running operating systems"
            ],
            "correct": 1,
            "explanation": "Loading and processing NLP datasets. Real-time Application: Directly loading IMDb dataset for sentiment classification."
        },
        {
            "question": "Which of these is a practical application of LLMs?",
            "options": [
                "Predicting stock movements",
                "Image denoising",
                "Language translation and summarization",
                "Sorting integers"
            ],
            "correct": 2,
            "explanation": "Language translation and summarization. Real-time Application: GPT-based summarizers condense news articles into short readable text."
        }
        ]
    }
}

# # ---------------------------
# # SESSION STATE
# # ---------------------------
# if 'selected_topic' not in st.session_state:
#     st.session_state.selected_topic = None
# if 'answers' not in st.session_state:
#     st.session_state.answers = {}
# if 'submitted' not in st.session_state:
#     st.session_state.submitted = False
# if 'last_quiz' not in st.session_state:
#     st.session_state.last_quiz = None  # ✅ Track last attempted quiz


# # ---------------------------
# # HELPER FUNCTIONS
# # ---------------------------
# def reset_quiz():
#     st.session_state.answers = {}
#     st.session_state.submitted = False


# def main():
#     st.set_page_config(page_title="MCQ Quiz App", page_icon="📝", layout="wide")

#     # --- Custom CSS ---
#     st.markdown("""
#         <style>
#         .correct-answer {background-color: #d4edda; border: 2px solid #28a745; padding: 10px; border-radius: 5px; margin: 5px 0; color: black;}
#         .wrong-answer {background-color: #f8d7da; border: 2px solid #dc3545; padding: 10px; border-radius: 5px; margin: 5px 0; color: black;}
#         .score-box {background-color: #e7f3ff; padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold; margin: 20px 0;}
#         </style>
#     """, unsafe_allow_html=True)

#     st.title("📝 MCQ Quiz Application")

#     # ---------------------------
#     # SIDEBAR
#     # ---------------------------
#     with st.sidebar:
#         st.header("📚 Select Topic")

#         if st.session_state.selected_topic:
#             if st.button("← Back to Topics"):
#                 st.session_state.selected_topic = None
#                 reset_quiz()
#                 st.rerun()

#             # ✅ Dropdown to switch topics while inside a quiz
#             st.markdown("### 🔽 Switch Topic")
#             topic_names = list(QUIZ_DATA.keys())
#             selected_dropdown = st.selectbox(
#                 "Go to another topic:",
#                 topic_names,
#                 index=topic_names.index(st.session_state.selected_topic) if st.session_state.selected_topic in topic_names else 0
#             )

#             if selected_dropdown != st.session_state.selected_topic:
#                 st.session_state.selected_topic = selected_dropdown
#                 st.session_state.last_quiz = selected_dropdown  # update last quiz
#                 reset_quiz()
#                 st.rerun()

#             st.markdown("---")

#         st.info("Select a topic to start the quiz!")

#     # ---------------------------
#     # MAIN CONTENT AREA
#     # ---------------------------
#     if st.session_state.selected_topic is None:
#         # ✅ Show last attempted quiz
#         if st.session_state.last_quiz:
#             last_title = QUIZ_DATA[st.session_state.last_quiz]["title"]
#             st.success(f"🕓 Last attempted quiz: **{last_title}**")

#         st.subheader("Choose a Quiz Topic")
#         st.markdown("Click on any topic below to start your quiz:")

#         cols = st.columns(3)
#         topics = list(QUIZ_DATA.keys())

#         for idx, topic in enumerate(topics):
#             col = cols[idx % 3]
#             with col:
#                 topic_display = topic.replace("_", " ").replace("QA", "").strip()
#                 if st.button(f"📌 {topic_display}", key=topic, use_container_width=True):
#                     st.session_state.selected_topic = topic
#                     st.session_state.last_quiz = topic  # ✅ store last opened quiz
#                     reset_quiz()
#                     st.rerun()

#     else:
#         # Display selected quiz
#         topic_data = QUIZ_DATA[st.session_state.selected_topic]
#         st.header(f"🎯 {topic_data['title']}")

#         if not topic_data['questions']:
#             st.warning("Questions for this topic are coming soon!")
#             return

#         st.markdown(f"**Total Questions:** {len(topic_data['questions'])}")
#         st.markdown("---")

#         if not st.session_state.submitted:
#             with st.form("quiz_form"):
#                 for idx, q in enumerate(topic_data['questions']):
#                     st.subheader(f"Question {idx + 1}")
#                     st.write(q['question'])
#                     answer = st.radio(
#                         "Select your answer:",
#                         options=range(len(q['options'])),
#                         format_func=lambda x, q=q: q['options'][x],
#                         key=f"q_{idx}",
#                         index=None
#                     )
#                     if answer is not None:
#                         st.session_state.answers[idx] = answer
#                     st.markdown("---")

#                 submitted = st.form_submit_button("Submit Quiz", use_container_width=True)
#                 if submitted:
#                     if len(st.session_state.answers) < len(topic_data['questions']):
#                         st.error("⚠️ Please answer all questions before submitting!")
#                     else:
#                         st.session_state.submitted = True
#                         st.rerun()

#         else:
#             # Show results
#             correct_count = 0
#             total_questions = len(topic_data['questions'])

#             for idx, q in enumerate(topic_data['questions']):
#                 user_answer = st.session_state.answers.get(idx)
#                 correct_answer = q['correct']
#                 is_correct = user_answer == correct_answer

#                 if is_correct:
#                     correct_count += 1

#                 st.subheader(f"Question {idx + 1}")
#                 st.write(q['question'])

#                 for opt_idx, option in enumerate(q['options']):
#                     if opt_idx == correct_answer:
#                         if opt_idx == user_answer:
#                             st.markdown(f'<div class="correct-answer">✅ {option} (Your answer - Correct!)</div>', unsafe_allow_html=True)
#                         else:
#                             st.markdown(f'<div class="correct-answer">✅ {option} (Correct answer)</div>', unsafe_allow_html=True)
#                     elif opt_idx == user_answer:
#                         st.markdown(f'<div class="wrong-answer">❌ {option} (Your answer - Incorrect)</div>', unsafe_allow_html=True)
#                     else:
#                         st.markdown(f'<p style="color:#ccc;padding:10px;">⚪ {option}</p>', unsafe_allow_html=True)

#                 with st.expander("📖 Explanation"):
#                     st.info(q['explanation'])

#                 st.markdown("---")

#             score_percentage = (correct_count / total_questions) * 100
#             st.markdown(f'<div class="score-box"><span style="color: black;">🎯 Your Score: {correct_count}/{total_questions} ({score_percentage:.1f}%)</span></div>', unsafe_allow_html=True)

#             if score_percentage >= 80:
#                 st.success("🌟 Excellent work! You have a strong understanding of this topic!")
#             elif score_percentage >= 60:
#                 st.info("👍 Good job! Review the explanations to strengthen your knowledge.")
#             else:
#                 st.warning("📚 Keep practicing! Review the material and try again.")

#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("🔄 Retry Quiz", use_container_width=True):
#                     reset_quiz()
#                     st.rerun()
#             with col2:
#                 if st.button("📚 Choose Another Topic", use_container_width=True):
#                     st.session_state.selected_topic = None
#                     reset_quiz()
#                     st.rerun()


# if __name__ == "__main__":
#     main()

import streamlit as st

# ---------------------------
# SESSION STATE
# ---------------------------
if 'selected_topics' not in st.session_state:
    st.session_state.selected_topics = []
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'last_quiz' not in st.session_state:
    st.session_state.last_quiz = None


# ---------------------------
# HELPER FUNCTIONS
# ---------------------------
def reset_quiz():
    st.session_state.answers = {}
    st.session_state.submitted = False


def main():
    st.set_page_config(page_title="MCQ Quiz App", page_icon="📝", layout="wide")

    # --- Custom CSS ---
    st.markdown("""
        <style>
        .correct-answer {background-color: #d4edda; border: 2px solid #28a745; padding: 10px; border-radius: 5px; margin: 5px 0; color: black;}
        .wrong-answer {background-color: #f8d7da; border: 2px solid #dc3545; padding: 10px; border-radius: 5px; margin: 5px 0; color: black;}
        .score-box {background-color: #e7f3ff; padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold; margin: 20px 0;}
        </style>
    """, unsafe_allow_html=True)

    st.title("📝 MCQ Quiz Application")

    # ---------------------------
    # SIDEBAR
    # ---------------------------
    with st.sidebar:
        if st.session_state.selected_topics:
            if st.button("← Back to Topics", use_container_width=True):
                st.session_state.selected_topics = []
                reset_quiz()
                st.rerun()
                
        st.header("📚 Select Topics")

        topic_names = list(QUIZ_DATA.keys())

        # Buttons for select all / clear all
        colA, colB = st.columns(2)
        with colA:
            if st.button("✅ Select All"):
                st.session_state.selected_topics = topic_names
                reset_quiz()
                st.rerun()
        with colB:
            if st.button("🗑️ Clear All"):
                st.session_state.selected_topics = []
                reset_quiz()
                st.rerun()

        # Multiselect topics
        selected = st.multiselect(
            "Select one or more topics:",
            topic_names,
            default=st.session_state.selected_topics
        )

        if selected != st.session_state.selected_topics:
            st.session_state.selected_topics = selected
            st.session_state.last_quiz = selected
            reset_quiz()
            st.rerun()

        if st.session_state.selected_topics:
            st.markdown("---")

        st.info("You can also click on topics on the home page to start a quiz.")

    # ---------------------------
    # MAIN CONTENT AREA
    # ---------------------------
    if not st.session_state.selected_topics:
        # ✅ Home Page
        if st.session_state.last_quiz:
            last_titles = [QUIZ_DATA[t]['title'] for t in st.session_state.last_quiz]
            st.success(f"🕓 Last attempted quiz: **{', '.join(last_titles)}**")

        st.subheader("Choose a Quiz Topic")
        st.markdown("Click on any topic below to start your quiz:")

        cols = st.columns(3)
        topics = list(QUIZ_DATA.keys())

        for idx, topic in enumerate(topics):
            col = cols[idx % 3]
            with col:
                topic_display = topic.replace("_", " ").replace("QA", "").strip()
                if st.button(f"📌 {topic_display}", key=topic, use_container_width=True):
                    st.session_state.selected_topics = [topic]
                    st.session_state.last_quiz = [topic]
                    reset_quiz()
                    st.rerun()

        return  # Exit here so only home page is shown

    # ---------------------------
    # COMBINED QUIZ DISPLAY
    # ---------------------------
    selected_data = [QUIZ_DATA[t] for t in st.session_state.selected_topics if t in QUIZ_DATA]
    combined_questions = []
    for topic in selected_data:
        for q in topic['questions']:
            combined_questions.append({**q, 'topic_title': topic['title']})

    if not combined_questions:
        st.warning("No questions found for the selected topics.")
        return

    st.header("🎯 Combined Quiz")
    st.markdown(f"**Selected Topics:** {', '.join([t['title'] for t in selected_data])}")
    st.markdown(f"**Total Questions:** {len(combined_questions)}")
    st.markdown("---")

    # ---------------------------
    # QUIZ QUESTIONS
    # ---------------------------
    if not st.session_state.submitted:
        with st.form("quiz_form"):
            for idx, q in enumerate(combined_questions):
                st.subheader(f"{q['topic_title']} — Question {idx + 1}")
                st.write(q['question'])
                answer = st.radio(
                    "Select your answer:",
                    options=range(len(q['options'])),
                    format_func=lambda x, q=q: q['options'][x],
                    key=f"q_{idx}",
                    index=None
                )
                if answer is not None:
                    st.session_state.answers[idx] = answer
                st.markdown("---")

            submitted = st.form_submit_button("Submit Quiz", use_container_width=True)
            if submitted:
                if len(st.session_state.answers) < len(combined_questions):
                    st.error("⚠️ Please answer all questions before submitting!")
                else:
                    st.session_state.submitted = True
                    st.rerun()

    else:
        correct_count = 0
        total_questions = len(combined_questions)

        for idx, q in enumerate(combined_questions):
            user_answer = st.session_state.answers.get(idx)
            correct_answer = q['correct']
            is_correct = user_answer == correct_answer

            if is_correct:
                correct_count += 1

            st.subheader(f"{q['topic_title']} — Question {idx + 1}")
            st.write(q['question'])

            for opt_idx, option in enumerate(q['options']):
                if opt_idx == correct_answer:
                    if opt_idx == user_answer:
                        st.markdown(f'<div class="correct-answer">✅ {option} (Your answer - Correct!)</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="correct-answer">✅ {option} (Correct answer)</div>', unsafe_allow_html=True)
                elif opt_idx == user_answer:
                    st.markdown(f'<div class="wrong-answer">❌ {option} (Your answer - Incorrect)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<p style="color:#ccc;padding:10px;">⚪ {option}</p>', unsafe_allow_html=True)

            with st.expander("📖 Explanation"):
                st.info(q['explanation'])
            st.markdown("---")

        score_percentage = (correct_count / total_questions) * 100
        st.markdown(f'<div class="score-box"><span style="color: black;">🎯 Your Score: {correct_count}/{total_questions} ({score_percentage:.1f}%)</span></div>', unsafe_allow_html=True)

        if score_percentage >= 80:
            st.success("🌟 Excellent work! You have a strong understanding of these topics!")
        elif score_percentage >= 60:
            st.info("👍 Good job! Review the explanations to strengthen your knowledge.")
        else:
            st.warning("📚 Keep practicing! Review the material and try again.")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Retry Quiz", use_container_width=True):
                reset_quiz()
                st.rerun()
        with col2:
            if st.button("🏠 Back to Home", use_container_width=True):
                st.session_state.selected_topics = []
                reset_quiz()
                st.rerun()


if __name__ == "__main__":
    main()

