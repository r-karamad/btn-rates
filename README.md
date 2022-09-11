# BTC to Currency Exchange Rates
This repo contains a small Django app for getting bitcoin exchange rates to other currencies.
- It calls https://api.coingecko.com/api/v3/exchange_rates and shows the return JSON in a proper way.

## How to build image
- Push your change into 'main' branch
- Pipeline builds a docker image  and pushes it to dockerhub which will be used by the helm chart in order to deploy.
- Dockerhub repo: https://hub.docker.com/r/karamad/btn-rates


## Test cases
- Homepage
- Coingecko API
