# SAS and Stata files
#   - SAS: Statistical Analysis System
#   - Stata: "Statistics" + "data"
#   - SAS: business analytics and biostatistics
#   - Stata: academic social sciences research

# SAS files:
#   - Used for:
#       * Advanced analytics
#       * Mulitvariate analysis
#       * Business intelligence
#       * Data management
#       * Predictive analytics
#       * Standard for computational analysis
# Importing SAS files
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('urbanpop.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Importing Stata files
import pandas as pd
data = pd.read_stata('urbanpop.dta')
