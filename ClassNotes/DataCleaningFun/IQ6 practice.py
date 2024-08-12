# Oct 7 & 12 Notes (in PandasFun)

# Data Aggregation = gathing data (and presenting it) in a summarized format, may be from multiple sources 
# Gonzaga's First Destination survey report
# Common approach: split, apply, combine
# 1. split = split the data into sub-tables based on the values of an attribute 
# ex: split on college/school 1 subtable for each college/school (SEAS, CAS, etc...)
# pandas group by "col"
# 2. apply = apply a function to the data in each subtable to summarize it
# ex: computing a percent employed (or mean(), median()...)
# 3. combine = combine the apply result (#2) into a summary table
# ex: building a new pandas series

# 1, split on "class", 
# 2. apply mean to population
# 3. combine population means into table (1 column)


# Data Cleaning
# it is quite common to have datasets with missing, invalid, or noisy values
# recall 60% of time is data cleaning

# missing values are often represented as "NA" or "N/A" or "np.NaN" (null value, invalid)
# dropna() = remove all NA values, fillna(), replace()

# ways to deal with noisy / invalid values
# noisy = recorded wrong, valid on measurement scale
# invalid = not right on scale
# 1. look for duplicates when there shouldn't be any
# 2. look for outliers: sort and print the values, visualizations
# smooth out values (filter, moving average smoothing)

# ways to deal with missing values
# remove the instances / attributes with missing values, dropna()
# mostly applicable when data set is large and missing values are rare

# fill / replace missing values 
# 1. by hand (manual inspection)

# 2. use a central tendency measure 
# for numeric: mean, median, mode, interpolate() linear only when you do not have NA value on first and last
# for categorical: most frequent label (survived y/n, most no, so put no)

# 3. use machine learning to make a prediction
# for numeric: regression techniques
# for categorical: classification techniques

# 4. ignore them and deal with on case by case basis
# a bunch of if statements

# number of missing values on df = .isnull().sum()




#Data Aggregation- gathering data + (presenting it) in assumed format
    #-data may be from multiple sources 
    #- ex: GU first destination survery report 
    #-common approach - split- apply- combine

#1) Split - split the data into subtables
    #based on the values of an attribute 
    #ex: split on college/school
        #1 subtable for each college/school (CAS, SEAS, SRS....)
#2) Apply - apply a function to the data in each subtable to summarize it 
    #ex: computes a pecent employed
        #(or mean(), meadian(),...)
#3) combine - combine the apply results (#2)
    #into a summary table 

#Data Cleaning 
    #it is quite common to have data sets with missing, invalid, or noisy values
#Missing values are often represented as 
    #-"NA" or "N/A" -> dropna() -> fillna() -> replace()
    #-np.NaN (null)
#Ways to deal with noisy/invalid values
    #-look for duplicates (when there shouldn't be any)
#look for outliers
    #sort and print the values
    #visualizations help
#Smooth out values(e.g. filter, moving average, etc...)

#ways to handle missing values
    #remove the instances/attributes with missing values -> dropna()
    #*mostly applicable when data set is large and missing values are rare

#Ways to do it 
    #fill/replace missing values
        #1)by hand (manual inspection)
        #2)use a central tendency measure 
            #for numeric: mean, median, mode -> interpolate() linear
            #for categorical: most frequent label -> fillna(), Lffill -> forward fill, Lbfill -> back fill
        #3)use machine learning to make a prediction 
            #for numeric attributes: regression techniques
            #for categorical: classification techniques
        #4) ignore them and deal with them on a case by case basis 
            #a bunch of if statements...
