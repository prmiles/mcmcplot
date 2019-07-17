__version__ = "1.0.0rc1"

from . import mcmatplot as _mcmpl
from . import mcseaborn as _mcsns

plot_density_panel = _mcmpl.plot_density_panel
plot_histogram_panel = _mcmpl.plot_histogram_panel
plot_chain_panel = _mcmpl.plot_chain_panel
plot_pairwise_correlation_panel = _mcmpl.plot_pairwise_correlation_panel

plot_joint_distributions = _mcsns.plot_joint_distributions
plot_paired_density_matrix = _mcsns.plot_paired_density_matrix