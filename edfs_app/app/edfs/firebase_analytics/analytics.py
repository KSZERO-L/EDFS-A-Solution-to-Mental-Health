from edfs.firebase_analytics import display
import pandas as pd
import numpy as np
import plotly.express as px

def firebase_analytics(q):
    
    if q == "q1":
        data1, data2, data3 = display.main('/Mental Health Dataset/share-with-depression.csv')
        # print(data1.head())
        # print(data1.shape)
        # print(data2.head())
        # print(data2.shape)
        # print(data3.head())
        # print(data3.shape)
        # countries = list(set(data['Entity']))
        # new_df = pd.DataFrame(columns = ["Country", "Prevalence"])
        d1 = data1.groupby('Entity')['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].agg(np.mean)
        d2 = data2.groupby('Entity')['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].agg(np.mean)
        d3 = data3.groupby('Entity')['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)'].agg(np.mean)

        # print(d1)
        j1, j2, j3 = {}, {}, {}
        d1 = d1.to_frame().reset_index()
        d2 = d2.to_frame().reset_index()
        d3 = d3.to_frame().reset_index()
        all_keys = set()
        for i in d1.iterrows():
            all_keys.add(i[1]['Entity'])
            j1[i[1]['Entity']] = i[1]['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)']

        for i in d2.iterrows():
            all_keys.add(i[1]['Entity'])
            j2[i[1]['Entity']] = i[1]['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)']

        for i in d3.iterrows():
            all_keys.add(i[1]['Entity'])
            j3[i[1]['Entity']] = i[1]['Prevalence - Depressive disorders - Sex: Both - Age: Age-standardized (Percent)']

        fd = {}
        all_keys = list(all_keys)
        # print(all_keys)
        for val in all_keys:
            val1, val2, val3 = 0, 0, 0
            if val in j1:
                val1 = j1[val]
            if val in j2:
                val2 = j2[val]
            if val in j3:
                val3 = j3[val]

            avg = (val1+val2+val3)/3

            fd[val] = avg

        # print(fd)
        desc = dict(sorted(fd.items(), key=lambda x: x[1], reverse=True) )
        fd_ = pd.DataFrame(columns=["Country", "Prevalence"])
        cnt = 1
        final = []
        for k,v in desc.items():
            final.append({
                'Country': k,
                'Prevalence': v
            })
            cnt+=1
            if cnt== 11:
                break


        return final


    if q == "q2":

        data1, data2, data3 = display.main('/Mental Health and Suicide Rates/Human Resources.csv')
        # print(data1.head())
        # print(data1.shape)
        # print(data2.head())
        # print(data2.shape)
        # print(data3.head())
        # print(data3.shape)
        # countries = list(set(data['Entity']))
        # new_df = pd.DataFrame(columns = ["Country", "Prevalence"])
        d1 = data1.groupby('Country')[['Psychiatrists', 'Psychologists']].agg(np.mean)
        d2 = data2.groupby('Country')[['Psychiatrists', 'Psychologists']].agg(np.mean)
        d3 = data3.groupby('Country')[['Psychiatrists', 'Psychologists']].agg(np.mean)

        j1, j2, j3 = {}, {}, {}
        d1 = d1.reset_index()
        d2 = d2.reset_index()
        d3 = d3.reset_index()
        all_keys = set()
        for i in d1.iterrows():
            all_keys.add(i[1]['Country'])
            j1[i[1]['Country']] = [i[1]['Psychiatrists'], i[1]['Psychologists']]

        for i in d2.iterrows():
            all_keys.add(i[1]['Country'])
            j2[i[1]['Country']] = [i[1]['Psychiatrists'], i[1]['Psychologists']]

        for i in d3.iterrows():
            all_keys.add(i[1]['Country'])
            j3[i[1]['Country']] = [i[1]['Psychiatrists'], i[1]['Psychologists']]

        fd = {}
        all_keys = list(all_keys)
        # print(all_keys)
        for val in all_keys:
            val1, val2, val3 = 0, 0, 0
            val4, val5, val6 = 0, 0, 0
            if val in j1:
                val1 = j1[val][0]
                val4 = j1[val][1]
            if val in j2:
                val2 = j2[val][0]
                val5 = j2[val][1]
            if val in j3:
                val3 = j3[val][0]
                val6 = j3[val][1]

            avg = (val1+val2+val3)/3
            avg2 = (val4+val5+val6)/3

            fd[val] = [avg, avg2]

        desc = dict(sorted(fd.items(), key=lambda x: x[1][0], reverse=True) )
        fd_ = pd.DataFrame(columns=["Country", "Psychiatrists", "Psychologists"])
        cnt = 1
        final = []
        for k,v in desc.items():
            final.append({
                'Country': k,
                'Psychiatrists': v[0],
                'Psychologists': v[1]
            })
            cnt+=1
            if cnt== 11:
                break

        print(final)
        
        return final

    if q == "q3":

        data1, data2, data3 = display.main('/Mental Health in Tech Survey/survey.csv')
        # print(data1.head())
        # print(data1.shape)
        # print(data2.head())
        # print(data2.shape)
        # print(data3.head())
        # print(data3.shape)
        # countries = list(set(data['Entity']))
        # new_df = pd.DataFrame(columns = ["Country", "Prevalence"])
        d1 = data1.groupby(['mental_health_consequence'])['mental_health_consequence'].count()
        d2 = data2.groupby(['mental_health_consequence'])['mental_health_consequence'].count()
        d3 = data3.groupby(['mental_health_consequence'])['mental_health_consequence'].count()

        x1 = list(d1.index)
        y1 = list(d1.values)
        x2 = list(d2.index)
        y2 = list(d2.values)
        x3 = list(d3.index)
        y3 = list(d3.values)


        new_lst = []
        new_lst.append(y1[0]+y2[0]+y3[0])
        new_lst.append(y1[1]+y2[1]+y3[1])
        new_lst.append(y1[2]+y2[2]+y3[2])

        final = {}
        for x, y in zip(x1, new_lst):
            final[x] = y

        print(final)

        return final

    if q == "q4":

        data1, data2, data3 = display.main('/World Happiness Report 2015-2021/2018.csv')
        # print(data1.head())
        # print(data1.shape)
        # print(data2.head())
        # print(data2.shape)
        # print(data3.head())
        # print(data3.shape)
        # countries = list(set(data['Entity']))
        # new_df = pd.DataFrame(columns = ["Country", "Prevalence"])
        print(data1.columns)
        d1 = data1.groupby('Country or region')['Score'].agg(np.mean)
        d2 = data2.groupby('Country or region')['Score'].agg(np.mean)
        d3 = data3.groupby('Country or region')['Score'].agg(np.mean)

        # print(d1)
        j1, j2, j3 = {}, {}, {}
        d1 = d1.to_frame().reset_index()
        d2 = d2.to_frame().reset_index()
        d3 = d3.to_frame().reset_index()
        all_keys = set()
        for i in d1.iterrows():
            all_keys.add(i[1]['Country or region'])
            j1[i[1]['Country or region']] = i[1]['Score']

        for i in d2.iterrows():
            all_keys.add(i[1]['Country or region'])
            j2[i[1]['Country or region']] = i[1]['Score']

        for i in d3.iterrows():
            all_keys.add(i[1]['Country or region'])
            j3[i[1]['Country or region']] = i[1]['Score']

        fd = {}
        all_keys = list(all_keys)
        # print(all_keys)
        for val in all_keys:
            val1, val2, val3 = 0, 0, 0
            if val in j1:
                val1 = j1[val]
            if val in j2:
                val2 = j2[val]
            if val in j3:
                val3 = j3[val]

            avg = (val1+val2+val3)/3

            fd[val] = avg

        # print(fd)
        desc = dict(sorted(fd.items(), key=lambda x: x[1], reverse=True) )
        fd_ = pd.DataFrame(columns=["Country", "Happiness Score"])
        cnt = 1
        final = []
        for k,v in desc.items():
            final.append({
                'Country': k,
                'Happiness Score': v
            })
            cnt+=1
            if cnt== 11:
                break


        return final

        