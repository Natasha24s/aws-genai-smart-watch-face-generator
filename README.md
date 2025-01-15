
# AWS GenAI Smart Watch Face Generator

A comprehensive solution for generating smart watch faces using AWS Generative AI services. This project combines Streamlit for the frontend with AWS services (Lambda, API Gateway, and Amazon Bedrock) to create customized watch faces through AI generation.

![Project Banner - Add your project banner image here]

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Deploy Configuration](#deploy-configuration)
- [Streamlit Integration](#streamlit-installation)
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
```
- Time and Date
- Calendar
- Appointments
- Weather
- Battery
```

#### Fitness Metrics
```
- Heart Rate
- Steps
- Calories
- Distance
```
#### Medical Metrics
```
- Heart Rate
- Blood Oxygen
- ECG
- Steps
```

### User Interface Features
```
- Real-time preview
- Interactive metric selection
- Style descriptions
- Download capabilities
- Generated image storage
```

## Architecture

## Technologies Used

### Frontend Technologies

```
- Streamlit (v1.31.0+)
  - Python-based web framework
  - Interactive UI components
  - Real-time updates
  - Session state management
  - File upload/download handling

- Python Libraries
  - `requests`: HTTP requests handling
  - `Pillow (PIL)`: Image processing
  - `base64`: Image encoding/decoding
  - `io`: Binary I/O handling
  - `datetime`: Timestamp management
```

## AWS Services
```
1. Amazon API Gateway
   - RESTful API endpoints
   - Request/Response handling
   - CORS support
   - API key management
   - Request throttling
   - API documentation

2. AWS Lambda
   - Python 3.9 runtime
   - Serverless compute
   - Event-driven architecture
   - Auto-scaling capability
   - Cost-effective execution

3. Amazon Bedrock
   - Stability AI integration
   - Foundation model access
   - Secure API endpoints
   - Pay-per-use pricing
   - Low-latency responses

4. AWS CloudFormation
   - Infrastructure as Code (IaC)
   - Stack management
   - Resource provisioning
   - Parameter management
   - Cross-stack references

5. AWS IAM
   - Role-based access control
   - Security policies
   - Permission management
   - Resource-level security
   - Least privilege principle
```

## Development Tools
```
- Git: Version control
- GitHub: Code repository
- VS Code: Code editor
- AWS CLI: AWS service management
- Postman: API testing
```

## Programming Languages
```
- Python: Backend & Frontend
- YAML: CloudFormation templates
- JSON: API communication
- CSS: UI styling
- Markdown: Documentation
```

## Deploy Configuration

1. Download the [watch.yaml](https://github.com/Natasha24s/aws-genai-smart-watch-face-generator/blob/main/watch.yaml) file.
2. Open AWS and select a region of your choice.
3. Open Cloudformation and click on Create Stack and select the downloaded template.
4. It will deploy the following resources:
     - API Gateway
     - Lambda Function
     - IAM Roles and Policies

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


| Use Case | Scenario | Implementation | Example Code |
|----------|----------|----------------|--------------|
| **1. Custom Watch Face Design Studios** | Design studios creating custom watch faces for different smart watch brands | • Multiple style templates<br>• Brand-specific customizations<br>• Bulk generation capability<br>• Style consistency checks |Some code here:<br><pre lang="json">{&#13;  "id": 10,&#13;  "username": "alanpartridge"&#13;}</pre> |
| **2. Healthcare Monitoring** | Medical facilities requiring specialized watch faces for patient monitoring | • Health metric prioritization<br>• Emergency alert displays<br>• Medical data integration<br>• Compliance with health standards | ```python<br># Medical Watch Face<br>medical_metrics = [<br>    "Heart Rate",<br>    "Blood Oxygen",<br>    "ECG",<br>    "Medication Alerts"<br>]<br>generate_watch_face("Medical", medical_metrics)``` |
| **3. Industrial Applications** | Manufacturing plants needing watch faces for worker safety and monitoring | • Environmental sensor displays<br>• Safety alert integration<br>• Machine status monitoring<br>• Quick response triggers | ```python<br># Industrial Watch Face<br>industrial_metrics = [<br>    "Temperature",<br>    "Humidity",<br>    "Gas Levels",<br>    "Emergency Alerts"<br>]<br>generate_watch_face("Industrial", industrial_metrics)``` |
| **4. Fitness and Sports** | Fitness centers and sports teams requiring specialized activity tracking | • Performance metrics display<br>• Workout tracking<br>• Team coordination<br>• Competition modes | ```python<br># Fitness Watch Face<br>fitness_metrics = [<br>    "Heart Rate",<br>    "Steps",<br>    "Distance",<br>    "Calories"<br>]<br>generate_watch_face("Fitness", fitness_metrics)``` |
| **5. Corporate Branding** | Companies wanting branded watch faces for employee smart watches | • Brand color integration<br>• Logo placement<br>• Corporate event reminders<br>• Team coordination features | ```python<br># Corporate Watch Face<br>corporate_metrics = [<br>    "Time",<br>    "Meetings",<br>    "Team Updates",<br>    "Goals"<br>]<br>generate_watch_face("Business", corporate_metrics)``` |
| **6. Educational Institutions** | Schools using smart watches for student scheduling and activities | • Class schedule display<br>• Assignment reminders<br>• Emergency notifications<br>• Parent communication | ```python<br># Educational Watch Face<br>education_metrics = [<br>    "Schedule",<br>    "Assignments",<br>    "Alerts",<br>    "Activities"<br>]<br>generate_watch_face("Cartoon", education_metrics)``` |

  
## 1. Custom Watch Face Design Studios
```
### Scenario
Design studios creating custom watch faces for different smart watch brands.
### Implementation
- Multiple style templates
- Brand-specific customizations
- Bulk generation capability
- Style consistency checks

```python
# Example: Bulk Generation
styles = ["Business", "Fitness", "Medical"]
for style in styles:
    metrics = get_style_metrics(style)
    generate_watch_face(style, metrics)
```
    
## 2. Healthcare Monitoring
```
Scenario
Medical facilities requiring specialized watch faces for patient monitoring.

Implementation
Health metric prioritization
Emergency alert displays
Medical data integration
Compliance with health standards
    
# Example: Medical Watch Face
medical_metrics = [
    "Heart Rate",
    "Blood Oxygen",
    "ECG",
    "Medication Alerts"
]
generate_watch_face("Medical", medical_metrics)

```
    
## 3. Industrial Applications

```
Scenario
Manufacturing plants needing watch faces for worker safety and monitoring.

Implementation
Environmental sensor displays
Safety alert integration
Machine status monitoring
Quick response triggers

# Example: Industrial Watch Face
industrial_metrics = [
    "Temperature",
    "Humidity",
    "Gas Levels",
    "Emergency Alerts"
]
generate_watch_face("Industrial", industrial_metrics)

 ```

## 4. Fitness and Sports

```   
Scenario
Fitness centers and sports teams requiring specialized activity tracking.

Implementation
Performance metrics display
Workout tracking
Team coordination
Competition modes
    
# Example: Fitness Watch Face
fitness_metrics = [
    "Heart Rate",
    "Steps",
    "Distance",
    "Calories"
]
generate_watch_face("Fitness", fitness_metrics)
```
    
## 5. Corporate Branding
```
Scenario
Companies wanting branded watch faces for employee smart watches.

Implementation
Brand color integration
Logo placement
Corporate event reminders
Team coordination features
    
# Example: Corporate Watch Face
corporate_metrics = [
    "Time",
    "Meetings",
    "Team Updates",
    "Goals"
]
generate_watch_face("Business", corporate_metrics)
```
    
## 6. Educational Institutions
```
Scenario
Schools using smart watches for student scheduling and activities.

Implementation
Class schedule display
Assignment reminders
Emergency notifications
Parent communication
    
# Example: Educational Watch Face
education_metrics = [
    "Schedule",
    "Assignments",
    "Alerts",
    "Activities"
]
generate_watch_face("Cartoon", education_metrics)
```

## Output

Output for Cartoon Watch Face Style:
![](https://github.com/Natasha24s/aws-genai-smart-watch-face-generator/blob/main/images/cartoon.png)

Output for Business Watch Face Style:
![](https://github.com/Natasha24s/aws-genai-smart-watch-face-generator/blob/main/images/businesses.png)

Output for Fitness Watch Face Style:
![](https://github.com/Natasha24s/aws-genai-smart-watch-face-generator/blob/main/images/fitness.png)

Output for Run Watch Face Style:
![](https://github.com/Natasha24s/aws-genai-smart-watch-face-generator/blob/main/images/sky.png)

Output for Industrial Watch Face Style:
![](https://github.com/Natasha24s/aws-genai-smart-watch-face-generator/blob/main/images/industrial.png)

