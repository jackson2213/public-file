#function input value is read from analyze_result.csv company and sensitivity colume
#example:
'''
company sensitivity
google  pos
intel   neu
google  pos
google  neu
intel   neg
'''

def count_company():
    articles = pd.read_csv('tweets_3.csv',index_col=['company', 'sensitivity'], low_memory=False)
    count_company = {}
    result = []
    for index, row in tqdm(articles.iterrows(), total = len(articles)):
        company = index[0]
        sensitivity = index[1]
        if company not in count_company.keys():
             count_company[company] = {'pos':0,'neg':0,'neu':0}
        else:
            if sensitivity == 'pos':
                count_company[company]['pos'] += 1
            elif sensitivity == 'pos':
                count_company[company]['neg'] += 1
            else:
               count_company[company]['neu'] += 1
    for key, value in count_company.items():
        # key value is company
        pos_ratio = round(value['pos']/(value['pos']+value['neg']+value['neu']),2)
        neg_ratio = round(value['neg']/(value['pos']+value['neg']+value['neu']),2)
        neu_ratio = round(value['neu']/(value['pos']+value['neg']+value['neu']),2)
        result.append([key, pos_ratio, neg_ratio,neu_ratio])
    df = pd.DataFrame(output, columns = ['company', 'pos_ratio', 'neg_ratio', 'neu_ratio'])  # convert list to dataframe
    df.to_csv('sensitivity_analyze_by_company.csv')  # save the result to a csv file
    print('task finished!')
