# BTC to Currency Exchange Rates
This repo contains a small Django app for getting bitcoin exchange rates to other currencies.

## How to build image
- Push your change into 'main' branch
- Pipeline builds a docker image  and pushes it to dockerhub which will be used by the helm chart in order to deploy.

## Test Cases
- Homepage
- Coingecko API
