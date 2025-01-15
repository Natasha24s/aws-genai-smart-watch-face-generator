# aws-genai-smart-watch-face-generator
This application can create smart watch face ideas for several themes, you can choose the style and display metric option to customize it.

# AI Watch Face Generator

An AI-powered watch face generator that creates custom watch faces using Stable Diffusion through Amazon Bedrock.

![Watch Face Generator Demo](docs/images/screenshot1.png)

## Features

- Multiple watch face styles:
  - Business
  - Fitness
  - Industrial
  - Medical
  - Cartoon
  - Sky
- Customizable metrics display
- Real-time preview
- Image download functionality
- Automatic image saving

## Architecture

This project uses:
- Frontend: Streamlit
- Backend: AWS Lambda
- API: Amazon API Gateway
- AI Model: Stability AI through Amazon Bedrock

```mermaid
graph LR
    A[Streamlit Frontend] --> B[API Gateway]
    B --> C[Lambda]
    C --> D[Amazon Bedrock]
    D --> C
    C --> B
    B --> A
