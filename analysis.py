import pandas as pd
from causalimpact import CausalImpact
import matplotlib.pyplot as plt

amc = pd.read_csv("AMC_history.csv")
amcx = pd.read_csv("AMCX_history.csv")
voo = pd.read_csv("VOO_history.csv")

# Join. All data is indexed by timestamp GMT
data = amc.join(amcx.set_index('date'),
                on='date',
                lsuffix='_amc',
                rsuffix='_amcx')
data = data.join(voo.set_index('date'), on='date')

# We just want the close prices at the end of each interval
data = data.drop([
    'high', 'open', 'low', 'high_amc', 'low_amc', 'open_amc', 'high_amcx',
    'low_amcx', 'open_amcx'
],
                 axis=1)

# Rename things, for the neatness
data = data.rename(columns={
    'close': 'close_voo',
})

print(data)

# Check if the SP500 looks like a solid input for our synthetic control
data.plot()
plt.savefig('summary.svg')

# Define periods. Article came out ~2:30 EDT on May 9th so let's say treatment end of markets the friday before
pre_period = [
    pd.Timestamp('2020-05-01 13:30:00+00:00'),
    pd.Timestamp('2020-05-08 20:00:00+00:00')
]
post_period = [
    pd.Timestamp('2020-05-11 13:30:00+00:00'),
    pd.Timestamp('2020-05-15 19:50:00+00:00')
]

# Shove it into CasualImpact
amc_data = data[['close_amc', 'close_voo', 'date']]
amc_data = amc_data.set_index('date')

ci = CausalImpact(amc_data, pre_period, post_period)
ci.plot()
print(ci.summary('report'))
