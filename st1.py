import help_funcs as hf
import props  # props contains functions for gas properties calculations
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import streamlit as st

# st.title("Welcome to My Streamlit App!")
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.write("And this is some regular text.")


st.title("Gas Properties")
st.header("Cp at Various Temperatures")


def calc_cps(comps, tempsc):
    result_matrix = []
    for comp in comps:
        cpcomp = [round(props.cp(comp, temp + 273.15), 2) for temp in tempsc]
        result_matrix.append(cpcomp)
    return result_matrix


comps = []
cp_table_html = ""

temp_list = ['50', '100', '150', '200', '300', '500', '600', '700']

comp_names = [['Methane', 1], ['Ethane', 2], ['Propane', 3], ['Acetylene', 6],
              ['Ethylene', 4], ['Propylene', 5], ['Butene-1', 8],
              ['Benzene', 9]]

temps = [50, 100, 150, 200, 250]
comps = [50, 100, 150, 200, 250]


comps = [1, 2, 3, 4, 5]
compstxt = ['Methane', 'Ethane', 'Propane', 'Ethylene']
result_matrix = calc_cps(comps, temps)
print(result_matrix)


# make pandas frame
tempsC = [str(temp) + " C" for temp in temps]
compstxt = [props.coeffs[comp].name for comp in comps]
cpdf = pd.DataFrame(result_matrix, compstxt, tempsC)

print(cpdf)

st.dataframe(cpdf)

#
# creating dataframe
df = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 4, 6, 10, 15]
})

# plotting a line graph
print("Line graph: ")
# plt.plot(df["X"], df["Y"])
# plt.show()

# for series in result_matrix:
#   plt.plot(temps, series)
# plt.show()
# plt.plot(temps, result_matrix[0])

fig1, ax = plt.subplots()
for series in result_matrix:
    plt.plot(temps, series)

plt.xlabel("Temperature, C")
plt.ylabel("Cp, J/(mol-K)")
plt.title("Cp of Hydrocarbon Gases")


st.pyplot(fig1)
