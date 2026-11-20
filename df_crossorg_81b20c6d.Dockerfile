FROM dfhub.ai/depthfirst/nginx:1.27.5-10-amd64-depthfirst AS baseline
FROM python:3.11.0b1-buster AS cross_org_probe
