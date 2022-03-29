# Hellofresh to MyFitnessPal REST API
This is just a simple REST API I'm going to deploy on my home computer or raspberry pi that I will call from my phone with a recipe id so it automatically adds it to myFitnessPal.

## Process
It will use Selenium to simulate a headless browser and fetch the meal information from hellofresh's webiste. Then it would post the macros into myfitnesspal using selenium again. Unfortunately, the companies don't have API endpoints for these particular activities.