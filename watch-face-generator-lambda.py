import json
import boto3
import base64

def get_stability_params(style):
    params = {
        "Business": {
            "cfg_scale": 8,
            "steps": 50,
            "seed": 42
        },
        "Fitness": {
            "cfg_scale": 9,
            "steps": 50,
            "seed": 123
        },
        "Industrial": {
            "cfg_scale": 10,
            "steps": 50,
            "seed": 456
        },
        "Medical": {
            "cfg_scale": 7,
            "steps": 50,
            "seed": 789
        },
        "Cartoon": {
            "cfg_scale": 12,
            "steps": 55,
            "seed": 234
        },
        "Sky": {
            "cfg_scale": 9,
            "steps": 60,
            "seed": 567
        }
    }
    return params.get(style, params["Business"])

def create_prompt(style, metrics):
    prompts = {
        "Business": "Create a minimal, elegant smart watch face with dark background, professional design, luxury watch style",
        "Fitness": "Design a sporty smart watch face with activity metrics, dynamic layout, vibrant colors",
        "Industrial": "Generate a robust industrial smart watch face with sensor displays, metallic texture, steampunk elements",
        "Medical": "Create a medical-focused smart watch face with health metrics, clean white interface, medical symbols",
        "Cartoon": "Design a playful cartoon smart watch face with cute animated characters, bright colors, fun elements, kawaii style, digital watch display",
        "Sky": "Create a smart watch face featuring beautiful sky scenery, cloud patterns, sun/moon phases, weather elements, gradient colors"
    }
    
    style_details = {
        "Business": ", minimalist typography, executive style",
        "Fitness": ", performance tracking layout",
        "Industrial": ", industrial gauge designs, mechanical elements",
        "Medical": ", vital signs styling, medical dashboard",
        "Cartoon": ", Disney/Pixar inspired, animated elements",
        "Sky": ", atmospheric gradients, weather icons"
    }
    
    base_prompt = prompts.get(style, prompts["Business"])
    style_detail = style_details.get(style, "")
    metrics_prompt = f" including displays for {', '.join(metrics)}"
    return base_prompt + metrics_prompt + style_detail

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        style = body['style']
        metrics = body['metrics']
        
        bedrock = boto3.client('bedrock-runtime')
        prompt = create_prompt(style, metrics)
        style_params = get_stability_params(style)
        
        response = bedrock.invoke_model(
            modelId='stability.stable-diffusion-xl-v1',
            body=json.dumps({
                "text_prompts": [{"text": prompt}],
                "cfg_scale": style_params["cfg_scale"],
                "steps": style_params["steps"],
                "seed": style_params["seed"]
            })
        )
        
        response_body = json.loads(response['body'].read())
        image_data = response_body['artifacts'][0]['base64']
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({
                'image': image_data
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({
                'error': str(e)
            })
        }
