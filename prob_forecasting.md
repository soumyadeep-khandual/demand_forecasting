# Probabilistic Forecasting
Probabilistic forecasting is a type of forecasting that provides a probability distribution over possible future outcomes, rather than a single "point" estimate. Instead of saying, "The temperature tomorrow will be 25°C," a probabilistic forecast might say, "There is a 70% chance the temperature will be between 23°C and 27°C, a 15% chance it will be above 27°C, and a 15% chance it will be below 23°C."

- **Focus on Uncertainty:** Probabilistic forecasting explicitly acknowledges and quantifies the inherent uncertainty in predicting the future. It recognizes that a single number is rarely sufficient to capture the range of possibilities.

- **Outputs a Distributions:** The result of a probabilistic forecast is a probability distribution. This distribution can take various forms (e.g., normal, beta, empirical) and assigns a likelihood to each potential future value.
- **richer Information:** Unlike deterministic (point) forecasts, probabilistic forecasts offer a much richer understanding of the potential future. This allows for better risk assessment, scenario planning, and decision-making.

- **Common Methodologies:**
    - Ensemble Methods: Running multiple simulations or models with slightly different initial conditions or parameters and analyzing the distribution of their outputs.
    - Bootstrapping: Resampling historical data to create multiple simulated future scenarios and building a distribution of forecasts.
    - Bayesian Methods: Using probability to represent uncertainty about model parameters and updating these probabilities as new data becomes available, leading to a predictive distribution.
    - Quantile Regression: Directly estimating different quantiles of the future distribution.
    - Distributional Regression: Modeling the parameters of a probability distribution as a function of input variables.


# Time Series Foundation Models
Time series foundation models are a relatively new and rapidly evolving area in time series analysis. Drawing inspiration from the success of foundation models in Natural Language Processing (like large language models) and Computer Vision, the goal is to create large, pre-trained models on vast amounts of diverse time series data that can then be adapted or fine-tuned for various downstream forecasting and analysis tasks with minimal task-specific training.


## Examples of Time Series Foundation Models:

- TimesFM (Google Research): A decoder-only transformer model pre-trained on a large corpus of real-world time series data, demonstrating strong zero-shot performance.
- Lag-Llama: A foundation model for probabilistic time series forecasting that uses lags as covariates and outputs a probability distribution.
- Chronos (Amazon): Another foundation model focused on zero-shot and few-shot time series forecasting.