# Tecnhical Challenge PRGX
 
---
This API returns the addition of two given number *x* and *y* that are passed through the *POST request body*

![](https://p3y6v9e6.stackpathcdn.com/wp-content/uploads/zikoko/2020/06/saving-things-to-cart.gif)

## Environment

GNU/Linux 

## How to install
1. Clone the repository below

`https://github.com/johnconnor77/tecnhical_challenge_PRGX`

2. Install dependencies from requirements.txt

`pip install -r requirements.txt`

3. Execute the following command for Application startup at repository root

`/sum_api_prgx.py `

---



##  Files

File Name | Description
--- | ---
`sum_api_prgx.py` | Executable file for API schema that will retrieve the addition of two digits
`sum_inout/__init__.py` |  Module with SumModel class that specifies the format and data type of input by User post request
`requirements.txt & runtime.txt` |  Files that specifies python runtime version and requirements of modules
`Procfile` |  File that specifies the commands that are executed by the app on startup

## Example Usage

### Local Example

#### cURL

Type the following command at your shell prompt

`curl --location --request POST 'http://127.0.0.1:5000/api/sum/' --header 'Content-Type: application/json' --data-raw '{"x": 1801, "y":20}'`



<img align="center" src="https://i.ibb.co/7jLMqzm/shellcurl.png" width="100%"/>


### Remote Example 

Sum API was deployed at Heroku where you can also test it from the docs enpoint


[https://jconnor-prgx-sum-api.herokuapp.com/docs](https://jconnor-prgx-sum-api.herokuapp.com/docs/)


### Postman


<img align="center" src="https://i.ibb.co/QPDcKXH/postman-sum.png" width="100%"/>


Author:

* **Juan F. Calle**  - [johnconnor77](https://github.com/johnconnor77)
