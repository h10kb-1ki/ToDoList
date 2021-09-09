import streamlit as st
import pandas as pd
import datetime

st.title('ToDoList')
df = pd.read_excel('ToDoList.xlsx', header=0)

for name, group in df.groupby('分類'):
    st.markdown(f'**{name}**')
    for i in range(0, len(group)):
        group = group.sort_values('締切り')
        naiyou = group.iat[i, 1]
        shimekiri = group.iat[i, 2]
        juyodo = group.iat[i, 3]
        st.write('・・・' + shimekiri + ' '+ juyodo +'   ［'+ naiyou + '］')
    st.write('')

'''
## 編集オプション
'''
if st.checkbox('新規登録'):
    category = st.selectbox('分類', ('1. 教育関連', '2. 放射線関連', '3. 自己研鑽', '4. その他', '5. メモ', ''), index=5, )
    body = st.text_input('内容')
    dead_line = st.date_input('締切り')
    importance = st.selectbox('重要度', ('★★★', '★★☆', '★☆☆', '☆☆☆', ''), index=4)
    if st.button('追加'):
        if body == '':
            st.write('空欄が残っています')
        elif dead_line == '':
            st.write('空欄が残っています')
        elif importance == '':
            st.write('空欄が残っています')
        else:
            df = df.append({'分類':category, '内容':body, '締切り':dead_line.strftime("%y/%m/%d"), '重要度':importance}, ignore_index=True)
            df.to_excel('ToDoList.xlsx', index=False)
            st.write('変更を保存しました')
            st.write('チェックボックスを外してください')

if st.checkbox('削除'):
    st.dataframe(df, width=500)
    num = st.selectbox('削除するindex番号を指定', range(0, len(df)))
    if st.button('削除'):
        df = df.drop(df.index[num])
        df.to_excel('ToDoList.xlsx', index=False)
        st.write('変更を保存しました')
        st.write('チェックボックスを外してください')
