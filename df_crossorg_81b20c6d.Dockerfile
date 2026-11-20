FROM nginx:1.27.5 AS baseline
FROM python:3.11.0b1-buster AS cross_org_probe
