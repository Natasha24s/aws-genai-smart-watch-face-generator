
# AWS GenAI Smart Watch Face Generator

A comprehensive solution for generating smart watch faces using AWS Generative AI services. This project combines Streamlit for the frontend with AWS services (Lambda, API Gateway, and Amazon Bedrock) to create customized watch faces through AI generation.

![Project Banner - Add your project banner image here]

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Streamlit Integration](#streamlit-installation)
- [Deploy Configuration](#deploy-configuration)
- [Use Case](#use-case)
- [Output](#output)

## Features

### Watch Face Styles
- **Business**: Minimal and elegant design for professionals
- **Fitness**: Dynamic layout focused on activity tracking
- **Industrial**: Robust interface with sensor displays
- **Medical**: Health monitoring focused interface
- **Cartoon**: Playful animated designs
- **Sky**: Nature-inspired weather themes

### Customizable Metrics
#### Business Metrics
- Time and Date
- Calendar
- Appointments
- Weather
- Battery

#### Fitness Metrics
- Heart Rate
- Steps
- Calories
- Distance

#### Medical Metrics
- Heart Rate
- Blood Oxygen
- ECG
- Steps

### User Interface Features
- Real-time preview
- Interactive metric selection
- Style descriptions
- Download capabilities
- Generated image storage

## Architecture

## Technologies Used

## Streamlit Integration

1. Download the zip files from `https://github.com/Natasha24s/streamlit.git`
2. Open the file in Visual code. Select the following option to install dependency.

3. In the Streamlit app code, update the `app.py` file to ue your own API Gateway endpoint URL you got in your CFN deployment.

![Alt text](https://github.com/Natasha24s/streamlit/blob/main/images/api.png)

4. Run the app: `streamlit run src/app.py`

![Alt text](https://github.com/Natasha24s/streamlit/blob/main/images/run.png)

It will show up in your browser as shown below:

![](https://github.com/Natasha24s/streamlit/blob/main/images/UI.png)



## Use Case

## Output


