import pandas as pd
from pandas import unique

# br_states = pd.read_csv("br.csv")
# my_states = list(unique(br_states['admin_name']))
# print(my_states)
br_states = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Distrito Federal', 'Bahia', 'Ceará', 'Amazonas',
               'Paraná', 'Pernambuco', 'Pará', 'Rio Grande do Sul', 'Goiás', 'Amapá', 'Maranhão', 'Alagoas', 'Piauí',
               'Rio Grande do Norte', 'Paraíba', 'Sergipe', 'Espírito Santo', 'Santa Catarina', 'Acre', 'Rondônia',
               'Mato Grosso', 'Mato Grosso do Sul', 'Roraima', 'Tocantins']


x = [39.0, 153.0, 117.0, 60.0, 160.0, 199.0, -211.0, -10.0, 229.0, -26.0, -31.0, 20.0, -6.0, 101.0, 250.0, 141.0, 249.0,
     250.0, 234.0, 181.0, 11.0, -336.0, -196.0, -74.0, -64.0, -169.0, 52.0]
y = [-142.0, -146.0, -76.0, -35.0, 30.0, 145.0, 165.0, -186.0, 89.0, 161.0, -267.0, -44.0, 253.0, 146.0, 68.0, 99.0, 135.0,
     108.0, 51.0, -102.0, -225.0, 83.0, 50.0, 13.0, -109.0, 272.0, 55.0]

br_states_game = pd.DataFrame({
    'states': br_states,
    'x': x,
    'y': y
})
br_states_game["states"] = br_states_game["states"].str.title()

