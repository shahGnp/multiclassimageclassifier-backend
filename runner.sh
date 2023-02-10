#!/bin/bash

  
  . ./multiclassimageclassifier-backend/fastAPI/bin/activate
  cd multiclassimageclassifier-backend
  uvicorn main:app --reload --host 0.0.0.0 --port 80
