import plotly.express as px
import pandas as pd

data = [
   
    dict(Task="Conduct Platform Research", Start='2025-10-15', Finish='2025-10-19', Resource='Durham Challenge', Members='Nevin, Luke'),
    dict(Task="Run Scripts", Start='2025-10-19', Finish='2025-10-22', Resource='Durham Challenge', Members='Nevin, Luke'),
    dict(Task="Prepare and Record Presentation", Start='2025-10-22', Finish='2025-10-30', Resource='Durham Challenge', Members='Nevin, Luke'),
    
    
    dict(Task="Run HPL Software", Start='2025-10-13', Finish='2025-10-19', Resource='EPCC Challenge', Members='Mayukha, Nevin, Nok Hang'),
    dict(Task="Optimise HPL Performance", Start='2025-10-19', Finish='2025-10-29', Resource='EPCC Challenge', Members='Mayukha, Nevin, Nok Hang'),
    dict(Task="Optimise Energy Efficiency", Start='2025-10-25', Finish='2025-10-30', Resource='EPCC Challenge', Members='Mayukha, Nevin, Nok Hang'),
    dict(Task="Prepare Slides", Start='2025-10-30', Finish='2025-10-31', Resource='EPCC Challenge', Members='Mayukha, Nevin, Nok Hang'),

    
    
    dict(Task="Initial Docker Containers and Streamlit set-up", Start='2025-10-18', Finish='2025-10-26', Resource='UCL Challenge', Members='Femi, Sacha, Luke'),
    dict(Task="Setup Postgres DB Docker and added four streamlit visualisations", Start='2025-10-26', Finish='2025-10-30', Resource='UCL Challenge', Members='Femi, Sacha, Luke'),

    dict(Task="Code Clean-Up, Review and Accessibility Features", Start='2025-10-30', Finish='2025-10-31', Resource='UCL Challenge', Members='Femi, Sacha, Luke'),
    dict(Task="Unit Testing", Start='2025-10-18', Finish='2025-11-01', Resource='UCL Challenge', Members='Femi, Sacha, Luke'),
    dict(Task="Setup GitHub Actions for Runnning a Build and Test", Start='2025-10-19', Finish='2025-10-24', Resource='UCL Challenge', Members='Femi, Sacha, Luke'),

    dict(Task="Presentation Creation and Rehersal", Start='2025-11-01', Finish='2025-11-03', Resource='UCL Challenge', Members='Femi, Sacha, Luke'),

]

df = pd.DataFrame(data)

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource", hover_data=['Members'])
fig.update_yaxes(autorange="reversed")
fig.update_layout(title="CIUK Challenge Gant Chart")

fig.show()