import pandas as pd
df = pd.read_csv('text_4_var_69', names =["firstname", "secondname", "age","salary", "phone"])
df = df.drop("phone", axis=1)
df["salary"] = df["salary"].apply(lambda x: int(x[:-1]))
df["age"] = df["age"].apply(lambda x: int(x))
df = df.loc[df["salary"] > df["salary"].mean()].loc[df["age"] > (25+69%10)]
df["full_name"] = df["firstname"]+" "+ df["secondname"]
df = df.drop(["firstname","secondname"], axis=1)
df.sort_values(by = ['age'], inplace = True)
df.reset_index(drop=True, inplace=True)
df.to_csv('result')

